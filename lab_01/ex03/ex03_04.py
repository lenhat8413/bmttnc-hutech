def truycapphantu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element , last_element

#nhap tuple tu nguoi dung
input_tuple = eval(input("Nhap mot tuple, vi du(1,2,3): "))
first, last =truycapphantu(input_tuple)

#in ket qua 
print("Phan tu dau tien:", first)
print("Phan tu cuoi cung:", last)