# Hàm kiểm tra số nhị phân có chia hết cho 5 không
def chiahetcho5(sonhiphan):
    try:
        # Loại bỏ khoảng trắng và chuyển số nhị phân sang số thập phân
        sothapphan = int(sonhiphan.strip(), 2)
        # Kiểm tra số thập phân có chia hết cho 5 không
        return sothapphan % 5 == 0
    except ValueError:
        return False  # Trả về False nếu không phải số nhị phân hợp lệ

# Nhập chuỗi số nhị phân từ người dùng
chuoisonhiphan = input("Nhập số nhị phân (phân tách bởi dấu phẩy nếu nhiều số): ")

# Tách chuỗi thành các số nhị phân và kiểm tra số chia hết cho 5
sonhiphan_list = chuoisonhiphan.split(",")
sochiahetcho5 = [so.strip() for so in sonhiphan_list if chiahetcho5(so)]

# In ra các số nhị phân chia hết cho 5
if len(sochiahetcho5) > 0:
    ketqua = ", ".join(sochiahetcho5)
    print("Các số nhị phân chia hết cho 5:", ketqua)
else:
    print("Không tìm thấy số nhị phân nào chia hết cho 5.")