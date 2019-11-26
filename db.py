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
    def get_gradeAverage(self):
        lowest = getLowest(self,self.scores)
        if not self.isValid:
            return -1
        return lowest
    def get_grade(self):
        lowest = int(getLowest(self,self.scores))
        #check if there is an invalid grade
        if not self.isValid:
            return 'I'
        testTotal = 0
        for x in self.scores:
            testTotal += int(x)
        testTotal -= lowest
        testTotal = testTotal/(len(self.scores)-1)
        total = (testTotal*.9)+((self.quiz)* .1)
        return total
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
    print('CourseName:',className,end='')
    print('ID:',className[-8:],end='')
    print('ClassLocation:', classRoom,end='')
    print('\nName\t\t\tID\t\t\tAverage\t\tGrade\n')
    for i in range(len(students)):
        tab = '\t\t'
        if len(students[i].fullName) > 15:
            tab = '\t'
        print('{}'.format(students[i].fullName)+tab+'{}\t\t{}\t\t{}'.format(students[i].id,students[i].get_gradeAverage(),students[i].get_LetterGrade()))
def printList(students):
    print('\nName\t\t\tAverage\t\tGrade\n')
    for i in range(len(students)):
        tab = '\t\t'
        if len(students[i].fullName) > 15:
            tab = '\t'
        print('{}'.format(students[i].fullName)+tab+'{}\t\t{}'.format(students[i].get_gradeAverage(),students[i].get_LetterGrade()))

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
    outputName = input('What do you want the name of the file to be?\n')
    outputFile = open(outputName,'w')
    outputFile.write(reportPrint(students,className,classRoom))
    outputFile.close()

# def printEmpList(outputFile,empList):
#     outputFile.write("%-25s%-15s%-15s\n"%("Name","Job","Income"))
#     outputFile.write("%-55s\n" %(55*'-'))
#     for index in range(len(empList)):
#                print("%-2dName: %-25sJob: %-15sIncome $%-15.2f"
#                     %(index, empList[index]['Name'],empList[index]['Title'],empList[index]['salary']))
#                outputFile.write("%-25s%-15s $%-15.2f\n" %
#                                 (empList[index]['Name'],empList[index]['Title'],empList[index]['salary']))
#     return
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
            return students,className,classRoom

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
            editScores()
        elif input == 5:
            addStudent()
if __name__ == '__main__':
    main()
