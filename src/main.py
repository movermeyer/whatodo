import pygments
from pygments.token import *
from pygments.lexers import guess_lexer, guess_lexer_for_filename

import sys
import argparse
from argparse import ArgumentParser

def parse_args():

    # make the parser
    parser = argparse.ArgumentParser(description = "Make array of files")
    
    # take command line arguments and make array
    parser.add_argument('--files', nargs = '*', help = "File names for the array")
    parser.add_argument('--keywords', type=str, nargs = '+', default='TODO', help = "Keywords to search for todo items")

    return parser.parse_args()

def get_tokens_from_file(filepath):
    # Read the file in
    file_text = ""

    with open(filepath) as file:
        for line in file:
            file_text += line

    # Determine the lexer we need to use to understand this file
    lexer = None

    try:
        lexer = guess_lexer(file_text)
    except Exception as e:
        lexer = guess_lexer_for_filename(filepath, file_text)
    finally:
        if lexer == None:
            print("ERROR: Unable to find a lexer")
            print("       Can't process " + str(filepath))
            return []

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


def main():
    args = parse_args()
    print(args)

    file_names = args.files

    keywords = args.keywords


    '''
    for file in file_names:
        tokens_with_lines = get_tokens_from_file(file)
        print("*" * 60)
        print("File:\t" +  file)
        print("*" * 60)
        for line_number in tokens_with_lines.keys():
            print(str(line_number) + " : '" + tokens_with_lines[line_number] + "'")
    '''

if __name__=='__main__':
    main()