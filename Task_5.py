print("Введите год")
year = int(input())
if ((year%4 == 0 and year%100 != 0) or (year%400 == 0)) :
    print (f"Год {year} високосный")
else:
    print(f"Год {year} не високосный ")