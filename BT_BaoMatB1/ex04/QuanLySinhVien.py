from SinhVien import SinhVien

class QuanLySinhVien:
    listSV = []

    def generateID(self):
        maxID = 1
        if self.soLuongSV() > 0:
            maxID = self.listSV[0]._id
            for sv in self.listSV:
                if maxID < sv._id:
                    maxID = sv._id
            maxID = maxID + 1
        return maxID

    def soLuongSV(self):
        return len(self.listSV)

    def nhapSV(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSV.append(sv)

    def updateSV(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID={} khong ton tai.".format(ID))

    def sortByID(self):
        self.listSV.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSV.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSV.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        searchResult = None
        if self.soLuongSV() > 0:
            for sv in self.listSV:
                if sv._id == ID:
                    searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if self.soLuongSV() > 0:
            for sv in self.listSV:
                if keyword.upper() in sv._name.upper():
                    listSV.append(sv)
        return listSV

    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if sv is not None:
            self.listSV.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"

    def showSV(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
                print("\n")

    def getListSV(self):
        return self.listSV