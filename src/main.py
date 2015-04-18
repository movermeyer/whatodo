import pygments
from pygments.token import *

from pygments.lexers import guess_lexer, guess_lexer_for_filename

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
            # This should make sure to catch the multiline comments,
            # instead of doing ==
            #print(str(num) + " : " + line)

            # Account for multi line comments, only take the comment line
            # since we want to give out where the comment starts
            first_comment_line = comment.splitlines()[0]

            # Get the index for the start of the first comment,
            # this will help account for indentation, inline comments
            # and others
            if first_comment_line in line:
                #print(str(num) + " : " + comment)
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
            yield tokens[1]



def main():

    file_names = ["examples/ruby_example.rb", "examples/ruby_example"]

    for file in file_names:
        tokens_with_lines = get_tokens_from_file(file)
        print("*" * 60)
        print("File:\t" +  file)
        print("*" * 60)
        for line_number in tokens_with_lines.keys():
            print(str(line_number) + " : " + tokens_with_lines[line_number])

    #get_tokens_from_file("examples/ruby_example.rb")
    '''
    for tokens in get_tokens_from_file("examples/ruby_example.rb"):
        print(tokens)
    '''

if __name__=='__main__':
    main()