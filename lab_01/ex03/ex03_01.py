def tinhtongsochan(lst):
    tong=0
    for num in lst:
        if num % 2 == 0:
            tong+=num
    return tong
# nhap danh sach tu nguoi dung va xu li chuoi
input_list = input("Nhap danh sach so nguyen (chuoi cach bang dau phay): ")
numbers = list(map(int, input_list.split(',')))
#su dung ham va in ket qua
tong_chan = tinhtongsochan(numbers)
print("Tong cac so chan trong danh sach la:", tong_chan)