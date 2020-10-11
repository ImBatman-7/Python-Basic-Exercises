# Movie tickets prices
# for 0 to 3 years - free
# for 4 to 10 years - 50 rs
# for 11 to 17 years - 100 rs
# for 18 to 100 years - 150 rs

Audience_age = int(input("Please tell your age: "))

if 0 < Audience_age <= 3:
   print("Your ticket is free of cost.")

elif 4 < Audience_age <= 10:
   print("Your ticket price is : 50 rs")

elif 11 < Audience_age <= 17:
   print("Your ticket price is: 100 rs ")

elif 18 < Audience_age:
   print("Your ticket price is: 150 rs")

else:
    print("invalid input")
