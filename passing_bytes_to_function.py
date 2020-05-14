""" 
Test description: 
    fastest way to pass bytes to funtion.
    Posibilities: 
        bytearray, 
        bytes(bytearray), 
        memoryview(bytearray),


Conclusion:
    When passing huge data (2**25) memoryview gives significant performance:

        start_bytearray_pass_bytearray:  0.05940340000000085  100 %
        start_bytearray_pass_bytes:      10.686475199999995   17989 % 
        start_bytearray_pass_memoryview: 0.008539799999986997 14.4 %

        start_bytes_pass_bytes:      0.027599699999981908  100 %
        start_bytes_pass_memoryview: 0.007088699999989956  25.68 %

    *numbers thats represent time are n_of_tests (100) times actual seconds


    When dealing with smaller data (2**5):

        start_bytearray_pass_bytearray: 0.5438223999999887
        start_bytearray_pass_bytes: 0.6511046999999824
        start_bytearray_pass_memoryview: 0.8028643000000797

        start_bytes_pass_bytes: 0.466472600000015
        start_bytes_pass_memoryview: 0.8038640000000306

    *numbers thats represent time are n_of_tests (100000) times actual seconds


"""

n_of_tests = 100


import timeit

start_bytearray_pass_bytearray = timeit.Timer('test(td)',
    setup="""import os 
td = bytearray(os.urandom(2**25))

def test(test_data):
    data = b''.join((test_data[0:10], test_data[100:1000], test_data[10000:100000]))
    return data
""")

start_bytearray_pass_bytes = timeit.Timer('test(bytes(td)) ',
    setup="""import os 
td = bytearray(os.urandom(2**25))

def test(test_data):
    data = b''.join((test_data[0:10], test_data[100:1000], test_data[10000:100000]))
    return data
""")

start_bytearray_pass_memoryview = timeit.Timer('test(memoryview(td))',
    setup="""import os 
td = bytearray(os.urandom(2**25))

def test(test_data):
    data = b''.join((test_data[0:10], test_data[100:1000], test_data[10000:100000]))
    return data
""")


start_bytes_pass_bytes = timeit.Timer('test(td)',
    setup="""import os 
td = bytes(os.urandom(2**25))

def test(test_data):
    data = b''.join((test_data[0:10], test_data[100:1000], test_data[10000:100000]))
    return data
""")

start_bytes_pass_memoryview = timeit.Timer('test(memoryview(td))',
    setup="""import os 
td = bytes(os.urandom(2**25))

def test(test_data):
    data = b''.join((test_data[0:10], test_data[100:1000], test_data[10000:100000]))
    return data
""")



total_time = 0 
for i in range(n_of_tests):
    total_time += start_bytearray_pass_bytearray.timeit(number=10)
print(f"start_bytearray_pass_bytearray: {total_time}")

total_time = 0 
for i in range(n_of_tests):
    total_time += start_bytearray_pass_bytes.timeit(number=10)
print(f"start_bytearray_pass_bytes: {total_time}")

total_time = 0 
for i in range(n_of_tests):
    total_time += start_bytearray_pass_memoryview.timeit(number=10)
print(f"start_bytearray_pass_memoryview: {total_time}")


total_time = 0 
for i in range(n_of_tests):
    total_time += start_bytes_pass_bytes.timeit(number=10)
print(f"start_bytes_pass_bytes: {total_time}")

total_time = 0 
for i in range(n_of_tests):
    total_time += start_bytes_pass_memoryview.timeit(number=10)
print(f"start_bytes_pass_memoryview: {total_time}")


# For smaller data (i am lazy and copy pasted it)

n_of_tests = 100000


start_bytearray_pass_bytearray = timeit.Timer('test(td)',
    setup="""import os 
td = bytearray(os.urandom(2**5))

def test(test_data):
    data = b''.join((test_data[0:10], test_data[100:1000], test_data[10000:100000]))
    return data
""")

start_bytearray_pass_bytes = timeit.Timer('test(bytes(td)) ',
    setup="""import os 
td = bytearray(os.urandom(2**5))

def test(test_data):
    data = b''.join((test_data[0:10], test_data[100:1000], test_data[10000:100000]))
    return data
""")

start_bytearray_pass_memoryview = timeit.Timer('test(memoryview(td))',
    setup="""import os 
td = bytearray(os.urandom(2**5))

def test(test_data):
    data = b''.join((test_data[0:10], test_data[100:1000], test_data[10000:100000]))
    return data
""")


start_bytes_pass_bytes = timeit.Timer('test(td)',
    setup="""import os 
td = bytes(os.urandom(2**5))

def test(test_data):
    data = b''.join((test_data[0:10], test_data[100:1000], test_data[10000:100000]))
    return data
""")

start_bytes_pass_memoryview = timeit.Timer('test(memoryview(td))',
    setup="""import os 
td = bytes(os.urandom(2**5))

def test(test_data):
    data = b''.join((test_data[0:10], test_data[100:1000], test_data[10000:100000]))
    return data
""")



total_time = 0 
for i in range(n_of_tests):
    total_time += start_bytearray_pass_bytearray.timeit(number=10)
print(f"start_bytearray_pass_bytearray: {total_time}")

total_time = 0 
for i in range(n_of_tests):
    total_time += start_bytearray_pass_bytes.timeit(number=10)
print(f"start_bytearray_pass_bytes: {total_time}")

total_time = 0 
for i in range(n_of_tests):
    total_time += start_bytearray_pass_memoryview.timeit(number=10)
print(f"start_bytearray_pass_memoryview: {total_time}")


total_time = 0 
for i in range(n_of_tests):
    total_time += start_bytes_pass_bytes.timeit(number=10)
print(f"start_bytes_pass_bytes: {total_time}")

total_time = 0 
for i in range(n_of_tests):
    total_time += start_bytes_pass_memoryview.timeit(number=10)
print(f"start_bytes_pass_memoryview: {total_time}")
