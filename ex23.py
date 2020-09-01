# Exercise 23: Strings, Bytes, and Character Encodings

# To do this exercise you'll need to download a text file that Zed wrote, named "languages.txt"
# (https://learnpythonthehardway.org/python3/languages.txt).  This file was created with a list
#   of human languages to demonstrate a few interesting concepts:
#   1.  How modern computers store human languages for display and processing and how python 3 
#           calls this "strings"
#   2.  How you must "encode" and "decode" Python's strings into a type called "bytes"
#   3.  How to handle errors in your string and byte handling
#   4.  How to read code and find out what it means even if you've never seen it before

#   In addition to that we will get a brief glimpse of the Python 3 if-statement and lists for
#       processing a list of things.

#               Initial Research

# The languages.txt file simply contains a list of human language names that are encoded in UTF-8

import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, error):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)