n = int(input("Nhap so nguyen duong n: "))
while n <= 0:
    n = int(input("Vui long nhap lai n la so nguyen duong: "))

# a) S4 = 1^2 + 2^2 + 3^2 + ... + n^2
S4 = 0
for i in range(1, n + 1):
    S4 = S4 + i ** 2
print("S4 =", S4)

# b) S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3
S5 = 0
for i in range(n + 1):
    S5 = S5 + (2 * i + 1) ** 3
print("S5 =", S5)

# c) S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4
S6 = 0
for i in range(1, n + 1):
    S6 = S6 + (2 * i) ** 4
print("S6 =", S6)


# Đầu vào:
# Nhap so nguyen duong n: 5
# Đầu ra:
# S4 = 55
# S5 = 2556
# S6 = 15664