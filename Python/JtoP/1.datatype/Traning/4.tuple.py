print('#tuple기본')
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(f"""\"t1 = ()\"\toutput: {t1}
\"t2 = (1,)\"\toutput: {t2}
\"t3 = (1, 2, 3)\"\toutput: {t3}
\"t4 = 1, 2, 3\"\toutput: {t4}
\"t5 = ('a', 'b', ('ab', 'cd'))\"\toutput: {t5}
""")

print('#튜플다루기')
t1 = (1, 2, 'a', 'b')
print(f"""\"t1 = (1, 2, 'a', 'b')\"

t1[0]\toutput: {t1[0]}
t1[3]\toutput: {t1[3]}
""")

print(f"t1[1:]\toutput: {t1[1:]}")

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(f"""
\"t1 = (1, 2, 'a', 'b')\"
\"t2 = (3, 4)\"

t1 + t2\toutput: {t1 + t2}""")
print(f't2 * 3\toutput: {t2 * 3}')
print(f'len(t1)\toutput: {len(t1)}')