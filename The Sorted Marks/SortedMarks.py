import random

#This function simple generates a random list of marks depending on the size parametre.
def generateMarks(size):
    marks = []

    for i in range (size):
        mark = random.choice(range(0,101))
        marks.append(mark)

    return marks

"""
Here we wil look at doing the same thing but with a sorted list of marks.
This tells us two things of a certainty:
    1. We can easily determine the values of our low and high marks. Depending
    on the order of the sorted list we can say that our low and high will be
    at the extremes of our list.
    
    As an example: sortedMarks = [89, 85, 60, 45, 30, 20, 12]

    The sortedMarks list above is in a descending order and we can clearly see
    that the high and low values are at the ends of our list. Similarly in a 
    case where the list is in an ascending order, the same will be true. 

    Lets us see how we can code this solution out. First we will start with our 
    generate marks function from the previous unsorted method.
"""

def sortMarks(size):
    #The randomly generated marks are stored in the variable marks
    marks = generateMarks(size)

    #This variable denotes the current position we are considering
    currentMarkPosition = 0

    #We make sure that we do not exceed the length of our list of marks
    while currentMarkPosition < len(marks) - 1:
        #We assume the first element is sorted and try to see where the next element fits in relation to the first
        currentMarkPosition += 1
        #The mark at the current position is then made the current mark we are considering
        currentMark = marks[currentMarkPosition]
        #The pointer is assigned the same position as the current mark
        pointer = currentMarkPosition
        
        #We make sure our pointer isn't zero and the current mark is less than the previous mark
        while pointer > 0 and currentMark < marks[pointer - 1]:
            #If the above condition holds, the mark at the pointer is replaced with the previous mark
            marks[pointer] = marks[pointer - 1]
            #Here we reduce the pointer and go through the loop again
            pointer = pointer - 1
        #If the condition doesn't hold the mark at the pointer remains in it's position
        marks[pointer] = currentMark
    return marks

# sortMarks(10)