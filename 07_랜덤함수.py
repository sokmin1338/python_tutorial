#랜덤함수
# from randome import *
from random import *
print(random()) # 0.0이상 ~ 1.0 미만의 임의의 값
print(random() *10) # 0.0이상 ~10.0 미만의 임의의 값
print(int(random()*10)) #소숫점 제거, 0이상 ~ 10미만의 임의의 값
print(int(random()*10)+1) # 0이 빠지고, 1이상 ~ 10이하의 임의의 값

#핵심
print(randrange(1, 200)) # 1이상 ~ 200미만의 임의의 값 하나 생성
print(randint(1, 200)) # 1이상 ~ 200이하의 임의의 값 하나 생성
# randrange 는 ~ 이상 ~ 미만
# randint 는 ~ 이상 ~ 이하



# shuffle, sample => 을 사용하려면 list 구조를 만들어야 함
lis = [1,2,3]
shuffle(lis) # lis 안의 값을 무작위로 섞어줌
sample(lis, 1) # lis 안의 값중에 1개를 뽑아줌
