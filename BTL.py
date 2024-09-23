import sqlite3

def menu():
    while True:
        print("\n--- Menu Quan Ly Cong Ty Dien Thoai ---")
        print("1. Them khach hang")
        print("2. Them goi cuoc")
        print("3. Tao hop dong")
        print("4. Tao hoa don")
        print("5. Cap nhat thong tin khach hang")
        print("6. Cap nhat thong tin goi cuoc")
        print("7. Cap nhat hop dong")
        print("8. Cap nhat hoa don")
        print("9. Xoa khach hang")
        print("10. Xoa goi cuoc")
        print("11. Xoa hop dong")
        print("12. Xoa hoa don")
        print("13. Tim kiem khach hang theo ten")
        print("14. Tim kiem hop dong theo ID khach hang")
        print("15. Tim kiem hoa don theo ID hop dong")
        print("16. Xem danh sach khach hang")
        print("17. Xem danh sach goi cuoc")
        print("18. Xem danh sach hop dong")
        print("19. Xem danh sach hoa don")
        print("20. Thoat")

        choice = int(input("Chon chuc nang (1-20): "))

        if choice == 1:
            add_customer()
        elif choice == 2:
            add_plan()
        elif choice == 3:
            add_contract()
        elif choice == 4:
            add_invoice()
        elif choice == 5:
            update_customer()
        elif choice == 6:
            update_plan()
        elif choice == 7:
            update_contract()
        elif choice == 8:
            update_invoice()
        elif choice == 9:
            delete_customer()
        elif choice == 10:
            delete_plan()
        elif choice == 11:
            delete_contract()
        elif choice == 12:
            delete_invoice()
        elif choice == 13:
            search_customer_by_name()
        elif choice == 14:
            search_contract_by_customer_id()
        elif choice == 15:
            search_invoice_by_contract_id()
        elif choice == 16:
            view_customers()
        elif choice == 17:
            view_plans()
        elif choice == 18:
            view_contracts()
        elif choice == 19:
            view_invoices()
        elif choice == 20:
            print("Thoat chuong trinh!")
            break
        else:
            print("Lua chon khong hop le, vui long thu lai.")
def add_customer():
    """Thêm một khách hàng mới vào hệ thống."""

    # Nhập thông tin khách hàng từ người dùng
    ma_khach_hang = tao_ma_khach_hang_moi()
    ten_khach_hang = input("Nhập tên khách hàng: ")
    dia_chi = input("Nhập địa chỉ: ")
    so_dien_thoai = input("Nhập số điện thoại: ")

    # Kiểm tra tính hợp lệ của dữ liệu nhập vào (có thể thêm các kiểm tra khác)
    while not ten_khach_hang:
        print("Tên khách hàng không được để trống.")
        ten_khach_hang = input("Nhập lại tên khách hàng: ")
    # Thêm các kiểm tra tương tự cho các trường khác

    # Tạo đối tượng khách hàng mới và thêm vào cơ sở dữ liệu
    khach_hang_moi = KhachHang(ma_khach_hang, ten_khach_hang, dia_chi, so_dien_thoai)
    them_khach_hang_vao_co_so_du_lieu(khach_hang_moi)

    print("Khách hàng đã được thêm thành công!")
def add_plan():

def add_contract():

def add_invoice():

def update_customer():

def update_plan():
    
def update_contract():

def update_invoice():

def delete_customer():

def delete_plan():

def delete_contract():

def delete_invoice():

def search_customer_by_name():

def search_contract_by_customer_id():

def search_invoice_by_contract_id():

def view_customers():

def view_plans():

def view_contracts():

def view_invoices():