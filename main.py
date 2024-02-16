print("Hello,Python!")

print("Привет,Python!")
print("Hello,Python!")
print("Bonjour,Python")
print("Hey,Python!")
print("Hola,Python!")

print("Привет", "Python!", sep=" ")

print("""
     (\___/)
     (='.'=)
     (")_(")
     """)

print("Привет,Python!\nHello,Python!\nBonjour,Python!\nHey,Python!\nHola,Python!")

name = input("Имя:")
print("Здравствуйте," + name)

name = input("Имя:")
print("Здравствуйте," + name)
habits = input("Your habit:")
print("Отлично!" + habits + " - хорошее увлечение")

login = input("Введите логин:")
password = input("Введите пароль:")
newpassword = input("Введите новый пароль:")
print("User", login, "has change the password to", newpassword)

d = ("Eminem - Mockingbird", "50 Cent - In da club", "Snoop dogg - Doggystyle", "Nate dogg - Ooh Wee", "Jay-Z - Numb")
s = ("Папин плейлист:\nEminem - Mockingbird\n50 Cent - In da club\nSnoop dogg - Doggystyle\nNate dogg - Ohh Wee\nJay-Z - Numb")
print(s)
print("Мамин плейлист:")
for m in reversed(d):
    print(m)

a = input("Номер рейса:")
b = input("Название авиакомпании(на русском)")
c = input("Название авиакомпании(на английском)")
d = input("город прилёта(на русском)")
e = input("город прилёта(на английском)")
print("Заканчивается посадка на рейс", a, b, "до", d)
print("This is the final boarding call for", c, "flight", a, "to", e)

name = input("Имя:")
print("Привет, " + name + "!")

a = int(input("Значение:"))
b = (a - 96*48)/6
print(b)

a = int(input("Значение:"))
b = int(input("Значение:"))
c = abs(3.141592653589793238*(b**2-a**2))
print(c)

a = int(input("Значение:"))
b = ((a+2)*3-6)/3-4
print(b)

c = float(input("Введите значение:"))
i = c / 2.54
f = i / 12
y = f / 3
m = y / 1760
print(y, "ярдов")
print(m, "мили")
print(f, "футов")
print(i, "дюймов")