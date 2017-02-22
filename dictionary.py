# dictionary is the python term for a JS OBJECT
# must put keys (properties) in quotes so it is not seen as a variable
# referred to key-value pairs rather than property/value in JS
zombie = {
	'speed':10,
	'power':6,
	'hunger':12,
	'name':'Zombie'
}
print zombie
print zombie['speed'];
zombie['startX'] = 200;

# you can add a new key just like in JS, variables are dynamic in PY as well
zombie['weapon'] = 'fist';
print zombie;

# change the value of an existing key just like JS
if zombie['speed'] < 5:
	zombie['position'] = zombie['startX'] + 2;

# you can delete a key with del
zombie['pointless']= 'duh';
del zombie['pointless'];
print zombie

# store all the techs we know in a dictionary and set the value from 1-10
skill1 = "Redux"

known_languages = {
	"javascript": 1,
	"nodeJS":2,
	"Python":3,
	"HTML5":4,
	"CSS3":5,
	"MySQL":6,
	"MongoDB":7,
	"Bootstrap":8,
	"React":9,
	"jquery":10,
	skill1:11
}
print known_languages

# for loops through dictionaries begin with the KEY (placeholder), value
for key,value in known_languages.items():
	print value;
if zombie.has_key('mother_name'):
	print zombie['mother_name'];

for key in zombie:
	print zombie[key];

# just like in JS, you can place dictionaries inside of lists (arrays)  (objects in arrays)
zombie = [];
zombie.append({
	'speed': 10,
	'power': 6,
	'hunger': 5,
	'name': 'Bill'
})	
zombie.append({
	'speed': 12,
	'power': 9,
	'hunger': 2,
	'name': 'mark'
})	
print zombie;
print zombie[0];
print zombie[0]['name'];

for zombie in zombie:
	print zombie['name'];

# just like a JS object you can assign a list to a dictionary key
zombie[0]['victim'] = ['sean', 'rishi', 'anna'];
print zombie[0];

zombie[0]['super_mode']={
	'power':23,
	'hunger':20,
	'weapon':'baseball bat'
}
















