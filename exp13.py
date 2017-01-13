from sys import argv, path

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "The path is:", path[0]
print "The total path including the name is:", path[0] + script
