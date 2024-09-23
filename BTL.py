def main_menu():
    while True:
        print("Menu quản lý cửa hàng điện thoại")
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

        choice = int(input("Nhập lựa chọn của bạn: "))

        if choice == :1
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
            sua_thong_tin()
        elif choice == "0":
            print("Chương trình kết thúc.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
