#!/usr/bin/python
# -*- coding: utf-8 -*-
def reserve(text):
    return text[::-1]

def is_palindrome(text):
    return text == reserve(text)

something = input('Enter text:')
if (is_palindrome(something)):
    print("Yes,it is a palindrome.")
else:
    print("No,it is not a palindrome.")
