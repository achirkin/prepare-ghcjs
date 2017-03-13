#!/usr/bin/env python

import json, sys, time

def isint(x):
    try:
        int(x)
        return True
    except:
        return False

if len(sys.argv) > 2 and isint(sys.argv[1]) and isint(sys.argv[2]):
    sys.argv.pop(1)

count = int(sys.argv[1])

for n in sys.argv[2:]:
    print '%s:' % n
    obj = json.load(open(n))
    start = time.time()
    for i in xrange(count):
        json.dumps(obj)
    end = time.time()
    print '  %d good, %gs' % (count, end - start)
