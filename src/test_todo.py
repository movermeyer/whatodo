import pytest
from main import *

test_files = [  "examples/C/filenames/script", "examples/Clojure/index.cljs.hl", 
                "examples/Chapel/lulesh.chpl", "examples/Forth/core.fth", 
                "examples/GAP/Magic.gd", "examples/JavaScript/steelseries-min.js",
                "examples/Matlab/FTLE_reg.m", "examples/Perl6/for.t",
                "examples/VimL/solarized.vim", "examples/C/cpu.c",
                "examples/CSS/bootstrap.css", "examples/D/mpq.d",
                "examples/Go/api.pb.go", "examples/HTML+ERB/index.html.erb"]

number_of_comments = [
    423,# examples/C/filenames/script
    13, # examples/Clojure/index.cljs.hl
    609,# examples/Chapel/lulesh.chpl
    0,  # examples/Forth/core.fth
    3,  # examples/GAP/Magic.gd 
    2,  # examples/JavaScript/steelseries-min.js
    6,  # examples/Matlab/FTLE_reg.m
    586,# examples/Perl6/for.t
    20, # examples/VimL/solarized.vim
    39, # examples/C/cpu.c
    680,# examples/CSS/bootstrap.css
    167,# examples/D/mpq.d 
    0,  # examples/Go/api.pb.go
    10  # examples/HTML+ERB/index.html.erb
]
def test_get_comment_tokens():
    from pygments.lexers.c_cpp import CLexer

    file_text_test = "int main(int argc, char[] argv){\n//This is a comment\n}\n"
    c_lexer = CLexer()

    results = []
    for comment in get_comment_tokens(file_text_test, c_lexer):
        results.append(comment)

    assert len(results) == 1
    assert results[0] == "//This is a comment\n"

def test_get_tokens_from_file():
    for index,file in enumerate(test_files, 0):
        result = get_tokens_from_file("../" + file)
        #print(index)
        print(file)
        assert number_of_comments[index] == len(result.keys())

