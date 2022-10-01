#!/usr/bin/env python3

string = input("Enter string: ")


def brackets_validator(string):

    if (
        string.count("(") == string.count(")")
        and string.count("[") == string.count("]")
        and string.count("{") == string.count("}")
    ):
        return True
    else:
        return False


print(brackets_validator(string))
