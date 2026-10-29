year = 2026
month = 1
day = 1

print (f"오늘은 {year}년 {month}월 {day}일입니다")


num1 =91000

num2 = 12000

print (f"금주 스타벅스 라떼 생산은 {num1}톤이며 {num2}톤씩 {num1%num2}번 9,10탱크에 믹스쳐야합니다")


weekly_plan = 91000
batch = 12000
count = weekly_plan//batch
잔량 = weekly_plan%batch

print (f"12톤씩 {count}번이고 찬량{잔량}톤 칩니다")

##name = "최지웅"
age = 32

print("제 이름은 %s이고 %d살입니다." % (name, age))

# %s, %d 같은 '포맷 스트링'이라는 것을 사용하는 방식입니다. C나 Java처럼 예전 프로그래밍 언어에서 주로 쓰던 방식인데, 파이썬에서도 사용할 수 있지만, 이제는 잘 쓰지 않는 오래된 방식입니다. 이런 게 있다는 것 정도만 알아 두시면 충분해요.

name = "최지웅"
age = 32

print("제 이름은 {}이고 {}살입니다.".format(name, age))

#format() 메소드를 이용해 문자열 안에 변수를 넣는 방법입니다. f-string이 등장하기 전에는 가장 널리 사용되던 방법이에요. 지금은 f-string을 사용하는 것이 일반적입니다.