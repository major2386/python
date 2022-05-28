import random
print("User needs to guess the random number assumed by the game")
top_number = input("Enter a number ? : ")

print("You will now need to guess a number between 0 and " + top_number)

if top_number.isdigit():
	top_number=int(top_number)

	if top_number <= 0:
		print("Enter a number greater than 0 next time. Bye !! ")
		quit()
else:
	print('type a number next time. Bye !!!')
	quit()


random_number = random.randint(0,top_number)

guess_count=0

while True:
	user_guess = input("Guess a number : ")
	if user_guess.isdigit():
		user_guess=int(user_guess)	
	else:
		print("Enter a number next time .")
		continue

	guess_count +=1
	
	if user_guess > random_number:
		print("Think of a lower number")

	if user_guess < random_number:
		print("think of a higher number")
	
	if random_number == user_guess:
		print("You got it . Yayy!!!")
		break
	else:
		print("Incorrect ! Guess Again: ")
	
print('Total number of attempts = ' + str(guess_count) )
	