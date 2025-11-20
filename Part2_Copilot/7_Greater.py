# Please write a program which asks for two integer numbers. 
# The program should then print out whichever is greater.
# If the numbers are equal, the program should print a different message.

# Some examples of expected behaviour:

# Sample output
# Please type in the first number: 5
# Please type in another number: 3
# The greater number was: 5

# Sample output
# Please type in the first number: 5
# Please type in another number: 8
# The greater number was: 8

# Sample output
# Please type in the first number: 5
# Please type in another number: 5
# The numbers are equal!

# Write your code here:
int_number1= int(input("please type in number 1:"))
int_number2= int(input("please type in number 2:"))
if int_number1 > int_number2:
    print("The greater number was:", int_number1)
elif int_number2> int_number1:
    print("The greater number was:", int_number2)
else:
    print("The numbers are equal")
    