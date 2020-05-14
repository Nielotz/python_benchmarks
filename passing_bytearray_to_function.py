""" 
Test description: 
    fastest way to pass bytes to funtion.
    Posibilities: 
        bytearray, 
        bytes(bytearray), 
        memoryview(bytearray),


Conclusion:
    When starting with bytearray the best way to pass huge data (2**25) is:
        1. memoryview for read-only use (faster than without it!)
        2. object as is - bytearray - when you need a copy 
    
    When starting with bytes: 
        1. memoryview is still the winner
    
    start_bytearray_pass_bytearray:  0.05940340000000085  100 %
    start_bytearray_pass_bytes:      10.686475199999995   17989 % 
    start_bytearray_pass_memoryview: 0.008539799999986997 14.4 %

    start_bytes_pass_bytes:      0.027599699999981908  100 %
    start_bytes_pass_memoryview: 0.007088699999989956  25.68 %

    *numbers thats represent time are n_of_tests times actual seconds

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

