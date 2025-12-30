import math
n = int(input("Nhap n: "))
cac_so_nguyen_to = []
for so in range(2, n + 1):
    la_so_nguyen_to = True
    for i in range(2, int(math.sqrt(so)) + 1):
        if so % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        cac_so_nguyen_to.append(so)

print("Cac so nguyen to nho hon hoac bang", n, "la:", cac_so_nguyen_to)

# Đầu vào:
# Nhap n: 100
# Đầu ra:
# Cac so nguyen to nho hon hoac bang 100 la: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]




