def daonguoclist(lst):
    return lst[::-1]
#nhap danh sach tu nguoi dung va xu ly chuoi
inputlist=input("Nhap danh sach cac so (cach bo trong phan cach bang dau phay): ")
numbers=list(map(int, inputlist.split(',')))
#su dung ham va in ket qua
listdaonguoc=daonguoclist(numbers)
print("Danh sach so da xoay nguoc la: ", listdaonguoc)