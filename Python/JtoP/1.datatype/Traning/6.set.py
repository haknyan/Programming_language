s1 = set([1,2,3])
s2 = set("Hello")
print(f'''
"s1 = set([1,2,3])"
print(s1)\toutput: {s1}
"s2 = set("Hello")"
print(s2)\toutput: {s2}''')

l1 = list(s1)
t1 = tuple(s1)
print(f'''
"l1 = list(s1)"
print(l1)\toutput: {l1}
l1[0]\toutput: {l1[0]}
"t1 = tuple(s1)"
print(t1)\toutput: {t1}
t1[0]\toutput: {t1[0]}''')

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(f'''
"s1 = set([1, 2, 3, 4, 5, 6])"
"s2 = set([4, 5, 6, 7, 8, 9])"

s1 & s2\toutput: {s1 & s2}
s1.intersection(s2)\toutput: {s1.intersection(s2)}

s1 | s2\toutput: {s1 | s2}
s1.union(s2)\toutput: {s1.union(s2)}

s1 - s2\toutput: {s1 - s2}
s2 - s1\touptut: {s2 - s1}
s1.difference(s2)\toutput: {s1.difference(s2)}
s2.difference(s1)\touptut: {s2.difference(s1)}''')

s1 = set([1, 2, 3])
s1.add(4)
print(f'''
"s1 = set([1, 2, 3])"
s1.add(4)
print(s1)\touptut: {s1}''')

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(f'''
"s1 = set([1, 2, 3])"
s1.update([4, 5, 6])
print(s1)\touptut: {s1}''')

s1 = set([1, 2, 3])
s1.remove(2)
print(f'''
"s1 = set([1, 2, 3])"
s1.remove(2)
print(s1)\touptut: {s1}''')