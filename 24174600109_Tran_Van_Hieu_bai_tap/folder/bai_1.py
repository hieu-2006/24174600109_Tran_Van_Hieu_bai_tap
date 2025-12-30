nam = int(input("Nhập năm: "))
if nam % 4 == 0 and nam % 100 != 0:
    print("Đây là năm nhuận")
elif nam % 400 == 0:
    print("Đây là năm nhuận")
else:
    print("Đây không phải là năm nhuận")

# |Đầu vào:                  | Đầu ra:
# |Nhập năm: 2024            | Đây là năm nhuận
# |Nhập năm: 2021            | Đây không phải là năm nhuận