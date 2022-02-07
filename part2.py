a = int(input('Введите число a:'))
b = int(input('Введите число b:'))
c = int(input('Введите число c:'))

scobki = 4*(c**5) // 6
#print(scobki)
chislitel = a**2 + b**2
#print(chislitel)

znamenatel = 3*b - 4
#print(znamenatel)
x = (chislitel // znamenatel)//scobki
y = (chislitel // znamenatel)%scobki
print(x)
print(y)