numbers = range(1,10);
print numbers;
player_guess = raw_input("Pick a number from 1-10");
if player_guess in numbers:
	print "you got it";
else:
	print "keep guessing";


