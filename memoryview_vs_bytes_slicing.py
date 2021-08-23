"""
bytes: 13.6776729 s
memoryview: 18.605768100000002 s
"""
import timeit

bytes_len = 100

bytes_dummy = timeit.Timer("""while data:
    _, data = convert_first_byte_to_int_and_return_leftover_bytes(data)""",
                           setup=f"""def convert_first_byte_to_int_and_return_leftover_bytes(data_: bytes):
    return int(data_[0]), data_[1:]
data = b'C' * {bytes_len}""")

memoryview_dummy = timeit.Timer("""while data:
    _, data = convert_first_byte_to_int_and_return_leftover_memoryview(data)""",
                                setup=f"""def convert_first_byte_to_int_and_return_leftover_memoryview(data_):
    return int(data_[0]), data_[1:]
data = memoryview(b'C' * {bytes_len})""")

overwrite_bytes = timeit.Timer("""data_doer = DataDoerOverwrite(data) 
while data_doer.data:
    _ = data_doer.get_int()""", setup=f"""class DataDoerOverwrite:
    def __init__(self, data):
        self.data = data

    def get_int(self):
        dat = self.data[0]
        self.data = self.data[1:]
        return dat
data = b'C' * {bytes_len}""")

overwrite_memoryview = timeit.Timer("""data_doer = DataDoerOverwrite(data) 
while data_doer.data:
    _ = data_doer.get_int()""", setup=f"""class DataDoerOverwrite:
    def __init__(self, data):
        self.data = data

    def get_int(self):
        dat = self.data[0]
        self.data = self.data[1:]
        return dat
data = memoryview(b'C' * {bytes_len})""")

indexes_bytes = timeit.Timer("""data_doer = DataDoerIndexes(data) 
while data_doer.data_len != data_doer.start:
    _ = data_doer.get_int()""",
                             setup=f"""class DataDoerIndexes:
    def __init__(self, data):
        self.data = data
        self.data_len = len(data)
        self.start = 0

    def get_int(self):
        dat = self.data[self.start]
        self.start += 1
        return dat
data = b'C' * {bytes_len}""")

indexes_memoryview = timeit.Timer("""data_doer = DataDoerIndexes(data) 
while data_doer.data_len != data_doer.start:
    _ = data_doer.get_int()""",
                                  setup=f"""class DataDoerIndexes:
    def __init__(self, data):
        self.data = data
        self.data_len = len(data)
        self.start = 0

    def get_int(self):
        dat = self.data[self.start]
        self.start += 1
        return dat
data = memoryview(b'C' * {bytes_len})""")

results = {
    "bytes dummy": bytes_dummy.timeit(100000),
    "memoryview dummy": memoryview_dummy.timeit(100000),

    "bytes class with overwrite": overwrite_bytes.timeit(100000),
    "memoryview class with overwrite": overwrite_memoryview.timeit(100000),

    "bytes class with indexes": indexes_bytes.timeit(100000),
    "memoryview class with indexes": indexes_memoryview.timeit(100000),
}
for item in sorted([(value, key) for value, key in results.items()], reverse=True):
    print(item[0].center(30), item[1])
