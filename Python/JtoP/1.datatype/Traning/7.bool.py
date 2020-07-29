a = True
b = False

print(f'''
"a = True"
"b = False"
type(a)\toutput: {type(a)}
type(b)\toutput: {type(b)}
1 == 1\toutput: {1 == 1}
2 > 1\toutput: {2 > 1}
2 < 1\toutput: {2 < 1}
''')

a = [1, 2 ,3, 4]
while a:
    print(a.pop())

if []:
    print("True")
else:
    print("False")

if ["Python"]:
    print("True")
else:
    print("False")