# 문자열 포맷

#방법 1
# %d = 정수 입력 값
print("나는 %d살 입니다" % 26)

# %s = 문자열, 정수, 문자 전부 가능하다
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# %c = 문자 
print("Apple은 %c로 시작해요" % ("A"))


#방법 2
# .format
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}을 좋아해요.".format("빨간","파란"))
print("나는 {0}와 {1}를 좋아해요.".format("바나나","사과"))

#방법 3
print("나는 {age}살 이며, {color}색를 좋아해요.".format(age=26, color="검정"))

#방법 4
age = 26
color = "검정"
print(f"나는 {age}살이며, {color}색을 좋아해요.")