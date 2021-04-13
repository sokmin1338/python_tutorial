# 리스트

# .append() => 자료 추가
A = ["재석","종국"]
A.append("하하")
print(A) # => ['재석', '종국', '하하']



# .insert() => 원하는 위치에 자료를 추가해서 넣을 수 있음
A = ["재석","종국"]
A.insert(1, "하하") #(1 =>넣고 싶은 위치 , "넣고 싶은 자료")
print(A) # => ['재석', '하하', '종국']



# .pop() => 뒤에서 한 개씩 제거 가능
A = ["재석", "종국", "하하"]
A.pop()
print(A) # => ['재석', '종국']



# .count() => 문자열, 숫자열과 동일
A = ["재석", "종국", "하하"]
print(A.count("종국"))



# .sort() => 정렬
A = [6,21,12,102,3214,42241,5332452,432222141415,534432]
A.sort()
print(A) # => [6,12,21,102,3214,42241,534432,5332452,4322222141415]



# .revers() => 순서 뒤집기
A = [6,21,12,102,3214,42241,5332452,432222141415,534432]
A.reverse()
print(A) # => [534432, 432222141415, 5332452, 42241, 3214, 102, 12, 21, 6]



# .clear => 모두 지우기
A = [1,2,3,4]
A.clear
print(A) # => []



# 다양한 자료형과 함께 사용가능함
A = ["유재석", 20, True]
print(A) # => ['유재석', 20 ,True]



# .extend()
A = [1,2,3,4,5,]
B = ["석","민"]
A.extend(B)
print(A) # => [1,2,3,4,5,'석','민']
