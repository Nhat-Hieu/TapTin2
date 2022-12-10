#Sinh ngẫu nhiên 1 danh sách gồm 1000 số nguyên trong khoảng từ [-1000, 1000]
import numpy as np
np.random.seed(123)

def sinh_ngau_nhien(low,high,size):
    list = np.random.randint(low = low , high = high, size = size)
    return list

def main():
    list = sinh_ngau_nhien(-1000,0,1000)
    print(list)

if __name__ == "__main__":
  main()

# Nhập tên tập tin từ bàn phím
taptin = input("Nhập tên tập tin: ")

