print('#Dictionary 기본')
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(f"""
\"dic = {{'name':'pey', 'phone':'0119993323', 'birth': '1118'}}\"
output: {dic}""")

a = {1: 'a'}
print(f"""
\"a = {{1: 'a'}}\"
a[2] = 'b'
output: {a}""")
a['name'] = 'hak'
print(f"""a['name'] = 'hak'
output: {a}""")
a[3] = [1,2,3]
print(f"""a[3] = [1,2,3]
output: {a}""")
del a[1]
print(f"""del a[1]
output: {a}""")

dic = {'name':'hak', 'phone':'0100000000', 'birth': '1116'}
print(f"""
\"dic = {{'name':'hak', 'phone':'0100000000', 'birth': '1116'}}\"
dic['name']\toutput: {dic['name']}
dic['phone']\toutput: {dic['phone']}
dic['birth']\toutput: {dic['birth']}

dic.keys()\toutput: {dic.keys()}
""")

for k in dic.keys():
    print(k)

print(f"""
list(dic.keys()\toutput: {list(dic.keys())}
dic.values()\toutput: {dic.values()}
dic.items()\toutput: {dic.items()}
dic.get('name')\toutput: {dic.get('name')}
dic.get('phone')\toutput: {dic.get('phone')}
dic.get('money')\t output: {dic.get('money')}
dic.get('money', 'koko')\t output: {dic.get('money', 'koko')}
'name' in dic\toutput: {'name' in dic}
'money' in dic\toutput: {'money' in dic}""")
dic.clear()
print(f"""dic.clear()
print(dic)\toutput: {dic}""")