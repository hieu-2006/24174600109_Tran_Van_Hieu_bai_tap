thang = int(input("Nhập vào tháng (1-12): "))
nam = int(input("Nhập vào năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    nam_nhuan = True
else:
    nam_nhuan = False

if thang == 2:
    if nam_nhuan:
        so_ngay = 29
    else:
        so_ngay = 28
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
else:
    so_ngay = 31

print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")


# Đầu vào:
# |Nhập vào tháng (1-12): 2            |Nhập vào tháng (1-12): 2
# |Nhập vào năm: 2024                  |Nhập vào năm: 2021

# Đầu ra:
# |Tháng 2 năm 2024 có 29 ngày.        |Tháng 2 năm 2021 có 28 ngày.