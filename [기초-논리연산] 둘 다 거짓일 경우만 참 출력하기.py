# [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기

a, b = input().split(' ')

x = bool(int(a))
y = bool(int(b))

print(not(x or y))