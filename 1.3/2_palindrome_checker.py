#!/usr/bin/env python3

print("Enter a string for palyndrome check:")
str = input()

str = str.replace(" ", "").lower()

if str == str[::-1]:
    print("Yes, this is a palindrome")
else:
    print("No, this is not a palindrome")
