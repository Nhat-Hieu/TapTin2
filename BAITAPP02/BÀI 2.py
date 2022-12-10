#Nhập tên tập tin từ bàn phím
taptin = input("Nhập tên tập tin: ")

#Đọc nội dung tập tin và in ra màn hình
f2 = open('D:/data/My Documents/%s.txt' % taptin, mode = 'r')
print(f2.read())