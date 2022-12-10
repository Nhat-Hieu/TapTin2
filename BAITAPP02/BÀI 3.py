#Nhập tên tập tin từ bàn phím
taptin = input("Nhập tên tập tin: ")

#Nhập một chuỗi kí tự từ bàn phím
kitu = input("Nhập một chuỗi kí tự bất kì: ")

#Ghi chuỗi kí tự này vào cuối tập tin ở trên
f3 = open('D:/data/My Documents/%s.txt' % taptin, mode = 'a')
f3.write(kitu)