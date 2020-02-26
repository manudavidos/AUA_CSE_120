tries = 0
max_tries = 4

grade_hw = -1
grade_project = -1

while (not(0 <= grade_hw <= 100 or tries >= max_tries)):
  if (tries > 0):
    print("ERR001: Your Grade is Not Valid")
  grade_hw = int(input("Please insert your grade for HW: "))
  tries += 1

if (0 <= grade_hw <= 100):
  print("Your HW Grade is", grade_hw)
else:
  print("ERR002: Maximum number of trials reached")
