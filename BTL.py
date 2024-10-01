import json

def main_menu():
    doc_du_lieu()  # Đọc dữ liệu sản phẩm khi khởi động
    doc_du_lieu_khach_hang()  # Đọc dữ liệu khách hàng khi khởi động
    while True:
        print(f"---------------------------------------")
        print("Menu")
        print("1. Thêm sản phẩm mới")
        print("2. Sửa thông tin sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Xem danh sách sản phẩm")
        print("5. Tìm kiếm sản phẩm")
        print("6. Lọc sản phẩm")
        print("7. Xem chi tiết sản phẩm")
        print("8. Thêm khách hàng mới")
        print("9. Sửa thông tin khách hàng")
        print("10. Xem danh sách khách hàng")
        
        print("0. Thoát")
        print(f"---------------------------------------")
        try:
            choice = int(input("Nhập lựa chọn của bạn: "))
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số.")
            continue

        if choice == 1:
            them_san_pham()
        elif choice == 2:
            sua_san_pham()
        elif choice == 3:
            xoa_san_pham()
        elif choice == 4:
            xem_danh_sach_san_pham()
        elif choice == 5:
            tim_kiem_san_pham()
        elif choice == 6:
            loc_san_pham()
        elif choice == 7:
            xem_chi_tiet_san_pham()
        elif choice == 8:
            them_khach_hang_moi()
        elif choice == 9:
            sua_thong_tin_khach_hang()
        elif choice == 10:
            xem_danh_sach_khach_hang()
        
        elif choice == 0:
            print("Chương trình kết thúc.")
            luu_du_lieu()  # Lưu dữ liệu sản phẩm trước khi thoát
            luu_du_lieu_khach_hang()  # Lưu dữ liệu khách hàng trước khi thoát
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

products = []  # Danh sách sản phẩm

def them_san_pham():
    ten = input("Nhập tên sản phẩm: ")
    try:
        gia = float(input("Nhập giá bán: "))
        soluong = int(input("Nhập số lượng: "))
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")
        return
    san_pham = {"ten": ten, "gia": gia, "soluong": soluong}
    products.append(san_pham)
    print("Sản phẩm đã được thêm.")
    luu_du_lieu()  # Lưu dữ liệu sau khi thêm

def sua_san_pham():
    ten_can_sua = input("Nhập tên sản phẩm cần sửa: ")
    for san_pham in products:
        if san_pham["ten"] == ten_can_sua:
            try:
                san_pham["gia"] = float(input("Nhập giá mới: "))
                san_pham["soluong"] = int(input("Nhập số lượng mới: "))
            except ValueError:
                print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")
                return
            print("Sản phẩm đã được sửa.")
            return
    print("Không tìm thấy sản phẩm.")

def xoa_san_pham():
    ten_can_xoa = input("Nhập tên sản phẩm cần xóa: ")
    for i, san_pham in enumerate(products):
        if san_pham["ten"] == ten_can_xoa:
            del products[i]
            print("Sản phẩm đã được xóa.")
            luu_du_lieu()  # Lưu dữ liệu sau khi xóa
            return
    print("Không tìm thấy sản phẩm.")

def xem_danh_sach_san_pham():
    if not products:
        print("Danh sách sản phẩm đang trống.")
    else:
        print("Danh sách sản phẩm:")
        for i, san_pham in enumerate(products):
            print(f"{i+1}. {san_pham['ten']} - Giá: {san_pham['gia']} - Số lượng: {san_pham['soluong']}")

def luu_du_lieu():
    with open('info.json', 'w') as f:
        json.dump(products, f)

def doc_du_lieu():
    global products
    try:
        with open('info.json', 'r') as f:
            products = json.load(f)
    except FileNotFoundError:
        pass


