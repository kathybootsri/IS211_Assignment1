# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:27:35 2020

@author: kbootsri
"""

"""Part 2: Define class and display function"""
class Book:
    def __init__(self, author, title):
        self.a = author
        self.t = title
        
OfMineMen = Book("John Steinbeck", "Of Mice and Men")
ToKillMock = Book("Harper Lee", "To Kill a Mickingbird")

def display(Book):
    print(Book.t + ", written by " + Book.a)
    
"""Part 2: Sample Output of display function"""
display(OfMineMen)
display(ToKillMock)