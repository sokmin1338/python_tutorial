# 자료구조의 변경

menu = {"커피","우유","쥬스"}
print(menu, type(menu)) # {'우유','커피','쥬스'} < class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['우유', '커피', '쥬스'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('쥬스', '커피', '우유') <class 'tuple'>


# 변경하고 싶은 구조를 씌우면 된다~ 
# {} = > 문자열 포맷, 사전, set
# [] = > list