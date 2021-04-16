# 사전

C = {3:"유재석",100:"김종국"} # 기본 모양
print(C)

# 출력 방법
print(C[3])
print(C[100])
print(C.get(3))
print(C.get(100))


# 확인 방법
print(3 in C)
print(100 in C)
print(200 in C)


# 문자열 가능
Cabi = {"A-3":"유재석", "c-20":"조세호", "b-1021": "석민"}
print(Cabi["A-3"])
print(Cabi["c-20"])



# 자료 추가
Cabi["A-3"] = "김종국"
print(Cabi["A-3"])



# 자료 삭제
del Cabi["A-3"]
print(Cabi)



# key만 출력
print(Cabi.keys())


# Valuse만 출력
print(Cabi.values())



# Ket랑 Values랑 동시 출력 가능
print(Cabi.items())





