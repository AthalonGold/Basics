things= ['food', 'mountain bikes', 'coffee']
things.insert(1,"hot dogs")
things.append("cars")
del things[3]
message=f"\t\nMy favourite thing about life is {things[2].lower()}."
print(message)
print(things)


magicians=['alice', 'david', 'carter']
for magician in magicians:
	if magician=='alice':
		print(f"Hey {magician.title()}, you did well.")
	else:
			print(f"Hey {magician.title()}, you are terrible.")
if 'alice' in magicians:
	print ("I love you, Alice")
else:
	print ("Where is alice?")


