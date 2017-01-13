# -*- coding: utf-8 -*-
my_name = 'Haiquan Li'
my_age = 27
my_height = 182
my_weight = 71
my_eyes = 'Dark brown'
my_teeth = 'White'
my_hair = 'Black'

my_weight_pounds = my_weight * 2.20462
my_height_inches = my_height * 0.393701

print "Let's talk about %s." % my_name
print "He's %dcm tall." % my_height
print "换算成inch是%d inches" % my_height_inches
print "He's %dkg heavy." % my_weight
print "That's %d pounds actually." % my_weight_pounds
print "他体重真是完美！"
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usurally %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %r." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
