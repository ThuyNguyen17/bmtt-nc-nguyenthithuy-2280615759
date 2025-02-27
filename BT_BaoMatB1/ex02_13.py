def tao_tuple_tu_list (lst):
    return tuple(lst)
input_list = input("Nhap danh sach cac so,cach nhau dau phay: ")
number_list = list(map(int, input_list.split(",")))

my_tuple = tao_tuple_tu_list(number_list)
print ("Tuple tu List la:", my_tuple)