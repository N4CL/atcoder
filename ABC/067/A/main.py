# coding: utf-8

a, b = map(int, raw_input().split())

if a % 3 == 0:
    print "Possible"
elif b % 3 == 0:
    print "Possible"
elif (a + b) % 3 == 0:
    print "Possible"
else:
    print "Impossible"
