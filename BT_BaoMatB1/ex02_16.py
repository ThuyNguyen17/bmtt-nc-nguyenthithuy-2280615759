def xoa_ptu (dic, key):
    if key in dic:
        del dic[key]
        return True
    else:
        return False

my_dic = {'a':1, 'b':2,'c': 3}
key_to_del = 'b'
result = xoa_ptu(my_dic,key_to_del)
if result:
    print("Phan tu da duoc xoa tu dic: ",my_dic)
else:
    print("Khogn tim thay phan tu can xoa trong dic")