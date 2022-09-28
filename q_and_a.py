name = input ("Please input your name.")
greeting = input(f"Hello {name}, would you like to learn some Python today?")
okay_then = ("Then let us begin!")
if greeting == "yes":
	print (okay_then)
	print (f"We have much work ahead of us, {name}.")
elif greeting == "no":
	print ("Okay, goodbye!")
else:
	print ("Invalid input, accept either 'yes' or 'no'.")

age = int(input(f"Before we begin, {name}, please tell me your age"))
if age <= 16:
	print ("Wow, you have started your journey younger than me, you should be proud.")
elif age == 17:
	print (f"At the same age as me, maybe we are alike {name}.")
else:
	print (f"Older than when I started, but never fear, {name}, we all have to start at some point.")
