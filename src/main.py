import pygments
from pygments.token import *
from pygments.lexers import guess_lexer, guess_lexer_for_filename

import sys
import os
import argparse
from argparse import ArgumentParser

global_error_list = []

def parse_args():
    '''
    Argument Parsing Helper Function

    Setups and runs the arg parse library to parse the command line arguments for us.

    Returns
    -------
        Already populated set of arguments ready for the taking.
    '''
    app_description = """
        WHATODO - 
        Keeps track of your TODO tasks in code. This quick app will scan
        all the files provided and give give you the location and summary 
        of any pending tasks marked with TODO.
    """
    # make the parser
    parser = argparse.ArgumentParser(description = app_description)
    
    # take command line arguments and make array
    parser.add_argument('files', type=str, nargs = '+', help = "File for TODO checking")
    parser.add_argument('-k', '--keywords', type=str, nargs = '*', default=['TODO'], 
                        help = "Keywords for TODO items, case sensitive. Defaults to TODO")

    return parser.parse_args()

def get_tokens_from_file(filepath):
    # Read the file in
    file_text = ""

    # Check if filename is an actual valid file
    if os.path.isfile(filepath):
        with open(filepath) as file:
            for line in file:
                file_text += line
    else:
        global_error_list.append("ERROR: " + filepath + " is not a file. Can't process.")

    # Determine the lexer we need to use to understand this file
    lexer = None

    # TODO Determine the best way of figuring out the mimetype for certain files,
    #      right now we suck.. Like bad.
    try:
        lexer = guess_lexer(file_text)
    except Exception as e:
        lexer = guess_lexer_for_filename(filepath, file_text)
    finally:
        if lexer == None:
            global_error_list.append("ERROR:\tUnable to find a lexer\n\t\t\tCan't process " + str(filepath))
            return {}
    
    comments_with_lines = {}

    # Get the comment tokens
    for comment in get_comment_tokens(file_text, lexer):
        for num, line in enumerate(file_text.splitlines(), 1):
            # Eliminate issues with newlines as comments
            if len(comment.strip()) == 0:
                continue
            # Account for multi line comments, only take the comment line
            # since we want to give out where the comment starts
            first_comment_line = comment.splitlines()[0]

            if first_comment_line in line:
                comments_with_lines[num] = comment
    
    return comments_with_lines


def get_comment_tokens(file_text, lexer):
    '''
    Retrieves the set of tokens from the file

    Arguments
    ---------
        file_text : str
            Contains the file text that we are running the lexer through
        lexer : pygments.lexer
            The lexer to use for this file

    Yields
    ------
        comment : str
    '''
    for tokens in pygments.lex(file_text, lexer):
        if tokens[0] in Comment:
            #print(tokens)
            yield tokens[1]

def find_Keywords(comment, keywords):
	
	# constants
	array = []
	count = 0

	# loop through key words & split comment into lines
	for keyword in keywords:
		comment_line_by_line = comment.splitlines()

		# loop through the lines and for each word strip white space
		# see if the word in the comment matches keyword
		for comment_line in comment_line_by_line:
			comment_line = comment_line.lstrip()
			index_of_keyword = comment_line.find(keyword)

			# get the index of the matching word 
			# only use if the index is < 10 and > -1
			if index_of_keyword == -1:
				continue
			else:
				if index_of_keyword < 10:
					print("GOT IT!")
				else:
					continue

def main():
    args = parse_args()

    file_names = args.files
    keywords = args.keywords
    
    #comment = "                     #TODO"
    #find_Keywords(comment, keywords)

    for file in file_names:
        print("*" * 60)
        print("File:\t" +  file)
        print("*" * 60)
        tokens_with_lines = get_tokens_from_file(file)
        for line_number in tokens_with_lines.keys():
            print(str(line_number) + " : '" + tokens_with_lines[line_number] + "'")


    for error in global_error_list:
        print(error)


if __name__=='__main__':
    main()