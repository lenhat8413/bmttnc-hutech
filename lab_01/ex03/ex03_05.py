def demsolanxuathien(lst):
    count_dict={}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

#nhap danh sach tu nguoi dung
input_string = input("Nhap danh sach cac phan tu, cach nhau bang dau cach: ")
word_list = input_string.split()

#goi ham demsolanxuathien
solanxuathien = demsolanxuathien(word_list)
print("So lan xuat hien cua moi phan tu:",solanxuathien)