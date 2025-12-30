import math
n = int(input("Nhap n: "))
so_nguyen_to = True
if n < 2:
    so_nguyen_to = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            so_nguyen_to = False
            break

if so_nguyen_to:
    print(n, "la so nguyen to")
else:
    print(n, "khong phai la so nguyen to")
    khoang_cach = 0
    while True:
        so_cong = n + khoang_cach
        so_nguyen_to_cong = True
        if so_cong >= 2:
            for i in range(2, int(math.sqrt(so_cong)) + 1):
                if so_cong % i == 0:
                    so_nguyen_to_cong = False
                    break
        else:
            so_nguyen_to_cong = False

        so_tru = n - khoang_cach
        so_nguyen_to_tru = True
        if so_tru >= 2:
            for i in range(2, int(math.sqrt(so_tru)) + 1):
                if so_tru % i == 0:
                    so_nguyen_to_tru = False
                    break
        else:
            so_nguyen_to_tru = False

        if so_nguyen_to_cong:
            print("So nguyen to gan nhat la:", so_cong)
            break
        elif so_nguyen_to_tru and so_tru > 1:
            print("So nguyen to gan nhat la:", so_tru)
            break
        
        khoang_cach = khoang_cach + 1


# Đầu vào:
# Nhap n: 9
# Đầu ra:
# 9 khong phai la so nguyen to
# So nguyen to gan nhat la: 11