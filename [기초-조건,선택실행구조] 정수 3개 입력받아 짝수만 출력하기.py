# [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기

num1, num2, num3 = input().split(' ')

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 % 2 == 0 :
    print(num1)

if num2 % 2 == 0 :
    print(num2)

if num3 % 2 == 0 :
    print(num3)