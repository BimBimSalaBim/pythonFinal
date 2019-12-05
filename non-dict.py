
className = ''
classRoom = ''
studentList = {}
testList = []
isSorted = False
fileName = ''

def get_LetterGrade(grade):
    if grade == '-1':
        return 'I'
    if grade > 90:
        return 'A'
    elif grade < 90 and grade > 80:
        return 'B'
    elif grade < 80 and grade > 70:
        return 'C'
    elif grade < 70 and grade > 60:
        return 'D'
    else:
        return 'F'
def getLowest(i):
    #finds the lowest score of the tests
    tempScore = studentList[i][3][0]
    for x in studentList[i][3]:
        if int(x) < tempScore:
            tempScore = int(x)
    return tempScore
def get_grade(i):
    lowest = getLowest(i)
    #make sure that the grade is valid
    if studentList[i][2] < 0:
        return '-1'
    testTotal = 0
    #add all the scores togeather and subtract the lowest one
    for x in studentList[i][3]:
        if x < 0:
            return '-1'
        testTotal += int(x)
    #calculate the grade based off the scale
    testTotal -= lowest
    testTotal = testTotal/(len(studentList[i][3])-1)
    total = (testTotal*.9)+((studentList[i][2])* .1)
    return round(total,2)



def sortState():
    list = studentList
    if isSorted == True:
        list = sorted(studentList, key=lambda x: x.lower())
    return list

def reportPrint():
    #SortList(students)
    #detailed report print for each student
    print('CourseName:',className,end='')
    classId = className.split(' ')
    print('ID:',(' '.join(classId[-2:])))
    print('ClassLocation:', classRoom,end='')
    print('\nName\t\t\tID\t\t\tAverage\t\tGrade\n')
    for i in sortState():
        if studentList[i][0] != ' ':
            tab = '\t\t'
            if len(studentList[i][0]) > 15:
                tab = '\t'
            if len(studentList[i][0]) < 8:
                tab = '\t\t\t'
            grade = get_grade(i)
            print('{}'.format(studentList[i][0])+tab+'{}\t\t{}\t\t{}'.format(studentList[i][1],grade,get_LetterGrade(grade)))


def printList():
    #SortList(students)
    #basic formated print
    print('\nName\t\t\tAverage\t\tGrade\n')
    list = studentList
    for i in sortState():
        if studentList[i][0] != ' ':
            tab = '\t\t'
            if len(studentList[i][0]) > 15:
                tab = '\t'
            if len(studentList[i][0]) < 8:
                tab = '\t\t\t'
            grade = get_grade(i)
            print('{}'.format(studentList[i][0])+tab+'{}\t\t{}'.format(grade,get_LetterGrade(grade)))



def saveReport():
    #set the basic vars
    line1 = str('CourseName: '+className)
    courseId = className.split(" ")[-2:]
    line2 = str('ID: '+' '.join(courseId))
    line3 = str('ClassLocation: '+ classRoom)
    try:
        #try to create a file
        outputName = input('What do you want the name of the file to be?\n')
        outputFile = open(outputName,'w')
    except:
        print('Invalid name please try again')
        saveReport(students,className,classRoom)
    #write the basic vars to the file
    outputFile.write(line1)
    outputFile.write(line2)
    outputFile.write(line3)
    outputFile.write("\n%-25s%-15s %-15s %-25s\n\n"%('Name','ID','Average','Grade'))
    avg = 0
    k = 0
    #write all the Students line by line
    list = studentList
    for i in sortState():
        if studentList[i][0] != ' ':
            tab = '\t\t\t\t'
            studentId = '***-**-'+str(studentList[i][1])[-4:]
            if len(studentList[i][0]) > 15:
                tab = '\t'
            line5 = "%-25s%-15s %-15.0f %-25s\n"%(studentList[i][0],studentId,float(get_grade(i)),get_LetterGrade(get_grade(i)))
            if get_grade(i) != '-1':
                k += 1
                avg += float(get_grade(i))
                line5 = "%-25s%-15s %-15.2f %-25s\n"%(studentList[i][0],studentId,float(get_grade(i)),get_LetterGrade(get_grade(i)))

            outputFile.write(str(line5))
    #write the avg scores
    avg = round((avg/k),2)
    last = '\nClass Average for '+str(k) +' student(s): '+str(avg)
    outputFile.write(str(last))
    outputFile.close()

