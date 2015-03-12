"From sys import argv"

"script, user_name = argv "
"promit = '> '"

print "Hi %s, I'm the %s script."
print "I'd like to ask you a few questions."
print "Do you like me %s?"
likes = raw_input()

print "Where do you live %s?"
lives = raw_input()

print "What kind of computer do you have?"
computer = raw_input()

print ""
"Alright, so you said %r abut liking me."
"You live in %r. Not sure where that is."
"And you have a %r computer. Nice."
" % (likes, lives, computer)"  