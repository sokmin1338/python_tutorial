# 문자열 처리 함수
A = "Sokmin likes Kunchu"
print(A.lower())
print(A.upper())
print(A[0].islower())
print(A[0].isupper())
print(len(A))
print(A.replace("likes","loves"))
# .lower = 소문자 프린트
# .upper = 대문자 프린트
# A[0].islower = 0번째 스펠링이 소문자가 맞는지 판별
# A[0].isupper = 0번째 스펠링이 대문자가 맞는지 판별
# .len(A) = A의 문장 길이를 알려줌
# .replace = 바꾸고 싶은 단어가 있을때 사용



# index
index = A.index("n")
print(A.index("n"))
print(A.index("n", index + 1))
# n이 몇 번째 자리에 있는지 알려줌

#find
print(A.find("S"))
# S가 몇 번째 자리에 있는지 알려줌

#index와 find의 차이점은 index는 없는 단어를 찾으려 하면 오류가 나고
#find는 없는 단어를 해도 -1이 뜨고 오류 없이 진행됨

# count
print(A.count("i"))
# A라는 변수 안에 i가 몇 번 등장하는지 알려줌