# Hàm tìm kiếm sản phẩm theo tên
def tim_kiem_san_pham():
    ten_tim_kiem = input("Nhập tên sản phẩm cần tìm: ").lower()
    ket_qua = [sp for sp in products if ten_tim_kiem in sp['ten'].lower()]
    
    if not ket_qua:
        print("Không tìm thấy sản phẩm nào.")
    else:
        print(f"Đã tìm thấy {len(ket_qua)} sản phẩm:")
        for i, sp in enumerate(ket_qua):
            print(f"{i+1}. {sp['ten']} - Giá: {sp['gia']} - Số lượng: {sp['soluong']}")

# Hàm lọc sản phẩm theo khoảng giá
def loc_san_pham():
    try:
        gia_min = float(input("Nhập giá thấp nhất: "))
        gia_max = float(input("Nhập giá cao nhất: "))
        if gia_min > gia_max:
            print("Giá thấp nhất không thể lớn hơn giá cao nhất.")
            return
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập số.")
        return

    ket_qua = [sp for sp in products if gia_min <= sp['gia'] <= gia_max]
    
    if not ket_qua:
        print("Không tìm thấy sản phẩm nào trong khoảng giá này.")
    else:
        print(f"Đã tìm thấy {len(ket_qua)} sản phẩm:")
        for i, sp in enumerate(ket_qua):
            print(f"{i+1}. {sp['ten']} - Giá: {sp['gia']} - Số lượng: {sp['soluong']}")

# Hàm xem chi tiết sản phẩm theo tên
def xem_chi_tiet_san_pham():
    ten_tim_kiem = input("Nhập tên sản phẩm để xem chi tiết: ").lower()
    for sp in products:
        if sp['ten'].lower() == ten_tim_kiem:
            print(f"Tên sản phẩm: {sp['ten']}")
            print(f"Giá: {sp['gia']}")
            print(f"Số lượng: {sp['soluong']}")
            return
    print("Không tìm thấy sản phẩm.")

# Dữ liệu khách hàng
customers = []  # Danh sách khách hàng

# Hàm thêm khách hàng mới
def them_khach_hang_moi():
    ten = input("Nhập tên khách hàng: ")
    so_dien_thoai = input("Nhập số điện thoại: ")
    dia_chi = input("Nhập địa chỉ: ")
    khach_hang = {"ten": ten, "so_dien_thoai": so_dien_thoai, "dia_chi": dia_chi}
    customers.append(khach_hang)
    print("Khách hàng đã được thêm.")
    luu_du_lieu_khach_hang()  # Lưu dữ liệu khách hàng

# Hàm sửa thông tin khách hàng
def sua_thong_tin_khach_hang():
    ten_can_sua = input("Nhập tên khách hàng cần sửa: ")
    for kh in customers:
        if kh["ten"] == ten_can_sua:
            kh["so_dien_thoai"] = input("Nhập số điện thoại mới: ")
            kh["dia_chi"] = input("Nhập địa chỉ mới: ")
            print("Thông tin khách hàng đã được sửa.")
            luu_du_lieu_khach_hang()  # Lưu dữ liệu khách hàng
            return
    print("Không tìm thấy khách hàng.")

# Hàm xem danh sách khách hàng
def xem_danh_sach_khach_hang():
    if not customers:
        print("Danh sách khách hàng đang trống.")
    else:
        print("Danh sách khách hàng:")
        for i, kh in enumerate(customers):
            print(f"{i+1}. {kh['ten']} - SĐT: {kh['so_dien_thoai']} - Địa chỉ: {kh['dia_chi']}")

# Hàm lưu dữ liệu khách hàng vào tệp
def luu_du_lieu_khach_hang():
    with open('customers.json', 'w') as f:
        json.dump(customers, f)

# Hàm đọc dữ liệu khách hàng từ tệp
def doc_du_lieu_khach_hang():
    global customers
    try:
        with open('customers.json', 'r') as f:
            customers = json.load(f)
    except FileNotFoundError:
        pass


main_menu()
