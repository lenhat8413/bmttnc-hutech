#nhap cac dong tu nguoi dung
print("Nhap cac dong van ban(Nhap'done' de ket thuc):")
lines=[]
while True:
    line=input()
    if line.lower() =='done':
        break
    lines.append(line)
#chuyen cac dong chu in hoa va in ra man hinh
print("\nCac dong van ban chu in hoa:")
for line in lines:
    print(line.upper())