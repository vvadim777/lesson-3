s1 = input("Введите строку s1:")
s2 = input("Введите строку s2:")
print("Вы ввели строку \"s1\" и \"s2\".")
a = len(s1)
b = len(s2)
print(f"Их длинна соответственно {a} и {b}.")
c = s1[0]
print(f"Первый символ первой строки: {c}")
d = s2[-1]
print(f"Последний символ последней строки: {d}")
k = s1 == s2
print("'s1' равен 's2'?", k)
m = s1 in s2
print("'s1' содержится ли в 's2'?", m)
f = s2 not in s1
print("А наоборот?", f)