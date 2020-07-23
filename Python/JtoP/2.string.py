print("#문자열 만들기")
a = "Hello, world"
b = 'Python is fun'
c = """Life is too short, You need python"""
d = '''Life is too short, You need python'''
print('a = "Hello, world"', 'output:', a)
print("b = 'Python is fun'", 'output:', b)
print('c = """Life is too short, You need python"""', 'output:', c)
print("d = '''Life is too short, You need python'''", 'output:', d)

food = "Python's favorite food is perl"
print('''\nfood = "Python's favorite food is perl"''', 'output:', food)

say = '"Python is very easy." he says.'
print("""say = '"Python is very easy." he says.'""", 'output:', say)

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print("\nfood = 'Python\'s favorite food is perl'", 'output', food)
print('say = "\"Python is very easy.\" he says."', 'output', say)

multiline = "Life is too short\nYou need python"
print('\nmultiline = "Life is too short\\nYou need python"')
print('output:')
print(multiline)

multiline='''
Life is too short
You need python
'''
print("""multiline=
'''
Life is too short
You need python
'''""")
print('output:')
print(multiline)

multiline="""
Life is too short
You need python
"""
print('''multiline="""
Life is too short
You need python
"""''')
print('output:')
print(multiline)

print('#문자열 연산')
head = "Python"
tail = " is fun!"
print('\"head = "Python", tail = " is fun!"\"')
print('head + tail =', head + tail)
print('head * 2=', head * 2)
print('''
print("=" * 50)
print("My Program")
print("=" * 50)''')
print('output:')
print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short"
print('\'a = "Life is too short"\'')
print('len(a):', len(a))

print('\n#Indexing & Slicing')
a = "Life is too short, You need Python"
print('a = "Life is too short, You need Python"')
print('a[0]:', a[0], '\ta[3]:', a[3], '\ta[-1]:', a[-1], '\ta[-0]:', a[-0], '\ta[-2]', a[-2], '\ta[-5]', a[-5])

b = a[0] + a[1] + a[2] + a[3]
print('b = a[0] + a[1] + a[2] + a[3]', '->output:', b)
print('a[0:4]', '->output:', a[0:4])
print('a[0:3]', '->output:', a[0:3])
print('a[0:5]', '->output:', a[0:5])
print('a[5:7]', '->output:', a[5:7])
print('a[12:17]', '->output:', a[12:17])
print('a[19:]', '->output:', a[19:])
print('a[:17]', '->output:', a[0:17])
print('a[:]', '->output:', a[:])
print('a[19:-7]', '->output:', a[19:-7])

a = "20200723Rainy"
date = a[:8]
weather = a[8:]

print('''
a = "20200723Rainy"
date = a[:8]
weather = a[8:]
''')
print('date ->output:', date)
print('weather ->output:', weather)

year = a[:4]
day = a[4:8]
weather = a[8:]

print('''
year = a[:4]
day = a[4:8]
weather = a[8:]
''')
print('year ->output:', year)
print('day ->output:', day)
print('weather ->output:', weather)

a = "Pithon"
print('a = "Pithon"')
print('a[:1]:', a[:1], ',a[2:]:', a[2:])
print("a[:1] + 'y' + a[2:] ->output:", a[:1] + 'y' + a[2:])

print('\n#Formatting')
print('print("I eat %d apples." % 3)\toutput:', "I eat %d apples." % 3)
print('print("I eat %s apples." % "five")\toutput:', "I eat %s apples." % "five")

number = 3
print('''
number = 3
print("I eat %d apples." % number)\toutput:''', "I eat %d apples." % number)

number = 10
day = "three"
print('''
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))\toutput:''', "I ate %d apples. so I was sick for %s days." % (number, day))

print('\nprint("I have %s apples" % 3)\toutput:', "I have %s apples" % 3)
print('print("rate is %s" % 3.234)\toutput:', "rate is %s" % 3.234)

print('\nprint("Error is %d%%." % 98)\toutput:', "Error is %d%%." % 98, '\n')

print('print("%10s" % "hi")\noutput:')
print("%10s" % "hi")
print('print("%-10sjane." % \'hi\')\noutput:')
print("%-10sjane." % 'hi')
print('print("%0.4f" % 3.141592)\toutput:', "%0.4f" % 3.141592)
print('print("%10.4f" % 3.141592)\toutput:', "%10.4f" % 3.141592, '\n')

