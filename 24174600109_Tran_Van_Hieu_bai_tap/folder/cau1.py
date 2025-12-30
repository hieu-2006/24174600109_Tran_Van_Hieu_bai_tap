import math
n = int(input("Nhap n: "))
kq = 1
for i in range(1, n+1):
    shang = 1
    for j in range(1, i+1):
        shang = shang * (2*j) / (2*j + 1)
    kq = kq + shang

print("Kết quả:", round(kq, 3))

# Đầu vào:
# Nhap n: 3
# Đầu ra:
# Kết quả: 2.657