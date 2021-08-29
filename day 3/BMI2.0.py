height=float(input("enter your height: "))
weight=float(input("enter your weight: "))

BMI=round(weight/height**2,1)

if BMI < 18.5:
    print(f"your BMI is {BMI} and you are underweight")
elif BMI >=18.5 and BMI <25:
    print(f"your BMI is {BMI} and you have normal weight")
elif BMI >=25 and BMI <30:
    print(f"your BMI is {BMI} and you are overweight")
elif BMI >=30 and BMI <35:
    print(f"your BMI is {BMI} and you are obese")
else:
    print(f"your BMI is {BMI} and you are clinically obese")
