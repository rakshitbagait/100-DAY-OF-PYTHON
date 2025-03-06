# nested if else


weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("normal weight")
else:
    print("overweight")