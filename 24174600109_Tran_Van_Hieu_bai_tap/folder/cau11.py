n = int(input("Nhập số hàng của tam giác: "))
print("\nTam giác rỗng (a): ")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * (n - i) + "*" * (2 * i - 1))
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")

print("\nTam giác rỗng (b): ")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * (n - i) + "* " * i)
    else:
        print(" " * (n - i) + "* " + "  " * (i - 2) + "* ")


print("Tam giác lớn không rỗng (c): ")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)


# Đầu vào:
# Nhập số hàng của tam giác: 5
# Đầu ra:
# Tam giác rỗng (a):
#     *
#    * *
#   *   *
#  *     *
# *********

# Tam giác rỗng (b):
#     *
#    * *
#   *   *
#  *     *
# * * * * *
# Tam giác lớn không rỗng (c):
#     *
#    * *
#   * * *
#  * * * *
# * * * * *