#!/usr/bin/env python3

string1 = input("Enter string # 1: ")
string2 = input("Enter string # 2: ")


def bin_nums_multiply(string1, string2):
    return bin(int(string1, 2) * int(string2, 2))[2:]


print(bin_nums_multiply(string1, string2))
