""" 
Test description: 
    fastest way of making a copy of data from n to m(end of list).
    Posibilities: list[n:], list[n:m], bonus: list[n:m:1]

Conclusion:
    [n:]    18.5953381
    [n:m]   19.2968721
    [n:m:1] 20.3518034

    [n:]    18.4176889
    [n:m]   19.1895338
    [n:m:1] 20.1841517

"""


import timeit
to_end = timeit.Timer(f'[td[i:] for i in range(100)]',
    setup='import random; td = (*[random.random() for i in range(100)],)')

to_m = timeit.Timer(f'[td[i:100] for i in range(100)]',
    setup='import random; td = (*[random.random() for i in range(100)],)')

to_m_extended = timeit.Timer(f'[td[i:100:1] for i in range(100)]',
    setup='import random; td = (*[random.random() for i in range(100)],)')

print(f"[n:] {to_end.timeit()}")
print(f"[n:m] {to_m.timeit()}")
print(f"[n:m:1] {to_m_extended.timeit()}")

