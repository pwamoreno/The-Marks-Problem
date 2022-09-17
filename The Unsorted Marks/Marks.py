import random

"""
Problem:
    Generate a program that inputs not more than 100 marks into an array. Then
    determines the lowest marks, highest marks, total marks, average marks, and
    number of marks below average and outputs each value.
    

Solution:
    In our case we will write a function to generate marks for a sample size. We
    will then use the generated list of marks to solve the problem. But a few 
    issues arise from using this method:
        1. The generated list of marks will likely be unordered or unsorted.
        2.An unordered or unsorted list of marks may be tedious to operate on
        for a very large sample size.

    We could use a brute force method of checking through our list of marks to
    determine the lowest and highest marks where in a sorted list we would know 
    that depending on the order, the lowest and highest marks are at the extremes
    of the list. So in this we would consider a sorted and unsorted list of marks.

Here we will consider the solution using an unsorted list of marks!
"""
#This function simple generates a random list of marks depending on the size parametre.
def generateMarks(size):
    marks = []

    for i in range (size):
        mark = random.choice(range(0,101))
        marks.append(mark)

    return marks

# generateMarks(10)