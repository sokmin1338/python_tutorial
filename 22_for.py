# 반복문 for


#(기본 모양) for 변수1 in 변수2 or 리스트 :
#     print("{0} 하고싶은말".format(변수1))

# range


for W_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(W_no))
#출력문
# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4


for S_no in range(1, 21):
    print("대기번호 :{0}".format(S_no))
# 출력문
# 대기번호 :1 
# 대기번호 :2 
# 대기번호 :3 
# 대기번호 :4 
# 대기번호 :5 
# 대기번호 :6 
# 대기번호 :7 
# 대기번호 :8 
# 대기번호 :9 
# 대기번호 :10
# 대기번호 :11
# 대기번호 :12
# 대기번호 :13
# 대기번호 :14
# 대기번호 :15
# 대기번호 :16
# 대기번호 :17
# 대기번호 :18
# 대기번호 :19
# 대기번호 :20


bils = ["혁재","석민","원기"]
for man in bils :
    print("{0}님 주문하신 커피 나왔습니다.".format(man))
# 출력문
# 혁재님 주문하신 커피 나왔습니다.
# 석민님 주문하신 커피 나왔습니다.
# 원기님 주문하신 커피 나왔습니다.