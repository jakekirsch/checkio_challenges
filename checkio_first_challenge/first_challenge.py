# Define import modules
import sys
import re, string

# Defines a repeat function that prints out the argument 3 times
# and uses a conditional to add a smiley face
def checkio(text):
	# clean up source text
	cleantext = re.sub('[^a-zA-Z]+', '', text)
	cleantext = cleantext.lower()

	# now create a dictionary of the values that are present
	resultdict = dict(zip(set(cleantext), 
		[0] * len(set(cleantext))))

	# find counts of keys
	for key in cleantext:
		resultdict[key] = resultdict[key] + 1

	# now find the letter with the greatest value, tie goes to 
	# lower
	max_char = ''
	max_value = 0

	for key, value in resultdict.items():
		if resultdict[key] > max_value:
			max_char = key
			max_value = resultdict[key]
		elif resultdict[key] == max_value:
			if key < max_char:
				max_char = key
				max_value = resultdict[key]
	
	return max_char

# one of the better answers

def checkio_improved(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower() # I understand this - does a similar thing
    # string.ascii_lowercase - this is a constant?
    # max - returns largest value in an iterable, however key
    # is a one argument ordering function

    # which brings us to text.count, which seems that the default
    # value is to take substrings of 1?
    # print(lambda text.count)
    # to what I used
    return max(string.ascii_lowercase, 
    	# key = text.count
    	key = lambda x: text.count(x)
    	)

    # string.ascii_lowercase ??


    
# define main argument of this module, which calls the repeat 
# function
def main():
	# text = sys.argv[1]
	# smiley = args[2]

	print(checkio_improved("""asdfa;LKJL;KJL;KJLKJ
		;LKJ;LKJ;LJK
		sdf234230498 )98098)(*)(* 134240098a;lkjsd;lfkajd;flkj
		thisis ;ijasdf string"""))

	# print(checkio(string.printable))


# Standard boilerplate to call main function
if __name__ == '__main__':
	main()