import sys
import re

def find(word):
	# pattern contains the regular expression used to match words in the file
	pattern = '(^'+word

	for i in range(0, len(word)+1):
		# this line considers the word formed by removing one character from the original word
		pattern += '$|^'+word[0:i]+word[i+1:len(word)]

		
		for j in range(65,91):
			# this line considers words formed by adding each character from A to Z, one by one, in the original word
			pattern += '$|^'+word[0:i]+chr(j)+word[i:len(word)]
			# this line considers words formed by replacing each character in the original word by every character from A to Z, one by one
			pattern += '$|^'+word[0:i]+chr(j)+word[i+1:len(word)]
	
	pattern += '$)'

	# this array contains the list of words that matched with the regex pattern
	list = []

	# matching the regex pattern with the file
	with open('sowpods.txt') as file:
		list = re.findall(pattern,file.read(),re.MULTILINE)

	if len(list)==0:
		print "No words found."
	else:
		print 'Similar Meaningful Words : '
		for simewo in list:
			print simewo

if __name__ == '__main__':
	if(len(sys.argv)!=2):
		print "Invalid syntax."
		print "Usage : simewo.py <word>"
	else:
		# find is called only if exactly one word is provided as input
		find(sys.argv[1].upper())