
def to_8bit(n):
    if n < 0:
        n = 256 + n
    return format(n, '08b')

print("--- Expression a): +48 + (+23) ---")
num1_a = 48
num2_a = 23

print(f"Operand +48 in 8-bit binary: {to_8bit(num1_a)}")
print(f"Operand +23 in 8-bit binary: {to_8bit(num2_a)}")

result_dec_a = num1_a + num2_a
result_bin_a = format(result_dec_a & 0xFF, '08b')

print(f"Final Result in Binary: {result_bin_a}")
print(f"Final Result in Decimal: {result_dec_a}")

if result_dec_a > 127 or result_dec_a < -128:
    print("Overflow: Yes \n")
else:
    print("Overflow: No \n")

print("--- Expression b): (-46) - (-29) ---")
num1_b = -46
num2_b = -29

print(f"Operand -46 in 8-bit binary: {to_8bit(num1_b)}")
print(f"Operand -29 in 8-bit binary: {to_8bit(num2_b)}")

result_dec_b = num1_b - num2_b
result_bin_b = to_8bit(result_dec_b)

print(f"Final Result in Binary: {result_bin_b}")
print(f"Final Result in Decimal: {result_dec_b}")

if result_dec_b > 127 or result_dec_b < -128:
    print("Overflow: Yes")
else:
    print("Overflow: No ")


    