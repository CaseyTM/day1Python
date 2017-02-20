# arrays (lists) are mutable (changeable) but what if you do not want them to be so, enter a tuple, a constant array (list)

a_tuple = (1,3,8)
print a_tuple;

# can loop through them and treat them the same as a list in most cases

for number in a_tuple:
	print number;

teams = ('falcons', 'hawks', 'atl_united', 'silverbacks');
for team in teams:
	if team == 'hawks':
		print 'Go Hawks!';
	else:
		print "It's basketball season";

team_a = 'falcons';
print team_a == 'falcons';
# comparison operators have same syntax as JS
team_b = 'braves';
condition_1 = team_a == 'falcons';
condition_2 = team_b == 'braves';
if condition_1 and condition_2:
	print 'Hooray';

# python's version of indexOf is "in"
print 'hawks' in teams
if team == 'hawks':
	print 'go hawks';
elif team == 'falcons':
	print 'sad superbowl';

if 'hawks' in teams:
	print 'go hawks';
if 'falcons in teams':
	print 'go falcons';

# message = input("please enter your name");
height = raw_input("in inches, how tall are you?\n");
if(int(height) >= 42):
	print "you are tall enough to go on the batman rollercoaster";
else:
	print "maybe try the kiddie coaster";

current = 1;
# while (current < 10):
# 	print current;
# 	current += 1;

answer = "play"
while answer != "quit":
	answer = raw_input("say quit to stop the game\n");

























