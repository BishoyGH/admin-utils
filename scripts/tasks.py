#!/usr/bin/env python3
"""Task CLI for docs/tasks. No dependencies. Run from the repo root."""
import argparse, csv, glob, io, json, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASKS = os.path.join(ROOT, "docs", "tasks")
SPECS = os.path.join(ROOT, "docs", "specs")
STATUSES = ["todo", "ready", "in-progress", "in-review", "blocked", "done"]
PRIO = {"P0": 0, "P1": 1, "P2": 2}

def parse(path):
    text = open(path, encoding="utf8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fm = {}
    for line in m.group(1).split("\n"):
        k, _, v = line.partition(": ")
        v = v.strip()
        if v.startswith("["):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        elif v.startswith('"'):
            v = json.loads(v)
        elif v in ("true", "false"):
            v = v == "true"
        elif re.fullmatch(r"\d+", v):
            v = int(v)
        fm[k] = v
    fm["_path"] = path
    return fm

def load():
    out = {}
    for p in glob.glob(os.path.join(TASKS, "*", "*-[0-9][0-9][0-9].md")):
        t = parse(p)
        out[t["id"]] = t
    return out

def modules():
    mods = {}
    for p in sorted(glob.glob(os.path.join(SPECS, "[0-9][0-9]-*.md"))):
        s = parse(p)
        mods[s["code"]] = s
    return mods

def key(t):
    return (t["wave"], PRIO[t["priority"]], t["module"], t["id"])

def filt(tasks, a):
    r = list(tasks.values())
    for f in ("module", "wave", "priority", "status"):
        v = getattr(a, f, None)
        if v is not None:
            r = [t for t in r if str(t[f]) == str(v)]
    return sorted(r, key=key)

def line(t):
    return f'{t["id"]:10} {t["priority"]} w{t["wave"]:<2} {t["status"]:11} {t["title"]}'

def cmd_list(a, tasks):
    for t in filt(tasks, a): print(line(t))

def cmd_show(a, tasks):
    t = tasks.get(a.id)
    if not t: sys.exit(f"unknown task {a.id}")
    print(open(t["_path"], encoding="utf8").read())

def cmd_next(a, tasks):
    cands = [t for t in filt(tasks, a) if t["status"] in ("todo", "ready")
             and all(tasks.get(r, {"status": "done"})["status"] == "done" for r in t["references"])]
    if a.role:
        cands = [t for t in cands if any(a.role in x for x in t["roles"])]
    if not cands: sys.exit("no pickable task")
    for t in cands[: a.n]: print(line(t)); print("   ", os.path.relpath(t["_path"], ROOT))

def set_field(t, field, value):
    p = t["_path"]
    s = open(p, encoding="utf8").read()
    s2, n = re.subn(rf"^{field}: .*$", f"{field}: {value}", s, count=1, flags=re.M)
    assert n == 1
    open(p, "w", encoding="utf8").write(s2)

def cmd_set_status(a, tasks):
    if a.status not in STATUSES: sys.exit(f"status must be one of {STATUSES}")
    t = tasks.get(a.id) or sys.exit(f"unknown task {a.id}")
    set_field(t, "status", a.status); print(f"{a.id} -> {a.status}"); reindex(quiet=True)

def cmd_set_wave(a, tasks):
    t = tasks.get(a.id) or sys.exit(f"unknown task {a.id}")
    set_field(t, "wave", a.wave); print(f"{a.id} -> wave {a.wave}"); reindex(quiet=True)

def cmd_stats(a, tasks):
    c = collections.Counter(t["status"] for t in tasks.values()); tot = len(tasks)
    print(f"{tot} tasks: " + ", ".join(f"{s} {c[s]}" for s in STATUSES))
    for w in sorted({t["wave"] for t in tasks.values()}):
        ts = [t for t in tasks.values() if t["wave"] == w]
        d = sum(t["status"] == "done" for t in ts)
        print(f"  wave {w:<2} {d:4}/{len(ts):<4} done")

def cmd_validate(a, tasks):
    bad = []
    for t in tasks.values():
        if t["status"] not in STATUSES: bad.append(f'{t["id"]}: bad status {t["status"]}')
        if os.path.basename(t["_path"]) != t["id"] + ".md": bad.append(f'{t["id"]}: file name mismatch')
        for r in t["references"]:
            if r not in tasks: bad.append(f'{t["id"]}: reference {r} not found')
        if not os.path.exists(os.path.join(ROOT, t["spec"])): bad.append(f'{t["id"]}: spec missing')
    print("\n".join(bad) if bad else f"ok: {len(tasks)} tasks valid"); sys.exit(1 if bad else 0)

def reindex(quiet=False):
    tasks = load(); mods = modules()
    rows = [dict(id=t["id"], module=t["module"], group=t["group"], priority=t["priority"], wave=t["wave"],
                 status=t["status"], title=t["title"], file=os.path.relpath(t["_path"], ROOT).replace(os.sep, "/"))
            for t in sorted(tasks.values(), key=lambda x: (list(mods).index(x["module"]) if x["module"] in mods else 99, x["id"]))]
    json.dump(rows, open(os.path.join(TASKS, "tasks.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)
    s = io.StringIO(); w = csv.DictWriter(s, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    open(os.path.join(TASKS, "tasks.csv"), "w", encoding="utf8", newline="").write(s.getvalue())
    byc = collections.defaultdict(list)
    for r in rows: byc[r["module"]].append(r)
    for c, rs in byc.items():
        spec = os.path.basename(mods[c]["_path"]) if c in mods else ""
        L = [f"# {c} — {mods[c]['title'] if c in mods else c}: tasks", "",
             f"Spec: [`{spec}`](../../specs/{spec}) · {len(rs)} tasks · done {sum(r['status']=='done' for r in rs)}", ""]
        cur = None
        for r in rs:
            if r["group"] != cur:
                cur = r["group"]; L += ["", f"## {cur}", "", "| ID | P | Wave | Status | Title |", "|---|---|---|---|---|"]
            L.append(f"| [{r['id']}]({r['id']}.md) | {r['priority']} | {r['wave']} | {r['status']} | {r['title'].replace('|','/')} |")
        open(os.path.join(TASKS, c, "INDEX.md"), "w", encoding="utf8").write("\n".join(L) + "\n")
    tot = collections.Counter(r["priority"] for r in rows)
    L = ["# Task index", "", f"{len(rows)} tasks · " + " · ".join(f"{k}: {v}" for k, v in sorted(tot.items())) +
         f" · done {sum(r['status']=='done' for r in rows)}", "",
         "Status lives in each task file front matter. Query and update with `python scripts/tasks.py` (see `README.md`).", "",
         "| Module | Code | Tasks | P0 | P1 | P2 | Done | Privileged |", "|---|---|---|---|---|---|---|---|"]
    for c in mods:
        rs = byc.get(c, []); cc = collections.Counter(r["priority"] for r in rs)
        L.append(f"| [{mods[c]['title']}]({c}/INDEX.md) | {c} | {len(rs)} | {cc['P0']} | {cc['P1']} | {cc['P2']} | "
                 f"{sum(r['status']=='done' for r in rs)} | {'yes' if mods[c]['privileged'] else ''} |")
    open(os.path.join(TASKS, "INDEX.md"), "w", encoding="utf8").write("\n".join(L) + "\n")
    if not quiet: print(f"reindexed {len(rows)} tasks")

def main():
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    for n in ("list", "next"):
        p = sp.add_parser(n)
        p.add_argument("--module"); p.add_argument("--wave", type=int); p.add_argument("--priority"); p.add_argument("--status")
        if n == "next": p.add_argument("--role"); p.add_argument("-n", type=int, default=1)
    sp.add_parser("show").add_argument("id")
    p = sp.add_parser("set-status"); p.add_argument("id"); p.add_argument("status")
    p = sp.add_parser("set-wave"); p.add_argument("id"); p.add_argument("wave", type=int)
    for n in ("stats", "validate", "reindex"): sp.add_parser(n)
    a = ap.parse_args()
    if a.cmd == "reindex": return reindex()
    tasks = load()
    {"list": cmd_list, "show": cmd_show, "next": cmd_next, "set-status": cmd_set_status, "set-wave": cmd_set_wave,
     "stats": cmd_stats, "validate": cmd_validate}[a.cmd](a, tasks)

if __name__ == "__main__":
    main()
