grade_hw = -1
tries = 0
while (not(0 <= grade_hw <= 100)):
  if (not(tries == 0) and tries < 4):
    print("ERR001: Your Grade is Not Valid")
    grade_hw = int(input("Please insert your grade for HW: "))
  else:
    if (tries == 0):
      grade_hw = int(input("Please insert your grade for HW: "))
    else:
      if (tries == 4):
        print("ERR002: Maximum number of trials reached")
  tries += 1

print("Your HW Grade is", grade_hw)
