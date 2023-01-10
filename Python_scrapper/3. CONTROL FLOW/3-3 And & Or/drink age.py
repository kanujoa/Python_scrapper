# and, or, 조건문, input을 사용한 음주 가능 나이 계산기
age = int(input("How old are you?"))

if age < 18:
  print("You can't drink.")
elif age >= 18 and age <= 35:
  print("You drink beer!")
elif age == 60 or age == 70:
  print("Birthday party!")
else:
  print("Go ahead!")
