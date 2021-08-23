"""
QUESTION:
    Are bitwise operators faster on a lots of small ints or
    one huge int wchich contains all of them?

TESTS: 
    Some of bitwise operations performed on a range of numbers on different orders of magnitudes.

RESULTS:
    lshift too slow to these tests.

    -----------------------------------------------------------------------------
    minimal_magnitude = 0
    number_of_magnitudes = 50
    random_numbers_per_magnitude = 100

    callout_number  total_time  function
    5100500         0.781        xor
    5100500         0.801        xor_assign
    5100500         0.784        logic_and
    5100500         0.812        logic_and_assign
    5100500         0.783        logic_or
    5100500         0.810        logic_or_assign
    5100500         0.760        rshift
    5100500         0.752        rshift_assign

    Because of small, quite constant difference and to save time decided to
    remove functions *_assign from test. 

    -----------------------------------------------------------------------------
    minimal_magnitude = 50
    number_of_magnitudes = 100 
    random_numbers_per_magnitude = 100

    callout_number  total_time  function
    10201000    1.545    xor
    10201000    1.526    logic_and
    10201000    1.545    logic_or
    10201000    1.620    logic_or_assign
    -----------------------------------------------------------------------------
    minimal_magnitude = 100
    number_of_magnitudes = 150 
    random_numbers_per_magnitude = 100

    callout_number  total_time  function
    15301500    2.330    python_bitwise_small_vs_big_numbers.py:104(logic_or)
    15301500    2.459    python_bitwise_small_vs_big_numbers.py:107(logic_or_assign)
    15301500    2.584    python_bitwise_small_vs_big_numbers.py:118(rshift)
    15301500    2.347    python_bitwise_small_vs_big_numbers.py:90(xor)
    15301500    2.299    python_bitwise_small_vs_big_numbers.py:97(logic_and)
    -----------------------------------------------------------------------------
    minimal_magnitude = 0
    number_of_magnitudes = 50
    random_numbers_per_magnitude = 1000

    callout_number  total_time  function
    501000500   74.871    logic_and
    501000500   75.476    logic_or
    501000500   78.846    logic_or_assign
    501000500   72.545    rshift
    501000500   76.120    xor
    -----------------------------------------------------------------------------

    Dissabled logic_or_assign test.

"""


minimal_magnitude = 0
number_of_magnitudes = 50
random_numbers_per_magnitude = 1000
""" RUN USING:
LINUX:
    python -m cProfile python_bitwise_small_vs_big_numbers.py | grep "python_bitwise_small_vs_big_numbers.py"
WINDOWS:
    python -m cProfile python_bitwise_small_vs_big_numbers.py 
    and find lines with "python_bitwise_small_vs_big_numbers.py"
"""


def get_magnitudes_of_ten(minimal_magnitude, number_of_magnitudes):
    test_numbers_ten_magnituded = [int,] * number_of_magnitudes

    base = 10**minimal_magnitude
    for i in range(number_of_magnitudes):
        test_numbers_ten_magnituded[i] = base
        base = base * 10
    return test_numbers_ten_magnituded

def get_random_numbers_between_magnitudes(magnitudes, random_numbers_per_magnitude):
    import random
    test_random_numbers = []
    shift = 0
    for i in range(len(magnitudes) - 1):
        for j in range(random_numbers_per_magnitude):
            test_random_numbers.append(random.randrange(magnitudes[i], \
                                                                magnitudes[i + 1]))
        shift += 10
    for j in range(random_numbers_per_magnitude):
        test_random_numbers.append(random.randrange(magnitudes[i + 1], \
                                                        magnitudes[i + 1] * 10))
    return test_random_numbers

test_numbers_ten_magnituded = \
                get_magnitudes_of_ten(minimal_magnitude, number_of_magnitudes)
test_random_numbers = \
    get_random_numbers_between_magnitudes(test_numbers_ten_magnituded, \
                                            random_numbers_per_magnitude)
import math

# Print summary of generated numbers.
print(f"""Generated numbers:\n    magnitudes <{test_numbers_ten_magnituded[0]}: 10**{int(math.log(test_numbers_ten_magnituded[-1], 10))}> total: {len(test_numbers_ten_magnituded)},
    random numbers per magnitude: {random_numbers_per_magnitude}, total: {len(test_random_numbers)}""")

# Define test functions.
def xor(a, b, assign=False):
    return a ^ b

def xor_assign(a, b):
    a ^= b
    return a

def logic_and(a, b):
    return a & b

def logic_and_assign(a, b):
    a &= b
    return a

def logic_or(a, b):
    return a | b

def logic_or_assign(a, b):
    a |= b
    return a

def lshift(a, shift):
    return a << shift

def lshift_assign(a, shift):
    a <<= b
    return a

def rshift(a, shift):
    return a >> shift

def rshift_assign(a, shift):
    a >>= shift
    return a

test_data_a = test_random_numbers + test_numbers_ten_magnituded

test_data_b = get_magnitudes_of_ten(0, 10)
test_data_b += get_random_numbers_between_magnitudes(test_data_b, random_numbers_per_magnitude)

for test_id in range(len(test_data_a)):
    a = test_data_a[test_id]
    for test_id_2 in range(len(test_data_b)):
        b = test_data_b[test_id_2]
        xor(a, b)
        #xor_assign(a, b)
        logic_and(a, b)
        #logic_and_assign(a, b)
        logic_or(a, b)
        # logic_or_assign(a, b)
        # lshift(a, b)
        # lshift_assign(a, b)    
        rshift(a, b)
        #rshift_assign(a, b)
