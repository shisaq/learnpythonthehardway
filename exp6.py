# 10 replaces %d
x = "There are %d types of people." % 10
# define 2 variables
binary = "binary"
do_not = "don't"
# make 2 vars to replace %s
y = "Those who know %s and those who %s" % (binary, do_not)

# print out x and y
print x
print y

# %r and %s.
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w= "This is the left side of..."
e = "a string with a right side."

print w + e
