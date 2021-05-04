# 한 줄 for문

students = [1,2,3,4,5,]
students = [i+100 for i in students] # students안에 하나 하나의 요소들에게 100을 더해줌
print(students) # = > [101, 102, 103, 104, 105]


bils = ["sok min", "혁재", "큰 누님", "알바생"]
bils = [len(i) for i in bils]
print(bils) # = > [7, 2, 4, 3] bils 안 요소 각각의 문자 길이를 알려줌


SM = ["kiss", "hug"]
SM = [i.upper() for i in SM]
print(SM) # = > ['KISS', 'HUG']