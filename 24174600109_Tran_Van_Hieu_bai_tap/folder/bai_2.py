import math
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ a của tâm I: "))
b = float(input("Nhập tọa độ b của tâm I: "))
R = float(input("Nhập bán kính R: "))
IM = math.sqrt((x - a) ** 2 + (y - b) ** 2)
print(f" Khoảng cách IM là: {IM}")
if IM <= R:
    print("True")
else:
    print("False")



# |Đầu vào:                          |Đầu ra:
# |Nhập tọa độ x của điểm M: 2       |Nhập bán kính R: 4
# |Nhập tọa độ y của điểm M: 4       |Khoảng cách IM là: 1.0
# |Nhập tọa độ a của tâm I: 2        |True
# |Nhập tọa độ b của tâm I: 3        |
# |Nhập bán kính R: 4                |
#
# |Nhập tọa độ x của điểm M: 2       |Nhập bán kính R: 4
# |Nhập tọa độ y của điểm M: 4       |Khoảng cách IM là: 2.23606797749979
# |Nhập tọa độ a của tâm I: 1        |False
# |Nhập tọa độ b của tâm I: 2        |
# |Nhập bán kính R: 22               |