def editScores():
    try:
        name = input('What is the last name of the student you want to edit?\n')
    except:
        print('Invalid entry, please try again')
        editScores()
    #go through the list of students and see if the names match
    for x in sortState():
        if name.strip().lower() == x.lower():
            i = 1
            #print the scores so the user knows what to update and what the prev values are
            print(str(i)+'- Quiz 1:',studentList[x][2])
            for score in studentList[x][3]:
                i += 1
                print(str(i)+'- Test '+str(i-1),score)
            print(str(8)+'- Quit')
            #ask user which score they want to update
            try:
                scoreToEdit = int(input('which score would you like to edit? Enter \'q\' to go back.\n'))
            except:
                print('Invalid choice please try again')
                editScores()
            if scoreToEdit == 8:
                break
            elif scoreToEdit > 0 and scoreToEdit < 8:
                try:
                    #update the score in the student class
                    if scoreToEdit == 1:
                        studentList[x][2] =( int(input('What is the updated value?\n')))
                    else:
                        studentList[x][3][scoreToEdit-2] = int(input('What is the updated value?\n'))
                except:
                    print('Invalid please try again')
                    editScores()
                print('Score has been updated')
                break
            else:
                print('Invalid choice please try again')
                editScores()
    if name == 'q':
        return
    #update the score in the file
    writeFile()

def inList(name):
    #check if the student is in the list
    for i in studentList:
        if name.strip().lower() == i.strip().lower():
            return True
    return False

def printStudent():
    try:
        name = input('What is the last name of the student you want to view? Enter \'q\' to go back.\n')
    except:
        print('Invalid entry, please try again')
        printStudent()
    if name == 'q':
        return
    found = False
    for x in studentList:
        #find the student in the list and print the information
        if name.strip().lower() == x.strip().lower():
            print("\n%-25s%-15s %-15s %-25s\n"%('Name','ID','Average','Grade'))
            print("%-25s%-15s %-15.0f %-25s\n"%(studentList[x][0],studentList[x][1],float(get_grade(x)),get_LetterGrade(get_grade(x))))
            i = 1
            print(' Quiz 1:',studentList[x][2])
            for score in studentList[x][3]:
                i += 1
                print(' Test '+str(i-1)+':',score)
            found = True
            break
    if not found:
        print('There is no student with that name, please try again.')
        printStudent()


def addStudent():
    name = input('What is the full name of the student? Press \'q\' to return.\n')
    if name == 'q':
        return
    name = name.split(' ',1)
    try:
        #make sure it is a valid entry
        if len(name[1]) < 1:
            raise Exception('Invalid entry, please try again')
        #first check if the last name if in the list or not
        if not inList(name[1]):
            #if not in the list then ask the user for all the other information and add it accordingly
            id = int(input('What is the ID of the student?\n'))
            quiz = (int(input('What is the quiz Score for '+name[0]+'?\n')))
            testscores = []
            for i in range(6):
                print('What is the Score for test '+str(i+1)+'?\n')
                score = int(input())
                testscores.append(score)
            studentList[str(name[1])] = [' '.join(name),id,quiz,testscores]
            print(' '.join(name),'has been added to the list.')
        else:
            print("Last name already in report, please try again or press 'q' to return.")
            addStudent()
    except:
        print('Invalid entry, please try again 1')
        addStudent()
    #save the new student to the existing file
    writeFile()

def removeStudent():
    name = input('What is the last name of the student?\n')
    isInList = False
    #check if the name is in the students list
    for i in sortState():
        if name.strip().lower() == i.strip().lower():
            #if it is then delete it and stop the loop
            del studentList[i]
            isInList = True
            break
    if isInList:
        print(name,'has been removed')
        writeFile()
    else:
        print(name,'is not in the list')

