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

#Q8. (1,2,3)이라는 튜플에 4라는 값을 추가하여 (1,2,3,4)처럼 만들어 출력
a = (1, 2, 3)
a = a + (4,)
print('Q8:', a)

#Q9. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명
#1. a['name'] = 'python'
#2. a[('a',)] = 'python'
#3. a[[1]] = 'python'
#4. a[250] = 'python'
print("Q9: 3, reason -> list는 변하는 값이라서 사용 불가")

#Q10. 딕셔너리 a에서 'B'에 해당되는 값을 추출 pop 사용
a = {'A':90, 'B':80, 'C':70}
r = a.pop('B')
print('Q10:', r)

#Q11. a 리스트에서 중복 숫자를 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s = set(a)
print('Q11:', s)

#Q12. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다.
# 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까?
# 그리고 이런 결과가 오는 이유에 대해 설명해 보자.
#a = b = [1, 2, 3]
#a[1] = 4
#print(b)
print('Q12: output: [1, 4, 3], reason: a, b 동일 객체')