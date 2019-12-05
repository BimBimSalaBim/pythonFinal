#class of students that holds all the information per student
class Student:
    #init student vars
    def __init__(self, firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName +' '+ lastName[:-1]
        self.id = 0
        self.scores = []
        self.quiz = 0
    #setter methods for calss
    def add_quiz(self, quiz):
        self.quiz = quiz
    def add_score(self, score):
        self.scores.append(score)
    #getter methods for class
    def getLowest(self,scores):
        #finds the lowest score of the tests
        tempScore = int(scores[0])
        for x in scores:
            if int(x) < tempScore:
                tempScore = int(x)
        return tempScore
    def get_grade(self):
        lowest = int(self.getLowest(self.scores))
        #make sure that the grade is valid
        if self.quiz < 0:
            return '-1'
        testTotal = 0
        #add all the scores togeather and subtract the lowest one
        for x in self.scores:
            if x < 0:
                return '-1'
            testTotal += int(x)
        #calculate the grade based off the scale
        testTotal -= lowest
        testTotal = testTotal/(len(self.scores)-1)
        total = (testTotal*.9)+((self.quiz)* .1)
        return round(total,2)
    def get_LetterGrade(self):
        grade = self.get_grade()
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

#output of all the students and their grades
def reportPrint(students,className,classRoom):
    #detailed report print for each student
    print('CourseName:',className,end='')
    classId = className.split(' ')
    print('ID:',(' '.join(classId[-2:])))
    print('ClassLocation:', classRoom,end='')
    print('\nName\t\t\tID\t\t\tAverage\t\tGrade\n')
    for i in range(len(students)):
        tab = '\t\t'
        if len(students[i].fullName) > 15:
            tab = '\t'
        if len(students[i].fullName) < 8:
            tab = '\t\t\t'
        print('{}'.format(students[i].fullName)+tab+'{}\t\t{}\t\t{}'.format(students[i].id,students[i].get_grade(),students[i].get_LetterGrade()))

def printList(students):
    #basic formated print
    print('\nName\t\t\tAverage\t\tGrade\n')
    for i in range(len(students)):
        tab = '\t\t'
        if len(students[i].fullName) > 15:
            tab = '\t'
        if len(students[i].fullName) < 8:
            tab = '\t\t\t'
        print('{}'.format(students[i].fullName)+tab+'{}\t\t{}'.format(students[i].get_grade(),students[i].get_LetterGrade()))

def SortList(students):
    Sorted = False
    size = len(students)
    while not Sorted:
        Sorted = True
        size -= 1 ;
        for i in range(size):
                     #if the prev name is bigger than the next then swap
                     if students[i].lastName.lower() > students[i+1].lastName.lower():
                         temp = students[i]
                         students[i] = students[i+1]
                         students[i+1] = temp
                         Sorted = False

def saveReport(students,className,classRoom):
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
    for i in range(len(students)):
        tab = '\t\t\t\t'
        studentId = '***-**-'+str(students[i].id[-4:])
        if len(students[i].fullName) > 15:
            tab = '\t'
        line5 = "%-25s%-15s %-15.0f %-25s\n"%(students[i].fullName,studentId,float(students[i].get_grade()),students[i].get_LetterGrade())
        if students[i].get_grade() != '-1':
            k += 1
            avg += float(students[i].get_grade())
            line5 = "%-25s%-15s %-15.2f %-25s\n"%(students[i].fullName,studentId,float(students[i].get_grade()),students[i].get_LetterGrade())

        outputFile.write(str(line5))
    #write the avg scores
    avg = round((avg/k),2)
    last = '\nClass Average for '+str(k) +' student(s): '+str(avg)
    outputFile.write(str(last))
    outputFile.close()

def editScores(students):
    try:
        name = input('What is the last name of the student you want to edit?\n')
    except:
        print('Invalid entry, please try again')
        editScores(students)
    #go through the list of students and see if the names match
    for x in students[0]:
        if name.strip().lower() == x.lastName.strip().lower():
            i = 1
            #print the scores so the user knows what to update and what the prev values are
            print(str(i)+'- Quiz 1:',x.quiz)
            for score in x.scores:
                i += 1
                print(str(i)+'- Test '+str(i-1),score)
            print(str(8)+'- Quit')
            #ask user which score they want to update
            try:
                scoreToEdit = int(input('which score would you like to edit? Enter \'q\' to go back.\n'))
            except:
                print('Invalid choice please try again')
                editScores(students)
            if scoreToEdit == 8:
                break
            elif scoreToEdit > 0 and scoreToEdit < 8:
                try:
                    #update the score in the student class
                    if scoreToEdit == 1:
                        x.add_quiz( int(input('What is the updated value?\n')))
                    else:
                        x.scores[scoreToEdit-2] = int(input('What is the updated value?\n'))
                except:
                    print('Invalid please try again')
                    editScores(students)
                print('Score has been updated')
                break
            else:
                print('Invalid choice please try again')
                editScores(students)
    if name == 'q':
        return
    #update the score in the file
    writeFile(students)

def inList(name,students):
    #check if the student is in the list
    for i in range(len(students)):
        if name.strip() == students[i].lastName.strip():
            return True
    return False

def printStudent(students):
    try:
        name = input('What is the last name of the student you want to view? Enter \'q\' to go back.\n')
    except:
        print('Invalid entry, please try again')
        printStudent(students)
    for x in range(len(students)):
        #find the student in the list and print the information
        if name.strip().lower() == students[x].lastName.strip().lower():
            print("\n%-25s%-15s %-15s %-25s\n"%('Name','ID','Average','Grade'))
            print("%-25s%-15s %-15.0f %-25s\n"%(students[x].fullName,students[x].id,float(students[x].get_grade()),students[x].get_LetterGrade()))
            i = 1
            print(' Quiz 1:',students[x].quiz)
            for score in students[x].scores:
                i += 1
                print(' Test '+str(i-1),score)
            break
    if name == 'q':
        return
    else:
        print('Invalid choice please try again')
        printStudent(students)

def addStudent(students):
    name = input('What is the name of the student? Press \'q\' to return.\n')
    if name == 'q':
        return
    name = name.split(' ',1)
    try:
        #make sure it is a valid entry
        if len(name[1]) < 1:
            raise Exception('Invalid entry, please try again')
        #first check if the last name if in the list or not
        if not inList(name[1],students[0]):
            #if not in the list then ask the user for all the other information and add it accordingly
            id = int(input('What is the ID of the student?\n'))
            students[0].append(Student(name[0],(name[1]+' ')))
            print('What is the quiz Score for '+name[0]+'?\n')
            students[0][-1].id = id
            students[0][-1].add_quiz(int(input()))
            for i in range(6):
                print('What is the Score for test '+str(i+1)+'?\n')
                students[0][-1].add_score(int(input()))
        else:
            print("Last name already in report, please try again or press 'q' to return.")
            addStudent(students)
    except:
        print('Invalid entry, please try again')
        addStudent(students)
    #save the new student to the existing file
    writeFile(students)

def removeStudent(students):
    name = input('What is the last name of the student?\n')
    isInList = False
    #check if the name is in the students list
    for i in range(len(students)):
        if name.strip() == students[i].lastName.strip():
            #if it is then delete it and stop the loop
            students.remove(students[i])
            isInList = True
            break
    if isInList:
        print(name,'has been removed')
    else:
        print(name,'is not in the list')

def writeFile(students):
    #open the file with write and append premissions
    outputFile = open(students[-1],'w+')
    #write the first 2 lines
    outputFile.write(students[1])
    outputFile.write(students[2])
    #write all the other lines (students)
    for i in range(len(students[0])):
        tab = '\t\t'
        if len(students[0][i].fullName) > 15:
            tab = '\t'
        outputFile.writelines(str(students[0][i].fullName)+'\n')
        line = str(students[0][i].id)+' '+ str(students[0][i].quiz)+' '+str(students[0][i].scores[0])+' '+str(students[0][i].scores[1])+' '+str(students[0][i].scores[2])+' '+str(students[0][i].scores[3])+' '+str(students[0][i].scores[4])+' '+str(students[0][i].scores[5])+'\n'
        outputFile.writelines(line)

    outputFile.close()

def fileImport():
    ## vars used for return
    inputFileOK = False
    students = []
    className = ''
    classRoom = ''
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
                        students.append(Student(string[0],string[1]))
                        i +=1
                    else:
                        #anything else is the values for the student
                        tempLine = line
                        id,quiz = line.split(' ',1)
                        students[i-1].id = id
                        if quiz.split(" ")[0].isdigit():
                            students[i-1].add_quiz(int(quiz.split(" ")[0]))
                        score = tempLine.split(" ",2)[2]
                        score = score.split(" ")
                        for x in score:
                            if x != '':
                                students[i-1].add_score(int(x))
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
            reportPrint(students[0],students[1],students[2])
        elif input == 2:
            printList(students[0])
        elif input == 3:
            printStudent(students[0])
        elif input == 4:
            saveReport(students[0],students[1],students[2])
        elif input == 5:
            editScores(students)
        elif input == 6:
            addStudent(students)
        elif input == 7:
            SortList(students[0])
            printList(students[0])
        elif input == 8:
            removeStudent(students[0])
        elif input == 9:
            break
        else:
            menu()
if __name__ == '__main__':
    main()
