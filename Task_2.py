print("Введите координату X первой точки")
x1 = float(input("X1="))
print("Введите координату Y первой точки")
y1 = float(input("Y1="))
print("Введите координату X второй точки")
x2 = float(input("X2="))
print("Введите координату Y второй точки")
y2 = float(input("Y2="))
if x1 == x2:
    if y1 == y2:
        print("Составить уравнение прямой невозможно. Координаты должны различаться")
    else:
        print(f"y={x1}")
else:
    k=(y2-y1)/(x2-x1)
    b=y1-x1*(y2-y1)/(x2-x1)
    if b<0:
         print(f"y={k}*x{b}")
    else:
         print(f"y={k}*x+{b}")