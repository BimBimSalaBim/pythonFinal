class Student:
    #init student vars
    def __init__(self, firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName +' '+ lastName[:-1]
        self.id = 0
        self.scores = []
        self.quiz = 0
        self.isValid = True
    #setter methods for calss
    def add_quiz(self, quiz):
        self.quiz = quiz
    def add_score(self, score):
        self.scores.append(score)
    #getter methods for class
    def get_grade(self):
        lowest = int(getLowest(self,self.scores))
        #check if there is an invalid grade
        if not self.isValid:
            return '-1'
        testTotal = 0
        for x in self.scores:
            testTotal += int(x)
        testTotal -= lowest
        testTotal = testTotal/(len(self.scores)-1)
        total = (testTotal*.9)+((self.quiz)* .1)
        return round(total,2)
    def get_LetterGrade(self):
        grade = self.get_grade()
        if not self.isValid:
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

def getLowest(self,scores):
    tempScore = int(scores[0])
    for x in scores:
        if int(x) < tempScore:
            tempScore = int(x)
    if tempScore < 0:
        self.isValid = False
    return tempScore

def reportPrint(students,className,classRoom):
    SortList(students)
    print('CourseName:',className,end='')
    classId = className.split(' ')
    print('ID:',(''.join(classId[-2:])))
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
    SortList(students)
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
                     if students[i].lastName > students[i+1].lastName:
                         temp = students[i]
                         students[i] = students[i+1]
                         students[i+1] = temp
                         Sorted = False

def saveReport(students,className,classRoom):
    line1 = str('CourseName: '+className)
    line2 = str('ID: '+className[-8:])
    line3 = str('ClassLocation: '+ classRoom)
    outputName = input('What do you want the name of the file to be?\n')
    outputFile = open(outputName,'w')
    outputFile.write(line1)
    outputFile.write(line2)
    outputFile.write(line3)
    outputFile.write('\nName\t\t\tID\t\t\tAverage\t\tGrade\n')
    for i in range(len(students)):
        tab = '\t\t'
        if len(students[i].fullName) > 15:
            tab = '\t'
        line4 ='{}'.format(students[i].fullName)+tab+'{}\t\t{}\t\t{}\n'.format(students[i].id,students[i].get_grade(),students[i].get_LetterGrade())
        outputFile.write(str(line4))
    outputFile.close()

def editScores(students):
    name = input('What is the last name of the student you want to edit?\n')
    for x in students[0]:
        if name == x.lastName.strip():
            i = 1
            print(str(i)+'- Quiz 1:',x.quiz)
            for score in x.scores:
                i += 1
                print(str(i)+'- Test '+str(i-1),score)
            print(str(8)+'- Quit')
            scoreToEdit = int(input('which score would you like to edit?\n'))
            if scoreToEdit == 8:
                break
            if scoreToEdit > 0 and scoreToEdit < 8:
                if scoreToEdit == 1:
                    x.quiz = int(input('What is the updated value?\n'))
                else:
                    x.scores[scoreToEdit-2] = int(input('What is the updated value?\n'))
                print('Score has been updated')
            else:
                print('Invalid choice please try again')
                editScores(students)
    writeFile(students)

def addStudent(students):
    name = input('What is the name of the student?\n')
    name = name.split(' ')
    id = int(input('What is the ID of the student?\n'))
    students[0].append(Student(name[0],(name[1]+' ')))
    print('What is the quiz Score for '+name[0]+'?\n')
    students[0][-1].id = id
    students[0][-1].add_quiz(int(input()))
    for i in range(6):
        print('What is the Score for test '+str(i+1)+'?\n')
        students[0][-1].add_score(int(input()))
    writeFile(students)
def writeFile(students):
    outputFile = open(students[-1],'w+')
    outputFile.write(students[1])
    outputFile.write(students[2])
    for i in range(len(students[0])):
        tab = '\t\t'
        if len(students[0][i].fullName) > 15:
            tab = '\t'
        outputFile.writelines(str(students[0][i].fullName)+'\n')
        line = str(students[0][i].id)+' '+ str(students[0][i].quiz)+' '+str(students[0][i].scores[0])+' '+str(students[0][i].scores[1])+' '+str(students[0][i].scores[2])+' '+str(students[0][i].scores[3])+' '+str(students[0][i].scores[4])+' '+str(students[0][i].scores[5])+'\n'
        outputFile.writelines(line)

    outputFile.close()
def fileImport():
    inputFileOK = False
    students = []
    className = ''
    classRoom = ''
    prevLine = ''
    i = 0
    while (inputFileOK == False):
        try:
            inputFileName = input("Enter name of input file: ")
            inputFile = open(inputFileName, "r")

        except IOError:
            print("File", inputFileName, "could not be opened\n")
        else:
            print("Opening file", inputFileName, " for reading.\n")
            inputFileOK = True
            for line in inputFile:
                if prevLine == '':
                    className = line
                elif prevLine == className:
                    classRoom = line
                elif not any(char.isdigit() for char in line.strip()):
                    string = line.split(' ',1)
                    students.append(Student(string[0],string[1]))
                    i +=1
                else:
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

            inputFile.close()
            SortList(students)
            return students,className,classRoom,inputFileName

def menu():
    print('\n------------------------------\n1: Print Report\n2: Print Student List\n3: Save Report to File\n4: Edit Scores\n5: Add Student\n6: Quit\n------------------------------')
    return (int(input('What would you like to do?\n')))

def main():
    students = fileImport()
    input = 0
    while input != 6:
        input = menu()
        if input == 1:
            reportPrint(students[0],students[1],students[2])
        elif input == 2:
            printList(students[0])
        elif input == 3:
            saveReport(students[0],students[1],students[2])
        elif input == 4:
            editScores(students)
        elif input == 5:
            addStudent(students)
if __name__ == '__main__':
    main()
