# 함수
#기본모양 = > def 이름 () :
#               print("실제로 수행되는 내용")
#실행법 = > 이름 ()
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

#---------------------------------------------------------------------------------------------


# 전달값과 반환값
#입금

# balance = 0 #현재 잔고

def deposit(balance,money): # def deposit(현재 잔고,입금 금액)
    print("입금이 완료 되었습니다.잔액은 {0}원 입니다.".format(balance + money))
    return balance + money 

balance = 0
balance = deposit(balance, 1000)
print(balance)


#---------------------------------------------------------------------------------------------

#출금

def withdraw(balance,money):
    if balance >= money:
        print("{0}원이 출금 되었습니다. 잔액은 {1}원 입니다.".format(money,balance - money))
        return balance - money
    elif balance < money :
        print("죄송합니다. 잔액부족으로 인해 출금이 불가합니다.남은 잔액{0}원 입니다".format(balance))
        return balance

balance = withdraw(balance, 100)
print(balance)


#--------------------------------------------------------------------------------------------- 


#야간 수수료
def withdraw_night(balance,money):
    commission = 150
    if balance >= money:
        print("{0}원이 출금 되었습니다. 잔액은 {1}원 입니다. 수수료{2}원".format(money,balance - money -commission,commission))
        return balance - money - commission
    else:
        ("잔액이 부족하여 출금 불가능 현재 잔액 {0}원".format(balance))
        

balance = withdraw_night(balance, 200)
print(balance)


#--------------------------------------------------------------------------------------------- 

#기본값

def profile(name,age=26,main_lang="일본어"):
    print("이름 :{0}, 나이 :{1}, 주 사용 언어 :{2}.".format(name,age,main_lang))

profile("신석민")
profile("장혁재")


#--------------------------------------------------------------------------------------------- 

#키워드 값
def pro(name ,age, main_lang):
    print(name, age, main_lang)

pro(name = "신석민", main_lang = "일본어", age = 26)
pro(main_lang = "소방법", name = "강주원", age = 26)



#--------------------------------------------------------------------------------------------- 


#가변인자
# ,end = " " = > 줄바꿈을 막아줌

def bils(name, age, *language):
    print("이름 :{0}, 나이 :{1}".format(name,age),end = " ")
    for bil in language:
        print(bil, end = " ")
    print()

bils("신석민", 26, "한국어","일본어","영어","독일어","스페인어","러시아어")
bils("강주원", 26, "소방학","소방법","한국사","국어","영어")


#---------------------------------------------------------------------------------------------

#지역변수

gun = 10
def checkpoint(soldiers): # 경계근무
    gun = 20 # 지역변수
    gun = gun - soldiers
    print("[함수 내] 남은 총기 :{0}".format(gun))

print("전체 총:{0}".format(gun)) # 전역변수
checkpoint(2) # 지역변수
print("남은 총:{0}".format(gun)) # 전역변수

#출력 값
# 전체 총:10
# [함수 내] 남은 총기 :18
# 남은 총:10



#---------------------------------------------------------------------------------------------

#전역변수
#기본모양 = > global 변수

gun = 10
def checkpoint(soldiers): # 경계근무
    global gun # 전역변수
    gun = gun - soldiers
    print("[함수 내] 남은 총기 :{0}".format(gun))

print("전체 총:{0}".format(gun)) # 전역변수
checkpoint(2) # 전역변수
print("남은 총:{0}".format(gun)) # 전역변수

#출력 값
# 전체 총:10
# [함수 내] 남은 총기 :8
# 남은 총:8

#---------------------------------------------------------------------------------------------
