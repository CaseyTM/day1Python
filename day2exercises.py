# for i in range(1,11):
# 	print i;

# for n in range(2,9):
# 	print n;

# start = raw_input("beginning number");
# end = raw_input("ending number");
# for i in range(int(start), int(end)+1):
# 	print i;

# for i in range(1,10,2):
# 	print i;

# for i in range(1,6):
# 	print '*****';
# 	
# size = raw_input("how many tiles would you like your square to be?");
# string = '';
# for n in range(1,(int(size) +1)):
# 	print (string + '*') * int(size);

# height = raw_input("height?");
# width = raw_input("width?");

# for n in range(1,int(height)+1):
# 	full_line = '';
# 	side_line = '';
# 	if n == 1 or n == (int(width)):
# 		print (full_line + '*')* (int(width));
# 	else:
# 		print "*" + ((side_line + ' ') * (int(width)-2)) + '*';
# height = int(raw_input("height?"));
# i = 0
# tri_level = 1;
# base = (2 * height)-1;
# stars = "";
# space = "";
# while i < height:
# 	print (((space + " ") *((base-tri_level)/2)) + ((stars + '*') * tri_level) +((space + " ") *((base-tri_level)/2)))
# 	tri_level +=2;
# 	i +=1;


# for i in range(1,11):
# 	for j in range(1,11):
# 		print j * i;

# string = raw_input("give me a piece of text");
# string_as_list = list(string);
# length = len(string_as_list);
# first_and_last_line = '';
# first_and_last_line += (length+4)*('*');
# print first_and_last_line;
# print '*' + ' ' + string + ' ' + '*';
# print first_and_last_line;

# for i in range(1,100):
# 	counter = i * (i + 1) /2
# 	if counter <= 100:
# 		print counter;


# def factorNumber(number):
# 	for i in range(1,number):
# 		if(number % i == 0):
# 			print i;
# factorNumber(144);


# def toUpper(string):
# 	stringUpper = string.upper();
# 	print stringUpper;

# toUpper("what's going on");

# print string.title();

# string = "whats up mang";


# print string[::-1]
# string = "haba laba ding dong"

# replacements = (('A', '4'), ('E', '3'), ('G', '6'), ('I', '1'), ('O', '0'), ('S', '5'), ('T', '7'))
# new_string = string.upper()
# for old, new in replacements:
# 	new_string = new_string.replace(old,new)
# print new_string;
	
# OR (alternate solution)
# from string import maketrans

# intab = "aegiost"
# outtab = "4361057"
# trantab = maketrans(intab, outtab)
# print string.translate(trantab)
 
# Given a word as a string, print the result of extending any long vowels to the length of 5. Examples:

# Good => Goooood
# Cheese => Cheeeeese
# Man => Man
# Spoon => Spooooon

# vowel_replacements = (('aa', 'aaaaa'), ('ee', 'eeeee'), ('oo', 'ooooo'), ('ii', 'iiiii'), ('uu', 'uuuuu'))

# vow_string = string.lower()
# for old, new in vowel_replacements:
#     vow_string = vow_string.replace(old, new)

# print vow_string


