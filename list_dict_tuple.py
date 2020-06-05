raise RuntimeError("Not runnable")
# Extension 'py' to enable syntax coloring.

### [TEST TYPE] description 

### [PERFORMANCE READ] dict vs list vs tuple
python -m timeit -s "x = {'a': 1, 'b': 2}" "x['a']"
10000000 loops, best of 5: 27 nsec per loop

python -m timeit -s "x = [1, 2]" "x[0]"
10000000 loops, best of 5: 34 nsec per loop

python -m timeit -s "x = (1, 2)" "x[0]"
10000000 loops, best of 5: 36 nsec per loop
### Result: dict, list, tuple

### [PERFORMANCE WRITE] dict vs list
python -m timeit -s "x = {'a': 1, 'b': 2}" "x['a'] = 2; x['b'] = 1"
5000000 loops, best of 5: 56.6 nsec per loop

python -m timeit -s "x = [1, 2]" "x[0] = 2; x[1] = 1"
5000000 loops, best of 5: 59.9 nsec per loop
### Result: dict, list


### [PERFORMANCE CREATE] dict vs list vs tuple
python -m timeit -s "x = {'a': 1, 'b': 2}" "x = {'a': 2, 'b': 1}"
5000000 loops, best of 5: 66.4 nsec per loop

python -m timeit -s "x = [1, 2]" "x = [2, 1]"
5000000 loops, best of 5: 44.2 nsec per loop

python -m timeit -s "x = (1, 2)" "x = (2,1)"
20000000 loops, best of 5: 10.1 nsec per loop
### Result: tuple, list, dict

