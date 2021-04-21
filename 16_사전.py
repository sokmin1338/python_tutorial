# 사전

C = {3:"유재석",100:"김종국"} # 기본 모양
print(C) # {3: '유재석', 100: '김종국'}

# 출력 방법
print(C[3]) #유재석
print(C[100]) #김종국
print(C.get(3)) #유재석
print(C.get(100)) #김종국


# 확인 방법
print(3 in C) #True
print(100 in C) #True
print(200 in C) #False


# 문자열 가능
Cabi = {"A-3":"유재석", "c-20":"조세호", "b-1021": "석민"} 
print(Cabi["A-3"]) #유재석
print(Cabi["c-20"]) #조세호



# 자료 추가
Cabi["A-3"] = "김종국"
print(Cabi["A-3"]) #김종국



# 자료 삭제
del Cabi["A-3"]
print(Cabi) #김종국 제거



# key만 출력
print(Cabi.keys())
# dict_keys(['c-20', 'b-1021'])

# Valuse만 출력
print(Cabi.values())
# dict_values(['조세호', '석민'])


# Ket랑 Values랑 동시 출력 가능
print(Cabi.items())
# dict_items([('c-20', '조세호'), ('b-1021', '석민')])






