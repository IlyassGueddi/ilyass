
weight = int(input("set your weight in kg: "))
height = int(input("set your height in cm: "))
age = int(input("set your age: "))
gender = str(input("set your gender: (men/women) "))
activity = str(input("set your activity level: (sendentary/lightly active/ moderately active/ very active/ super active)"))

BMR1 = (10*weight) + (6.25*height) - (5*age) + 5
BMR2 = (10*weight) + (6.25*height) - (5*age) - 161

if gender == "men":
  print(f"your BMR is {BMR1}")
  if activity == "sendentary":
    TDEE1 = BMR1 * 1.2
    print(f"your TDEE is {TDEE1}")
  elif activity == "lightly active":
    TDEE2 = BMR1 * 1.375
    print(f"your TDEE is {TDEE2}")
  elif activity == "moderately active":
    TDEE3 = BMR1 * 1.55
    print(f"your TDEE is {TDEE3}")
  elif activity == "very active":
    TDEE4 = BMR1 * 1.725
    print(f"your TDEE is {TDEE4}")
  elif activity == "super active":
    TDEE5 = BMR1 * 1.9
    print(f"your TDEE is {TDEE5}")


elif gender == "women":
  print(f"your BMR is {BMR2}")
  if activity == "sendentary":
    TDEE1 = BMR2 * 1.2
    print(f"your TDEE is {TDEE1}")
  elif activity == "lightly active":
    TDEE2 = BMR2 * 1.375
    print(f"your TDEE is {TDEE2}")
  elif activity == "moderately active":
    TDEE3 = BMR2 * 1.55
    print(f"your TDEE is {TDEE3}")
  elif activity == "very active":
    TDEE4 = BMR2 * 1.725
    print(f"your TDEE is {TDEE4}")
  elif activity == "super active":
    TDEE5 = BMR2 * 1.9
    print(f"your TDEE is {TDEE5}")