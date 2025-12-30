ky_tu = input("Nhập một ký tự bất kỳ: ")
if ky_tu.isalpha() and ky_tu != "":
    ky_tu = ky_tu.lower()
    if ky_tu in 'euoai':
        print(f"Ký tự '{ky_tu}' là nguyên âm.")
    else:
        print(f"Ký tự '{ky_tu}' là phụ âm.")
else:
    print("Ký tự '{ky_tu}' không phải là nguyên âm hay phụ âm")

# Đầu vào:
# Nhập một ký tự bất kỳ: K     |Nhập một ký tự bất kỳ: o
# Đầu ra:
# Ký tự 'k' là phụ âm.         |Ký tự 'o' là nguyên âm.