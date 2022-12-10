#BÀI 1
#Nhập một chuỗi kí tự từ bàn phím
kitu = input("Nhập một chuỗi kí tự bất kì: ")

#Nhập tên tập tin từ bàn phím
taptin = input("Nhập tên tập tin: ")

#Lưu chuỗi ký tự ở trên vào tập tin
f1 = open('D:/data/My Documents/ %s.txt' % taptin, mode = 'w')
f1.write(kitu)
