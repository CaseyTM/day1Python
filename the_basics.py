# underscores more common than camelcase for Python 

print "Casey McCaskill"

name = "Casey McCaskill";
name = "Casey" + "McCaskill";

forty_two = 40 + 2;
print forty_two;

# Arrays are called Lists in Python
animals = ['wolf', 'giraffe', 'hippo'];
print animals
print animals[0];
# print full length of the array 
print animals[-1];

# push to an array
animals.append("alligator");
print animals;

# to delete an index use remove method
animals.remove("wolf");
print animals;

# we can insert into any index with the insert method
animals.insert(0,'zebra');
print animals;
# replace a given index with horse
animals[0] = "horse"
print animals;
del animals[0];

# pop method works the same way, remove the last element
animals.pop()
print animals;

# split works the same way as well 
dc_class = "Michael, Paul, Mason, Casey, Connie, Sarah, Andy";
dc_class_as_list = dc_class.split(", ");
print dc_class_as_list;

# sorted method will sort the list, but not actually change into
sorted_class = sorted(dc_class_as_list);

dc_class_as_list.sort()
print dc_class_as_list;

# reverse method reverses the list, based on index
dc_class_as_list.reverse();
print dc_class_as_list;

# len attribute, it works like .length in JS
len(dc_class_as_list); 

# slice works just like it did in JS, [xvariable:xvariable]
   # includes 2 but excludes 3

print dc_class_as_list[2:3];

# for loop is For,what you call this one, in, variable
for student in dc_class_as_list:
	# indentation matters bigtime here in Python
	print student

for i in range(1,10):
	print i;

for i in range(1,len(dc_class_as_list)):
	print dc_class_as_list;

# funtions in python are known as definitions, ergo def
def sayHello():
	print "Hello, World";

sayHello();

def say_hello_with_name(name):
	print "Hello, " + name;

say_hello_with_name("Casey");







