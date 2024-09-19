


# question1: find the current age

# currentYear = int(input("Enter the current year"))
# bornYear = int(input("Enter the born year"))
# ageInYear = currentYear - bornYear
# print(ageInYear)

#  question3: currency converter
#convert rs. into dollar
# print(" Convert ruppes into dollars")
# ruppesAmount = int(input("Enter the amount in Rs. : "))
# rsIntoDollar = (ruppesAmount / 84)
# print(ruppesAmount, " convert into dollar ", rsIntoDollar)


#convert dollar into rupees
# print(" Convert dollar into ruppes")
# dollarAmount = int(input("Enter the amount in Dollar. : "))
# dollarIntoRs = (dollarAmount * 84)
# print(dollarAmount, " convert into ruppes ", dollarIntoRs)


#qUESTION 2: BMI calculator

w = int(input("Enter your weight:"))
h = float(input("Enter your height:"))
x = w/float(h*h)
if x < 18.5:
    print('Underweight')
if x>=18.5 and x<25:
    print("Normal")
if x >= 25 and x < 30:
   print('Overweight')
if x >= 30:
   print('Obesity')