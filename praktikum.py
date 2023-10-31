a = int (input("masukan bilangan A:"))
b = int (input("masukan bilangan B :"))
c = int (input("masukan bilangan C :"))

if a > b:
    maks = a

else:
     maks = b

if c > maks:
    maks = c

print("bilangan terbesar adalah", maks)