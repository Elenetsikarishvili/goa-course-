odd_list = []
even_list = []

for i in range(5):
    user_num = int(input("Enter number: "))
    
    if user_num % 2 == 0:
        even_list.append(user_num)
    else:
        odd_list.append(user_num)
        
print(odd_list)
print(even_list)
[11:53 AM]
odd_list = []
even_list = []

for i in range(10, 21):
    if i %2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
        
print(odd_list)
print(even_list)