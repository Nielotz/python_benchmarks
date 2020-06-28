""" 
Test description: 
    fastest way to convert int to minecraft varint
    (like normal varint but negative values are always 5 bytes)

"""

n_of_tests = 100

import gc
gc.disable()

import time

import random, struct


MAX_INT = 0x7FFFFFFF
MIN_INT = -0x80000000
MAX_UINT = 0x100000000
def convert_to_varint(value: int) -> bytes:
    if value > MAX_INT:
        raise ValueError(f"value: '{value}' is too big for VarInt")
    if value < MIN_INT:
        raise ValueError(f"value: '{value}' is too small for VarInt")

    if value == 0:
        return bytes(b'\x00')
    if value > 0:
        varint = bytearray()

        while value != 0:
            byte = value & 0x7F
            value >>= 7
            varint.extend(struct.pack('B', byte | (0x80 if value != 0 else 0)))
        return bytes(varint)

    # When value is negative
    # Negative varint always has 5 bytes
    varint = bytearray(b'\x80\x80\x80\x80\x00')
    value_in_bytes = value.to_bytes(4, byteorder="little", signed=True)
    varint[0] |= value_in_bytes[0]
    varint[1] |= (value_in_bytes[1] << 1) & 0xFF | value_in_bytes[0] >> 7
    varint[2] |= (value_in_bytes[2] << 2) & 0xFF | value_in_bytes[1] >> 6
    varint[3] |= (value_in_bytes[3] << 3) & 0xFF | value_in_bytes[2] >> 5
    varint[4] |= value_in_bytes[3] >> 4

    return bytes(varint)

def convert_to_varint2(value: int) -> bytes:
    if value > MAX_INT:
        raise ValueError(f"value: '{value}' is too big for VarInt")
    if value < MIN_INT:
        raise ValueError(f"value: '{value}' is too small for VarInt")

    if value == 0:
        return bytes(b'\x00')

    if value < 0:
        value = ~value + 1
    print(value)
    varint = bytearray()
    
    while value != 0:
        byte = value & 0x7F
        value >>= 7
        varint.extend(struct.pack('B', byte | (0x80 if value != 0 else 0)))
    return bytes(varint)


print(convert_to_varint(-1))
print(convert_to_varint2(-1))
print()
print(convert_to_varint(-2))
print(convert_to_varint2(-2))
print()
print(convert_to_varint(2))
print(convert_to_varint2(2))

"""
values = [random.randint(MIN_INT, -1) for i in range(10000)]
print("Generated values.")

time_passed = 0
for i in range(100):
    start = time.perf_counter()
    for val in values:
        convert_to_varint(val)
    time_passed += time.perf_counter() - start

print(f"v1: {time_passed / 100}")

time_passed = 0
for i in range(100):
    start = time.perf_counter()
    for val in values:
        convert_to_varint(val)
    time_passed += time.perf_counter() - start

print(f"v2: {time_passed / 100}")
"""