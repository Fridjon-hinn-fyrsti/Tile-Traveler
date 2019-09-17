#notum fall sem tekur inn x og y hnit notanda og skilar volmoguleikum
def option(x ,y):
	if x==1 and y==1:
		return "NXXX"
	if x==1 and y==2:
		return "NESX"
	if x==1 and y==3:
		return "XESX"
	if x==2 and y==3:
		return "XEXW"
	if x==2 and y==2:
		return "XXSW"
	if x==2 and y==1:
		return "NXXX"
	if x==3 and y==1:
		return "NXXX"
	if x==3 and y==2:
		return "NXSX"
	if x==3 and y==3:
		return "XXSW"
#fallid tekur inn x og y hnit og skilar streng med attum
#fallid gerir tedda med if setningum

def print_options(options):
	answer="You can travel: "
	more_than_two=False
	if options[0]!="X":
		answer += "(N)orth"
		more_than_two=True
	if options[1]!="X":
		if more_than_two:
			answer += " or "
		answer += "(E)ast"
		more_than_two=True
	if options[2]!="X":
		if more_than_two:
			answer += " or "
		answer += "(S)outh"
		more_than_two=True
	if options[3]!="X":
			if more_than_two:
					answer += " or "
			answer += "(W)est"
	print(answer+".")

x=1
y=1
victory=False
user_input=""
#geymum x og y hnit notanda
while victory!=True:
	options=option(x,y)
	print_options(options)

	user_input=input("Direction: ")
	user_input=user_input.upper()
	while not (user_input == options[0] or user_input == options[1] or user_input== options[2] or user_input == options[3]):
		print("Not a valid direction!")
		user_input=input("Direction: ").upper()

	if user_input == "N":
		y+=1
	elif user_input == "E":
		x+=1
	elif user_input == "S":
		y-=1
	elif user_input == "W":
		x-=1
	if x == 3 and y==1:
		victory=True
print("Victory!")
#tokum inn input hans
#skopun fall sem synir notanda loglegar leidir og tekur einn attir i strng "NESW"
#berum sman input vid loglegar leidir
#ef input er ologlegt reyna aftur ad taka inn input
#annars uppfaera stadsetningu
#ef stadsetning er (3,1) skila victory og stoppa forrit
