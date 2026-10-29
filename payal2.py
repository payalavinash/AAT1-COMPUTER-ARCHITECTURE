def to_8bit(n):
    return format(n & 0xFF, '08b')

def ror(binary_str, n):
    n = n % 8
    return binary_str[-n:] + binary_str[:-n]

def rcr(binary_str, carry, n):
    for _ in range(n):
        new_carry = binary_str[-1]
        binary_str = carry + binary_str[:-1]
        carry = new_carry
    return binary_str, carry

print("--- Question 2a: Rotate Right Without Carry (ROR) ---")
original_a = "11010101"
n_a = 2
result_a = ror(original_a, n_a)

print(f"Original 8-bit binary: {original_a}")
print(f"Rotation process: Rotate right by {n_a} positions step by step")
print(f"Final 8-bit binary result: {result_a}\n")

print("--- Question 2b: Rotate Right With Carry (RCR) ---")
original_b = "11010101"
initial_carry = "0"
n_b = 2

print(f"Original 8-bit binary: {original_b}")
print(f"Initial Carry Flag: {initial_carry}")

final_b, final_carry = rcr(original_b, initial_carry, n_b)

print(f"Final 8-bit binary result: {final_b}")
print(f"Final Carry Flag: {final_carry}")