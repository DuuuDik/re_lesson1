'''
a="Hello"
b="World"
d="{} {}".format(a, b)
#print(d)
'''
'''
user = 'Artyom'
c="{}, {name}".format(a, name = user)
#print(c)
'''
'''
f_format = f"Привет, {user}"
#print(f_format)
'''
'''
len_fun = f'{a} {b}'
#print(len(len_fun))
'''
'''
print(a.upper())
print(b.lower())
print(d.capitalize())
'''
'''
ab = '   Миша   '
bc = ab.strip()
print(ab)
print(bc)
'''
'''
a = "Hello worldЫ".capitalize().replace('ы','')
print(a)
'''
'''
a = 'hello.python.ru'
print(a.split('.'))
'''
'''
a = 'Multiple words in a sentence'
b = a.split()
print(b)
print(len(b))
'''
'''
a = None
b = 0 
c = a == b
print(c)
'''
'''
a = 1
b = 0.5
c = 'Type'
d = False
e = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
'''
'''
name = input('Введите ваше имя: ')
userName = f'Ваше имя - {name}'
print(userName)
'''
'''
age = input('How old are you?')
age = 2021 - int(age)
print(f'You was born in {age}')
'''


