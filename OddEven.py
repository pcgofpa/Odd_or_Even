number = int(input("Which number do you want to check? "))

#Determine if number is odd or even
result = number % 2
if result == 0:
    message = "This number is even."
else:
    message = "This number is odd."

#Display whether number is even or odd    
print(message)