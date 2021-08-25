"""
Python 3.9.5
Windows 10.0.19042
AMD Ryzen 5 3600
Results (best times for x repeats):
    60MB, 12 repeats:
        bytes_class_with_indexes       15.29s
        memoryview_class_with_indexes  15.95s
        memoryview_func                16.65s
    6MB, 35 repeats:
        bytes_class_with_indexes       1.511s
        memoryview_class_with_indexes  1.627s
        memoryview_func                1.640s
        bytes_func                     FOKs
    600KB, 35 repeats:
        bytes_class_with_indexes       0.1483s
        memoryview_class_with_indexes  0.1534s
        memoryview_func                0.1603s
        bytes_func                     5.5000s
    400KB, 50 repeats:
        bytes_class_with_indexes       0.1007s
        memoryview_class_with_indexes  0.1059s
        memoryview_func                0.1132s
        bytes_func                     1.7689s
    60KB, 100 repeats:
        bytes_class_with_indexes      0.01454s
        memoryview_class_with_indexes 0.01528s
        memoryview_func               0.01620s
        bytes_func                    0.05163s
    6KB, 1000 repeats:
        bytes_class_with_indexes      0.001512s
        memoryview_class_with_indexes 0.001573s
        memoryview_func               0.001640s
        bytes_func                    0.001977s
"""

import copy
from time import perf_counter_ns as get_time_ns

bytes_len = 2500000
N_OF_TESTS = 100

base_data = b'C' * bytes_len


def convert_first_byte_of_data_to_int_and_return_leftover(data_: bytes):
    return int(data_[0]), data_[1:]


def convert_first_byte_of_memoryview_to_int_and_return_leftover(data_: memoryview):
    return int(data_[0]), data_[1:]


class DataDoerIndexes:
    def __init__(self, data_):
        self.data = data_
        self.start = 0

    def get_int(self):
        number = int(self.data[self.start])
        self.start += 1
        return number


times: {str: [], } = {
    "bytes_func": [],
    "memoryview_func": [],
    "bytes_class_with_indexes": [],
    "memoryview_class_with_indexes": [],
}

for i in range(N_OF_TESTS):
    print(f"Iteration: {i} / {N_OF_TESTS}")

    data = copy.deepcopy(base_data)
    start = get_time_ns()  # # #
    for _ in range(bytes_len):
        _, data = convert_first_byte_of_data_to_int_and_return_leftover(data)
    times["bytes_func"].append(get_time_ns() - start)  # # #

    memoryview_of_data = memoryview(base_data)
    start = get_time_ns()  # # #
    for _ in range(bytes_len):
        _, memoryview_of_data = convert_first_byte_of_memoryview_to_int_and_return_leftover(memoryview_of_data)
    times["memoryview_func"].append(get_time_ns() - start)  # # #

    data = copy.deepcopy(base_data)
    start = get_time_ns()  # # #
    data_doer = DataDoerIndexes(data)
    for _ in range(bytes_len):
        _ = data_doer.get_int()
    times["bytes_class_with_indexes"].append(get_time_ns() - start)  # # #

    memoryview_of_data = memoryview(base_data)
    start = get_time_ns()  # # #
    data_doer = DataDoerIndexes(memoryview_of_data)
    for _ in range(bytes_len):
        _ = data_doer.get_int()
    times["memoryview_class_with_indexes"].append(get_time_ns() - start)  # # #

    for item in sorted([(min(value), key) for key, value in times.items()], reverse=False):
        print(f"    {item[1].ljust(30)} {item[0] * 0.000000001}")
