import time
import sys


def update_pct(w_str):
    w_str = str(w_str)
    sys.stdout.write("\b" * len(w_str))
    sys.stdout.write(" " * len(w_str))
    sys.stdout.write("\b" * len(w_str))
    sys.stdout.write(w_str)
    sys.stdout.flush()

for pct in range(0, 101):
    update_pct("{n}%".format(n=str(pct)))
    time.sleep(0.1)
