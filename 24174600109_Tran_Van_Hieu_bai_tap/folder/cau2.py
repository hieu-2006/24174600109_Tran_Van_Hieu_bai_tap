import math
n = int(input("Nhap n: "))
cac_so_hoan_hao = []
for so in range(2, n):
    tong_cac_uoc = 1
    for i in range(2, int(math.sqrt(so)) + 1):
        if so % i == 0:
            tong_cac_uoc = tong_cac_uoc + i
            if i != so // i:
                tong_cac_uoc = tong_cac_uoc + so // i
    if tong_cac_uoc == so:
        cac_so_hoan_hao.append(so)

print("Cac so hoan hao nho hon", n, "la:", cac_so_hoan_hao)

# Đầu vào:
# Nhap n: 50
# Đầu ra:
# Cac so hoan hao nho hon 50 la: [6, 28]