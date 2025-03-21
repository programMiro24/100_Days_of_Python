weight = float(input())
height = float(input())

bmi = weight / (height ** 2)
print(bmi)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")
# 🚨 Do not modify the values above
# Write your code below 👇
