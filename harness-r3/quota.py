"""Print the most recent rate_limit_event seen in any episode stream (five-hour / seven-day utilisation).

  python3 quota.py [runs/]
AMENDMENT_r3 §12.4: do not start a batch above 80 % seven-day or 85 % five-hour.
"""
import glob
import json
import os
import sys
import time

root = sys.argv[1] if len(sys.argv) > 1 else "runs"
files = sorted(glob.glob(os.path.join(root, "*", "*", "stdout.jsonl")), key=os.path.getmtime)
last = None
for f in files[-5:]:
    for line in open(f, encoding="utf-8"):
        if '"rate_limit_event"' in line:
            try:
                last = json.loads(line)
            except json.JSONDecodeError:
                pass
if not last:
    print("no rate_limit_event found under", root)
    sys.exit(1)
info = last["rate_limit_info"]["unifiedWindows"]
for w in ("five_hour", "seven_day"):
    u = info[w]["utilization"]
    reset = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(info[w]["resetsAt"]))
    print(f"{w}: {u:.0%} (resets {reset})")
ok = info["seven_day"]["utilization"] <= 0.80 and info["five_hour"]["utilization"] <= 0.85
print("batch allowed by §12.4:", ok)