def writeFile():
    #open the file with write and append premissions
    outputFile = open(fileName,'w+')
    #write the first 2 lines
    outputFile.write(className)
    outputFile.write(classRoom)
    #write all the other lines (students)
    for i in sortState():
        if studentList[i][0] != ' ':
            tab = '\t\t'
            if len(studentList[i][0]) > 15:
                tab = '\t'
            outputFile.writelines(str(studentList[i][0])+'\n')
            line = str(studentList[i][1])+' '+ str(studentList[i][2])+' '+str(studentList[i][3][0])+' '+str(studentList[i][3][1])+' '+str(studentList[i][3][2])+' '+str(studentList[i][3][3])+' '+str(studentList[i][3][4])+' '+str(studentList[i][3][5])+'\n'
            outputFile.writelines(line)

    outputFile.close()
def fileImport():
    ## vars used for return
    inputFileOK = False
    students = []
    global className
    global classRoom
    global fileName
    prevLine = ''

    i = 0
    ## check if the file exists
    while (inputFileOK == False):
        try:
            inputFileName = input("Enter name of input file: ")
            inputFile = open(inputFileName, "r")
        ##if can't open file
        except IOError:
            print("File", inputFileName, "could not be opened\n")
        else:
            try:
                fileName = inputFileName
                studentFirst = ''
                studentLast = ''
                studentId = 0
                quiz = 0
                tests = []
                print("Opening file", inputFileName, " for reading.\n")
                inputFileOK = True
                #read all the line and then put the values in the proper objects
                for line in inputFile:
                    # if it is the first line then that is the name of the class
                    if prevLine == '':
                        className = line
                    #if it is the second line then it is the class room location
                    elif prevLine == className:
                        classRoom = line
                    ## if there are no numbers in the line then it is the name of the student
                    elif not any(char.isdigit() for char in line.strip()):
                        string = line.split(' ',1)
                        studentFirst = string[0]
                        studentLast = string[1]
                        #students.append(Student(string[0],string[1]))
                        i +=1
                    else:
                        #anything else is the values for the student
                        tempLine = line
                        id,quiz = line.split(' ',1)
                        studentId = id
                        if quiz.split(" ")[0].isdigit():
                            quiz = (int(quiz.split(" ")[0]))
                        score = tempLine.split(" ",2)[2]
                        score = score.split(" ")
                        tests = []
                        for x in score:
                            if x != '':
                                tests.append(int(x))
                    if prevLine != '':
                        fullName = studentFirst +' '+ studentLast[:-1]
                        list = [fullName,studentId,quiz,tests]
                        studentList[studentLast[:-1]] =list
                    prevLine = line

            except:
                print('Somthing went wrong with the file, please try a different file.')
                inputFile.close()
                fileImport()
            inputFile.close()
            #SortList(students)
            #if the file is empty then ask user for a new file
            if (className == '' or classRoom == ''):
                print('Invalid File, Try again')
                fileImport()
            return students,className,classRoom,inputFileName

def menu():
    print('\n------------------------------\n1: Print Report\n2: Print Student List\n3: View Student\n4: Save Report to File\n5: Edit Scores\n6: Add Student\n7: Sort Students\n8: Remove Student\n9: Quit\n------------------------------')
    return (int(input('What would you like to do?\n')))

def main():
    ##main loop making all the call
    students = fileImport()
    input = 0
    while input != 9:
        input = menu()
        if input == 1:
            reportPrint()
        elif input == 2:
            printList()
        elif input == 3:
            printStudent()
        elif input == 4:
            saveReport()
        elif input == 5:
            editScores()
        elif input == 6:
            addStudent()
        elif input == 7:
            global isSorted
            isSorted = True
            writeFile()
            printList()
        elif input == 8:
            removeStudent()
        elif input == 9:
            break
        else:
            menu()
if __name__ == '__main__':
    main()
