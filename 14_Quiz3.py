# Quiz

#사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오
#예)http://naver.com
#규칙 1 http://부분은 제외
#규칙 2 점(.)부터 이후 부분 제외
#규칙 3 비밀번호는 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 "e"의 갯수 + "!" 로 구성

#답
A = "http://naver.com"
B = A.replace("http://", "")
C = B[:B.index(".")]
password = C[:3] + str(len(C)) + str(C.count("e")) + "!"
print(password)