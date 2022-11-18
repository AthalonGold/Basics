a=int(input("Enter your first number.")) # The two inputs are converted into an integer  
b=int(input("Enter your second number."))

c=input("What should be done with the two numbers?")
if c == "multiply":
	print (f"The answer is {a*b}.")
elif c == "divide":
	print (f"The answer is {a/b}.")
elif c == "subtract":
	print(f"The answer is {a-b}.")
elif c == "add":
	print (f"The answer is {a+b}.")
else:
	print ("Invalid input, please try again")

restart=input("Would you like to try again? Enter 1 for yes, Enter 0 for no.") # Easy way to restart the calculator
if restart=="1":
	begin()
elif restart=="0":
	print("Ok, goodbye.")
else:
	print("Gibberish, bye.")
