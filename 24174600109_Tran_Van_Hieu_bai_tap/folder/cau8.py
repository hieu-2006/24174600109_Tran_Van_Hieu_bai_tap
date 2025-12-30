n = int(input("Nhap so nguyen duong n: "))
while n <= 0:
    n = int(input("Vui long nhap lai n la so nguyen duong: "))

# a) S1 = 1 + 2 + 3 + ... + n = n(n+1)/2
S1 = n * (n + 1) // 2
print("S1 =", S1)

# b) S2 = 1 + 3 + 5 + ... + (2n+1) = (n+1)^2
S2 = (n + 1) ** 2
print("S2 =", S2)

# c) S3 = 2 + 4 + 6 + ... + 2n = n(n+1)
S3 = n * (n + 1)
print("S3 =", S3)


# Đầu vào:
# Nhap so nguyen duong n: 5
# Đầu ra:
# S1 = 15
# S2 = 36
# S3 = 30
