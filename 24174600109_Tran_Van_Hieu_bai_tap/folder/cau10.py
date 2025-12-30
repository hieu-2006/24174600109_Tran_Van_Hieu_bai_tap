n = int(input("Nhap so nguyen duong n: "))
thua_so = 2
ket_qua = []

while n > 1:
    while n % thua_so == 0:
        ket_qua.append(thua_so)
        n = n // thua_so
    thua_so = thua_so + 1

print("Dang phan tich thua so nguyen to:", " * ".join(map(str, ket_qua)))


# Đầu vào:
# Nhap so nguyen duong n: 5
# Đầu ra:
# Dang phan tich thua so nguyen to: 5