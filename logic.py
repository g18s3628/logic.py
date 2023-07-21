num1 = 14
num2 = 6
num3 = 12
#Calculating the average of the numbers 
average = (num1 + num2 + num3)/2
print(f"The average of these numbers are: {average}")
#The value of the average is incorrect

print("\n")
#Requesting the user to guess a number that is unknown to them then trying to get them closer to the number
num = int(input("Enter a number to guess :"))
if num == 5:
    print("The number is spot on!")
elif num >= 6:
    print("The number you entered is smaller than the number, try again")
elif num >= 10:
    print("The number you entered is too big than the number, try again")
elif num <= 4:
    print("The number you entered is larger than the number, try again")
else:
    print("The number you entered is too small, try again")


#The outputs say the wrong give the wrong guesses the output does not give clear indications 
print("\n")
   
print("In the above codes there are Logical errors ")
