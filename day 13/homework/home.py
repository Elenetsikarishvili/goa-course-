#davaleba1
age = int(input("Please enter your age: "))

if age < 18:
    print("You are child")
elif age >= 18 and age < 65:
    print("You are adult")
else:
    print("You are old")


    #davaleba2
    for i in range(5):
      number = int(input("Please enter number: "))

    if number % 2 == 0:
        print(number,"is even")
    else:
        print(number,"is odd")


        #davaleba3
        grade = input("Please enter grade (A,B,C,D or F): ")

if grade == "A":
    print("Excellent!")
elif grade == "B":
    print("Good job!")
elif grade == "C":
    print("You passed.")
elif grade == "D":
    print("You can do better.")
else:
    print("You failed.")


    #davaleba4
    num = 1

while num < 10:
    print(num)
    num = num + 1



    #davaleba5
    num = 4
count = 0
number = 0

while number != num:
    number = int(input("Please enter number (1-10): "))
    count = count + 1
    if number == num:
        print("You guessed number in",count,"try")



        #davaleba6
        for i in range(1, 10+1):
         print(i)