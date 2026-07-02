num_1 = float(input("enter your first number: "))
num_2 = float(input("enter your second number: "))

if num_1 == num_2:
    print("both number are the same")
elif num_1 > num_2:
    print("the first number is greater than the second number")

elif num_2 > num_1:
    print("the second number is greater than the first number")

elif num_1 < num_2:
    print("the first number is less than the second number")

elif num_2 < num_1:
    print("the second number is less than the first number")

else:
    print("please enter a number")
