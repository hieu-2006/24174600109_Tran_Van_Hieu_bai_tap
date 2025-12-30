so_hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
so_hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
so_hang_tram = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]

so = int(input("Nhập vào số nguyên có 3 chữ số: "))

tram = so // 100
chuc = (so % 100) // 10
don_vi = so % 10

cach_doc = so_hang_tram[tram]

if chuc == 0 and don_vi != 0:
    cach_doc += " lẻ " + so_hang_don_vi[don_vi]
elif chuc != 0:
    cach_doc += " " + so_hang_chuc[chuc]
    if don_vi != 0:
        cach_doc += " " + so_hang_don_vi[don_vi]
        
print(f"Cách đọc: {cach_doc}")


# Đầu vào:
# Nhập vào số nguyên có 3 chữ số: 345

# Đầu ra:
# Cách đọc: ba trăm bốn mươi năm