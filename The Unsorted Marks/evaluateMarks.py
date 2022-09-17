from Marks import generateMarks

def evaluateMarks(size):
    #Calls the generateMarks function and stores its value in marks
    marks = generateMarks(size)
    # print(marks)
    totalMarks = 0
    lowMark = 100
    highMark = 0

    #Loops through the list of marks
    for mark in marks:
        #Adds the values to totalMarks
        totalMarks = mark + totalMarks
        #Checks if a mark is lower than the lowMark variable if it is, it is replaced 
        if mark < lowMark:
            lowMark = mark
        #Checks if a mark is higher than the highMark variable if it is, it is replaced 
        elif mark > highMark:
            highMark = mark
    return (marks, totalMarks, lowMark, highMark)

# evaluateMarks(10)