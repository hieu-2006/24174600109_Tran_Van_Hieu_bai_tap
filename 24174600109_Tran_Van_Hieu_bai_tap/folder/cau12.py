ma_container = input("Nhap ma container (10 ky tu): ").upper()
gia_tri = {'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18,
           'I': 19, 'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27,
           'Q': 28, 'R': 29, 'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36,
           'Y': 37, 'Z': 38}
trong_so = 0

for i in range(10):
    ky_tu = ma_container[i]
    if ky_tu.isdigit():
        trong_so = trong_so + int(ky_tu) * (2 ** i)
    else:
        trong_so = trong_so + gia_tri[ky_tu] * (2 ** i)

so_kiem_tra = trong_so % 11
print("So kiem tra cua ma container", ma_container, "la:", so_kiem_tra)


# Đầu vào:
# Nhap ma container (10 ky tu): HIEU080206
# Đầu ra:
# So kiem tra cua ma container HIEU080206 la: 7


# H = 18,I = 20,E = 15,U = 32
# 18*2**0 + 20*2**1 + 15*2**2 + 32*2**3 + 0*2**4 + 8*2**5 + 0*2**6 + 2*2**7 + 0*2**8 + 6*2**9 = 3956
# 3956 / 11 = 359 dư 7