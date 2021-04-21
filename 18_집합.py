# 집합(set)
"중복X,순서X"

my_set = {1,2,3,3,3}
print(my_set) #{1,2,3}


java = {"유재석", "김태호", "양세형"} 
python = set(["유재석", "박명수"])

# <교집합> (java,python을 모두 할 수 있는 개발자) 
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}


# <합집합> (java도 할 수 있거나, python도 할 수 있는 개발자)
print(java | python) # {'유재석', '양세형', '박명수', '김태호'}
print(java.union(python)) # {'유재석', '양세형', '박명수', '김태호'}


# <차집합> (java는 할 수 있지만 python은 할줄 모르는 개발자)
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# python을 할 수 있는 사람이 추가됨
python.add("김태호")
print(python) # {'유재석', '박명수', '김태호'}


# java를 잊었어요
java.remove("김태호")
print(java) # {'양세형', '유재석'}

