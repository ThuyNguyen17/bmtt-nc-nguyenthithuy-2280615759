from QuanLySinhVien import QuanLySinhVien

def menu():
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("***********************MENU************************")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên")
    print("3. Xóa sinh viên bởi ID")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo tên chuyên ngành")
    print("7. Hiển thị danh sách sinh viên")
    print("0. Thoát")
    print("***************************************************")

def main():
    qlsv = QuanLySinhVien()
    while True:
        menu()
        choice = int(input("Chọn chức năng: "))
        if choice == 1:
            print("\n1.Thêm sinh viên")
            qlsv.nhapSV()
            print("Thêm sinh viên thành công!")
        elif choice == 2:
            if(qlsv.soLuongSV() > 0):
                print("2. Cập nhật thông tin sinh viên")
                id = int(input("Nhập ID sinh viên cần cập nhật: "))
                qlsv.updateSV(id)
            else:
                print("\n Danh sach sinh vien trong!")
        elif choice == 3:
            if(qlsv.soLuongSV() > 0):
                print("3. Xóa sinh viên bởi ID")
                id = int(input("Nhập ID sinh viên cần xóa: "))
                if qlsv.deleteByID(id):
                    print("\nSinh vien co id = ",ID,"da bi xoa.")
                else:
                    print("\nSinh vien co id = ",ID,"khong ton tai.")
            else:
                print("\n Danh sach sinh vien trong!")
        elif choice == 4:
            if(qlsv.soLuongSV() > 0):
                print("4. Tìm kiếm sinh viên theo tên")
                name = input("Nhập tên sinh viên cần tìm: ")
                result = qlsv.findByName(name)
                qlsv.showSV(result)
            else:
                print("\n Danh sach sinh vien trong!")
        elif choice == 5:
            if(qlsv.soLuongSV() > 0):
                print("5. Sắp xếp sinh viên theo điểm trung bình")
                qlsv.sortByDiemTB()
                qlsv.showSV(qlsv.getListSV())
            else:
                print("\n Danh sach sinh vien trong!")
        elif choice == 6:
            if(qlsv.soLuongSV() > 0):
                print("6. Sắp xếp sinh viên theo tên chuyên ngành")
                qlsv.sortByName()
                qlsv.showSV(qlsv.getListSV())
            else:
                print("\n Danh sach sinh vien trong!")
        elif choice == 7:
            if(qlsv.soLuongSV() > 0):
                print("7. Hiển thị danh sách sinh viên")
                qlsv.showSV(qlsv.getListSV())
            else:
                print("\n Danh sach sinh vien trong!")
        elif choice == 0:
            print("Ban da chon thoat chuong trinh!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()