# 튜플

"값을 추가하거나 변경 불가능"

menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
menu.add("등심까스")
print(menu) # 오류 #실행X

name = "신석민"
age = 26
hobby = "코딩"
print(name, age, hobby) # 신석민 26 코딩


name,age,hobby = ("신석민", 26, "코딩")
print(name,age,hobby) # 신석민 26 코딩