so_gio_lam = float(input("Nhap so gio lam bat dau:"))
luong_gio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
gio_tieu_chuan = 44
gio_vuot_tieu_chuan = max(0,so_gio_lam - gio_tieu_chuan)
thuc_nhan= gio_tieu_chuan * luong_gio + gio_vuot_tieu_chuan * luong_gio * 1.5
print(f"So tien thuc linh cua nhan vien la: {thuc_nhan}")