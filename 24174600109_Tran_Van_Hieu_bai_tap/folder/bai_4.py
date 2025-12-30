a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
# Giả sử số lớn nhất là a
SLN = a
if b >= a and b >= c:
    SLN = b
elif c >= a and c >= b:
    SLN = c
else:
    SLN = a
print(f"Vậy số lớn nhất là: {SLN}")

# Đầu vào:
# Nhập số thứ nhất: 6
# Nhập số thứ hai: 8
# Nhập số thứ ba: 8
# Đầu ra:
# Vậy số lớn nhất là: 8.0