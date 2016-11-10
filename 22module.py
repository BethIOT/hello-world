"""This is not a script. Its a module of functions
this module can be used with other objects.
When calling this module, dont type '.py'
Also, this will be the first ?? that we 
handle on python prompt (not cmd) """

# These comments are not displayed in help().
# These are normal comments

"""These comments are also not displayed in help(),
even though these are documentation comments,
it is broken from the top"""

def break_words(data) :
	"""This function will break up words for us"""
	words=data.split(' ')
	return words

def sort_words (wrds):
	'''Sorts the words'''
	return sorted(wrds)

def print_first_word (wrds) :
	'''Prints the first word after popping it off'''
	wrd=wrds.pop(0)
	print wrd

def print_last_word (wrds) :
	'''Prints the last word after popping it off.'''
	wrd=wrds.pop(-1)
	print wrd

def sort_sentence(snt):
	'''Takes in a full sentence and returns the sorted words'''
	wrds=break_words(snt)
	return sort_words(wrds)

def print_first_last(snt):
	'''Prints the first and last words of a sentence'''
	wrds=break_words(snt)
	print_first_word(wrds)
	print_last_word(wrds)

def print_first_last_sorted(snt):
	wrds=sort_sentence(snt)
	print_first_word(wrds)
	print_last_word(wrds)


''' Instructions to handle module :

1.Enter python promt
	<path>./python.exe
	>>>_

2.Import this module
	>>>import '22module'
Make sure you dont type '.py'; you will get error msg
This statement creates a new file called "22module.pyc"
pyc=Python Bytecode. If you delete it, it will just be created again

3.Create an object to work on
	sentence = "The bigger they are, the harder they fall"

4.Run break_words function
	>>>words = 22module.break_words(sentence)
	>>>words
observe the return. another way to execute this is
	>>>print 22module.break_words(sentence)
22module
5.Run sort_words function
	>>>sorted_words= 22module.sort_words(words)
	>>>sorted_words

6.Run print_first_word function
	>>>22module.print_first_word(words)

7.Run print_last_word function
	>>>22module.print_last_word(words)

8.Run sort_sentence function
	>>>sorted_sentence=22module.sort_sentence(sentence)
	>>>sorted_sentence

9.Run print_first_last function
	>>>22module.print_first_last(sentence)

10.Run print_first_last_sorted function
	>>>22module.print_first_last_sorted(sentence)

To avoid typing '22module.' when calling each function,
you could import the entire 22module in the begining itself
	>>>from 22module import *
mind the space before the astrix

You could type up >>>help(22module) and you can see the comments
typed and  the explaination of functions.
You could >>>help(22module.sort_words) to get desription
of only that particular function
'''