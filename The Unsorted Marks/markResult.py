from evaluateMarks import evaluateMarks

def markResult(size):
    #Calls the evaluate mark function
    evaluateMark = evaluateMarks(size)
    #These variables are assigned to a specific value that the above function returns 
    marks = evaluateMark[0]
    totalMarks = evaluateMark[1]
    lowMark = evaluateMark[2]
    highMark = evaluateMark[3]
    #This saves the marks below the average  
    belowAverage = []
    #This checks that our list of marks is not empty
    if len(marks) > 0:
        #Determines the value of the average mark
        averageMark = totalMarks/len(marks)
        #Loops through our list of marks
        for mark in marks:
            #Checks if any mark in the list is below average
            if mark < averageMark:
                #Adds any mark found to be below the average to the belowAverage list
                belowAverage.append(mark)
        print(totalMarks, lowMark, highMark, averageMark, belowAverage)


markResult(10)