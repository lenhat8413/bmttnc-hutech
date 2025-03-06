def tao_tuple_tu_list(lst):
    return tuple(lst)

#nhap danh sach tu nguoi dung va xu li chuoi

list_str = input("Nhap danh sach cac phan tu (cach phan tu bang dau phay): ")
numbers =list(map(int, list_str.split(',')))

my_tuple = tao_tuple_tu_list(numbers)

print("List: ",numbers)
print("Tuple tu list:", my_tuple)
