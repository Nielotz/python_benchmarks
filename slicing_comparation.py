""" 
Test description: 
    fastest way of making a copy of data from n to m(end of list).
    Possibilities: list[n:], list[n:m], bonus: list[n:m:1]

Conclusion:
    [n:]    18.5953381  +0%
    [n:m]   19.2968721  +3.772%
    [n:m:1] 20.3518034  +9.445%

    [n:]    18.4176889  +0%
    [n:m]   19.1895338  +4.190%
    [n:m:1] 20.1841517  +9.591%

"""

import timeit

to_end = timeit.Timer('[td[i:] for i in range(100)]',
                      setup='import random; td = (*[random.random() for i in range(100)],)')

to_m = timeit.Timer('[td[i:100] for i in range(100)]',
                    setup='import random; td = (*[random.random() for i in range(100)],)')

to_m_extended = timeit.Timer('[td[i:100:1] for i in range(100)]',
                             setup='import random; td = (*[random.random() for i in range(100)],)')

print(f"[n:] {to_end.timeit()}")
print(f"[n:m] {to_m.timeit()}")
print(f"[n:m:1] {to_m_extended.timeit()}")
