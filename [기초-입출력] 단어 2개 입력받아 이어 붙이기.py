# [기초-입출력] 단어 2개 입력받아 이어 붙이기

# 단어는 문자(character)들로 만든다.
# 문자들로 구성된 문장을 문자열(string)이라고 부른다.
# 문자열에는 공백문자(' ')가 포함될 수 있는데, 
# 문자 1개는 길이가 1인 문자열이라고 할 수 있고
# 공백문자(' ')가 없는 문자열은 단어(word)라고 할 수 있다.

str1, str2 = input().split(' ')

print(str1 + str2)