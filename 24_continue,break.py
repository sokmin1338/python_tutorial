# continue => 생략

absent = [2,4] #결석
for student in range(1,11):
    if student in absent :
        continue
    print("{0}번은 나와서 교과서를 읽어 보도록.".format(student))
#출력문
# 1번은 나와서 교과서를 읽어 보도록.
# 3번은 나와서 교과서를 읽어 보도록.
# 5번은 나와서 교과서를 읽어 보도록.
# 6번은 나와서 교과서를 읽어 보도록.
# 7번은 나와서 교과서를 읽어 보도록.
# 8번은 나와서 교과서를 읽어 보도록.
# 9번은 나와서 교과서를 읽어 보도록.
# 10번은 나와서 교과서를 읽어 보도록. # 2번과 4번을 생략하고 진행시킴





# break => 뒤에 조건이 더 있어도 반복문을 탈출
absent = [2,4] #결석
no_book = [7]
for student in range(1,11):
    if student in absent :
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지다.{0}은 교무실로와".format(no_book))
        break
    print("{0}번은 나와서 교과서를 읽어 보도록.".format(student))

    #출력문
# 1번은 나와서 교과서를 읽어 보도록.
# 3번은 나와서 교과서를 읽어 보도록.
# 5번은 나와서 교과서를 읽어 보도록.
# 6번은 나와서 교과서를 읽어 보도록. 
# 오늘 수업은 여기까지다.[7]은 교무실로와  # 반복문 탈출