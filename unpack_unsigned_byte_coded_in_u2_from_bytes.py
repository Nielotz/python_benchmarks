import random
import timeit


N_OF_NUMBERS = 10

original = [None] * N_OF_NUMBERS
u2_number = [None] * N_OF_NUMBERS
decoded_numbers = [None] * N_OF_NUMBERS
decoded_numbers2 = [None] * N_OF_NUMBERS

for i in range(N_OF_NUMBERS):
    original[i] = random.randint(0, 255)
    u2_number[i] = original[i].to_bytes(1, byteorder="big", signed=False)

u2_number = tuple(u2_number)

print(f"Generated {N_OF_NUMBERS} numbers.")


""" End of init """

#  Faster 
def unsigned_byte_from_bytes():
    for idx in range(N_OF_NUMBERS):
        decoded_numbers[idx] = int.from_bytes(u2_number[idx], byteorder="big", signed=False)

def unsigned_byte_hex_int():
    for idx in range(N_OF_NUMBERS):
        decoded_numbers2[idx] = int(u2_number[idx].hex(), 16)


t1 = timeit.Timer(unsigned_byte_from_bytes)
t2 = timeit.Timer(unsigned_byte_hex_int)

print(t1.timeit())   #  2.6375862000000003
print(t2.timeit())   #  3.2448588000000003



for idx in range(N_OF_NUMBERS):
    if not decoded_numbers[idx] == decoded_numbers2[idx]:
        raise RuntimeError(f"{original[idx]} {decoded_numbers[idx]} {decoded_numbers2[idx]}")

