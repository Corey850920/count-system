#檢查檔案是否存在
import os

if os.path.isfile(r"C:/Users/Administrator/Desktop/記帳程式/products.csv"):
    print("Y")   
else: 
    print("N")

#讀取檔案
products = []
with open("products.csv","r",encoding="utf-8") as f:
    for line in f:
        if "商品,價格" in line:
            continue
        [name,price]=line.strip().split(",")
        products.append([name,price])
    print(products)
            
#讓使用者輸入
while True:
    name = input("請輸入商品名稱:")
    if name.lower()== "q":
        break
    price =int(input("請輸入商品價格:"))
    products.append([name,price])    
print(products)

#印出檔案       
for i in products:
    print(i[0],"的價格是",i[1])
#寫入csv 
with open(r"C:/Users/Administrator/Desktop/記帳程式/products.csv","w",encoding="utf-8") as f:
    f.write("商品,價格\n")
    for i in products:
        f.write(i[0]+","+str(i[1])+"\n")
    