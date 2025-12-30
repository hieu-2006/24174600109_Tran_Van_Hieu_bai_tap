luong = float(input("Nhập lương của nhân viên (đồng): "))
thue = 0
luong_rong = 0
if luong >= 15000000:
    thue = luong * 0.3  
elif luong >= 7000000 and luong < 15000000:
    thue = luong * 0.2
else:
    thue = luong * 0.1
luong_rong = luong - thue
print(f"Lương trước thuế: {luong} đồng")
print(f"Thuế thu nhập: {thue} đồng")
print(f"Lương ròng (lương thực sự nhận): {luong_rong} đồng")

# Đầu vào:
# Nhập lương của nhân viên (đồng): 10000000

# Đầu ra:
# Lương trước thuế: 10000000.0 đồng
# Thuế thu nhập: 2000000.0 đồng
# Lương ròng (lương thực sự nhận): 8000000.0 đồng