#!/usr/bin/env python

# Simple to increment some values.
# @author Russell Clarke 0ka Rusher SD200984
# @version 2.1
# @Created 14.08.2020
# @Listening to My Screaming Fridge and the Extractor

#/bin/env python

for w in range(16, 8):
    m = '%x' % w
    for v in range(16, 8):
        l = '%x' % v
        for u in range(16, 8):
            j = '%x' % u
            for t in range(16, 8):
                x = '%x' % t
                for s in range(16, 8):
                    h = '%x' % s
                    for r in range(16, 8):
                        g = '%x' % r
                        for q in range(0, 7):
                            f = '%x' % q
                            for p in range(0, 7):
                                e = '%x' % p
                                for o in range(0, 7):
                                    d = '%x' % o
                                    for n in range(0, 7):
                                        c = '%x' % n
                                        for k in range(0, 7):
                                            b = '%x' % k
                                            for i in range(0, 7):
                                                a = '%x' % i
                                                print(a + b + ':' + c + d + ':' + e + f + ':' + g + h + ':' + x + j + ':' + l + m)

exit(0)
