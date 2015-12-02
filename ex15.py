# --coding: utf-8--

# import argv from sys
from sys import argv

# unpack argv
script, filename = argv

# open filename and assign the return value to txt
txt = open(filename)

print "Here's your file %r:" % filename
# read at most size bytes from txt, return as a string
print txt.read()

print "Type the filename again:"

# read a filename from standard input, and the prompt is ">"
file_again = raw_input("> ")

# open file_again and assign the return value to txt_again
txt_again = open(file_again)

# read at most size bytes from txt_again, and return as a string
print txt_again.read()

# close these two file
txt.close()
txt_again.close()
