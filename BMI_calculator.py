height = float(input("Enter your height in cm"))
weight = float(input("Enter your weight in Kg"))
BMI = weight/(height/100)**2
print("Your BMI is ", BMI)
if BMI <= 18.4:

    print("You are underweight.")
elif BMI >= 18.5 and BMI < 24.9:
    print("You have a normal weight.")
elif BMI >= 25.0 and BMI < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")