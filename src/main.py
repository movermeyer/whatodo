import pygments
from pygments.lexers import guess_lexer, guess_lexer_for_filename

import sys
import argparse
from argparse import ArgumentParser

def filesArray():
	# make the parser
	parser = argparse.ArgumentParser(description = "Make array of files")
	
	# take command line arguments and make array
	parser.add_argument('--files', nargs = '*',
						help = "File names for the array")
	print(parser.parse_args())
	#print(parser)

def main():
	filesArray()



'''
def main():
    print("Hello world")

    file_text = ""

    for line in open("examples/admin_user.rb"):
        file_text += line

    print(guess_lexer_for_filename('admin_user.rb', file_text))
    #hello world 
'''

if __name__=='__main__':
    main()