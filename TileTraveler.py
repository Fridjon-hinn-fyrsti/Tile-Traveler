

#notum fall sem tekur inn x og y hnit notanda og skilar volmoguleikum
def option(x ,y):
	if x==1 and y==1:
		coin = 0
		return "NXXX", coin
	if x==1 and y==2:
		coin = 1
		return "NESX", coin
	if x==1 and y==3:
		coin = 0
		return "XESX", coin
	if x==2 and y==3:
		coin = 1
		return "XEXW", coin
	if x==2 and y==2:
		coin = 1
		return "XXSW", coin
	if x==2 and y==1:
		coin = 0
		return "NXXX", coin
	if x==3 and y==1:
		coin = 0
		return "NXXX", coin
	if x==3 and y==2:
		coin = 1
		return "NXSX", coin
	if x==3 and y==3:
		coin = 0
		return "XXSW", coin
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

game_over = False
while not game_over:
	x=1
	y=1
	victory=False
	user_input=""
	coins = 0
#geymum x og y hnit notanda
	while victory != True:
		options, coin = option(x,y)
		if coin != 0:
			coin_input = input('Pull a lever (y/n): ').upper()
			if coin_input == 'Y':
				coins += 1
				print('You received 1 coin, your total is now {}.'.format(coins))
		print_options(options)
		user_input=input("Direction: ")
		user_input=user_input.upper()
		while (not (user_input == options[0] or user_input == options[1] or user_input== options[2] or user_input == options[3])) or user_input == 'X':
			print("Not a valid direction!")
			print_options(options)
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
	print("Victory! Total coins {}.".format(coins))
	user_input=input("Play again (y/n): ").upper()
	if user_input == 'N':
		game_over = True
#tokum inn input hans
#skopun fall sem synir notanda loglegar leidir og tekur einn attir i strng "NESW"
#berum sman input vid loglegar leidir
#ef input er ologlegt reyna aftur ad taka inn input
#annars uppfaera stadsetningu
#ef stadsetning er (3,1) skila victory og stoppa forrit