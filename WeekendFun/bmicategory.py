weight = float(input("Enter Your Weight in Kg: "))
height = float(input("Enter Your Height in Meters: "))
bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