print('print("I eat {} apples".format(3))\toutput:', "I eat {} apples".format(3))
print('print("I eat {} apples".format("five"))\toutput:', "I eat {} apples".format("five"))

number = 3
print('''
number = 3
print("I eat {} apples".format(number))\toutput:''', "I eat {} apples".format(number))

number = 10
day = "three"
print('''
number = 10
day = "three"
print("I ate {} apples. so I was sick for {} days.".format(number, day))\toutput:''', "I ate {} apples. so I was sick for {} days.".format(number, day))

print('print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))\toutput:', "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print('print("I ate {} apples. so I was sick for {day} days.".format(10, day=3))\toutput', "I ate {day} apples. so I was sick for {} days.".format(10, day=3))

print('print("{:<10}".format("hi"))\toutput:', "{:<10}".format("hi"))
print('print("{:>10}".format("hi"))\toutput:', "{:>10}".format("hi"))
print('print("{:^10}".format("hi"))\toutput:', "{:^10}".format("hi"))
print('print("{:=^10}".format("hi"))\toutput:', "{:=^10}".format("hi"))
print('print("{:!<10}".format("hi"))\toutput:', "{:!<10}".format("hi"))

y = 3.141592
print('''
y = 3.141592
"{:0.4f}".format(y)\toutput:''', "{:0.4f}".format(y))
print('print("{:10.4f}".format(y))\toutput:', "{:10.4f}".format(y), '\n')

print('print("{{ and }}".format())\toutput:', "{{ and }}".format())

name = 'HAK'
age = 30
print("""
name = 'HAK'
age = 30
print(f'My name is {name}. My age is {age}.')\toutput:""", f'My name is {name}. My age is {age}.')
print("print(f'My age is {age + 1}.')\toutput:", f'My age is {age + 1}.')

d = {'name':'HAK', 'age':30}
print("""
d = {'name':'HAK', 'age':30}
print(f'My name is {d["name"]}. My age is {d["age"]}')\toutput:""", f'My name is {d["name"]}. My age is {d["age"]}', '\n')

print("print(f'{\"hi\":<10}')\toutput:", f'{"hi":<10}')
print("print(f'{\"hi\":>10}')\toutput:", f'{"hi":>10}')
print("print(f'{\"hi\":^10}')\toutput:", f'{"hi":^10}')
print("print(f'{\"hi\":=^10}')\toutput:", f'{"hi":=^10}')
print("print(f'{\"hi\":!<10}')\toutput:", f'{"hi":!<10}')
print("print(f'{\"hi\":!>10}')\toutput:", f'{"hi":!>10}')

y = 3.141592
print("""
y = 3.42134234
print(f'{y:0.4f}')\toutput""", f'{y:0.4f}')
print("print(f'{y:10.4f}')\toutput", f'{y:10.4f}')
print("print(f'{{ and }}')\toutput:", f'{{ and }}')

print('\n#문자열 관련 함수')
a = "hobby"
print('''
a = "hobby"
a.count(\'b\')\toutput:''', a.count('b'))
a = "Python is the best choice"
print('''
a = "Python is the best choice"
a.find('b')\toutput:''', a.find('b'))
print("a.find('k')\toutput:", a.find('k'))

a = "Life is too short"
print('''
a = "Life is too short"
a.index("t")\toutput:''', a.index("t"), '\n')

print('", ".join("abcd")\toutput:', ", ".join("abcd"))
print('", ".join(["a", "b", "c", "d"])\toutput:', ", ".join(["a", "b", "c", "d"]))

a = "hi"
print('''
a = "hi"
a.upper()\toutput:''', a.upper())
a = "HI"
print('''a = "HI"
a.lower()\toutput:''', a.lower())

a = " hi "
print('''
a = " hi "
a.lstrip()\toutput:''', a.lstrip())
print('a.rstrip()\toutput:', a.rstrip())
print('a.strip()\toutput:', a.strip())

a = "Life is too short"
print('''
a = "Life is too short"
a.replace("Life", "Your leg")\toutput:''', a.replace("Life", "Your leg"))
print('a.split()\toutput:', a.split())
b = "a:b:c:d"
print('''
b = "a:b:c:d"
b.split(":")\toutput:''', b.split(":"))