#!/usr/bin/python3
"""
module that has
a function that
print text
"""


def text_indentation(text):
    """
    function that look for chars and print new lines
    """
    l = ['.', '?', ':']
    i = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    while i < len(text):
        for j in l:
            if text[i] == j:
                print("{}".format(text[i]))
                print()
                i += 2
        print("{}".format(text[i]), end="")
        i += 1
