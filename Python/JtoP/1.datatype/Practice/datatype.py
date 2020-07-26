#연습문제

#Q1. 과목별 평균 점수
#국어: 80, 영어: 75, 수학: 55
korean = 80
english = 75
math = 55
avr = (korean + english + math) / 3
print('Q1:', avr)

#Q2. 자연수 13 홀짝 판단
num = 13
if num%2 == 1:
    print('Q2: 홀')
else:
    print('Q2: 짝')

#Q3. 문자열 'pin = "881120-1068234" 를 yymmdd와 그 뒤로 나누기 Slicing사용
pin = "881120-1068234"
yymmdd = pin[:6]
num = pin[7:]
print(f'Q3: yymmdd->{yymmdd}, Number->{num}')

#Q4. 주민등록번호 'pin = "881120-1068234"의 성별 판별
pin = "881120-1068234"
if pin[7] == 1 or 3:
    print('Q4: 남')
elif pin[7] == 2 or 4:
    print('Q4: 여')

#Q5. a = "a:b:c:d" replace 사용 a#b#c#d로 바꾸기
a = "a:b:c:d"
print('Q5:', a.replace(':', '#'))

#Q6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자. 리스트 내장함수 사용
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print('Q6:', a)

#Q7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자. join함수
a = ['Life', 'is', 'too', 'short']
print('Q7:', " ".join(a))