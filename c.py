
import time
def range_with_status(total):
    import sys
    n = 0
    while n < total:
        done = '#' * (n + 1)
        todo = '-' * (total - n - 1)
        s = '<{0}>'.format(done + todo)
        if not todo:
            s += '\n'
        if n > 0:
            s = '\r' + s
        print(s, end='\r')
        sys.stdout.flush()
        yield n
        n += 1
for i in range_with_status(40):
    time.sleep(0.05)
