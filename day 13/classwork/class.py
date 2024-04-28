age = int(input("please enter your age: "))

if age >= 0 and age < 18:
    print("you are kid")
elif age >= 18 and age < 50:
    print("you are an adult")
else:
    print("you are old")


number = float(input("Please enter number: "))

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is 0")
