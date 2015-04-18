import pygments

from pygments.lexers import guess_lexer, guess_lexer_for_filename

def main():
    print("Hello world")

    file_text = ""

    for line in open("examples/admin_user.rb"):
        file_text += line

    print(guess_lexer_for_filename('admin_user.rb', file_text))
    #hello world 


if __name__=='__main__':
    main()