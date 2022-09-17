from SortedMarks import sortMarks

def evaluateSortedMarks(size):

    #Calls the sortMarks function and stores its value in marks
    marks = sortMarks(size)
    lowMark = marks[0]
    highMark = marks[len(marks) - 1]
    totalMark = 0
    #Loops through the list of marks
    for mark in marks:
        #Adds the values to totalMark
        totalMark = mark + totalMark
    #Finds the average mark
    averageMark = totalMark/len(marks)
    #This stores the marks less than the average mark
    lessThanAverage = []
    #Loops through our marks and finds values less than the average
    for mark in marks:
        if mark < averageMark:
            lessThanAverage.append(mark)
    print (totalMark, lowMark, highMark, averageMark, lessThanAverage)

evaluateSortedMarks(10)