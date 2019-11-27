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
    def get_grade(self):
        lowest = int(getLowest(self,self.scores))
        if self.quiz < 0:
            return '-1'
        testTotal = 0
        for x in self.scores:
            if x < 0:
                return '-1'
            testTotal += int(x)
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

def getLowest(self,scores):
    tempScore = int(scores[0])
    for x in scores:
        if int(x) < tempScore:
            tempScore = int(x)
    return tempScore

def reportPrint(students,className,classRoom):
    SortList(students)
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
    courseId = className.split(" ")[-2:]
    line2 = str('ID: '+' '.join(courseId))
    line3 = str('ClassLocation: '+ classRoom)
    try:
        outputName = input('What do you want the name of the file to be?\n')
        outputFile = open(outputName,'w')
    except:
        print('Invalid name please try again')
        saveReport(students,className,classRoom)
    outputFile.write(line1)
    outputFile.write(line2)
    outputFile.write(line3)
    outputFile.write("\n%-25s%-15s %-15s %-25s\n\n"%('Name','ID','Average','Grade'))
    avg = 0
    k = 0
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

    for x in students[0]:
        if name.strip().lower() == x.lastName.strip().lower():
            i = 1
            print(str(i)+'- Quiz 1:',x.quiz)
            for score in x.scores:
                i += 1
                print(str(i)+'- Test '+str(i-1),score)
            print(str(8)+'- Quit')
            try:
                scoreToEdit = int(input('which score would you like to edit? Enter \'q\' to go back.\n'))
            except:
                print('Invalid choice please try again')
                editScores(students)
            if scoreToEdit == 8:
                break
            elif scoreToEdit > 0 and scoreToEdit < 8:
                try:
                    if scoreToEdit == 1:
                        x.add_quiz( int(input('What is the updated value?\n')))
                    else:
                        x.scores[scoreToEdit-2] = int(input('What is the updated value?\n'))
                except:
                    print('Invalid choice please try again')
                    editScores(students)
                print('Score has been updated')
                return
            else:
                print('Invalid choice please try again')
                editScores(students)
    if name == 'q':
        return
    else:
        print('Invalid choice please try again')
        editScores(students)
    writeFile(students)

def printStudent(students):
    try:
        name = input('What is the last name of the student you want to view? Enter \'q\' to go back.\n')
    except:
        print('Invalid entry, please try again')
        editScores(students)
    for x in range(len(students)):
        if name.strip().lower() == students[x].lastName.strip().lower():
            print("\n%-25s%-15s %-15s %-25s\n"%('Name','ID','Average','Grade'))
            print("%-25s%-15s %-15.0f %-25s\n"%(students[x].fullName,students[x].id,float(students[x].get_grade()),students[x].get_LetterGrade()))
            i = 1
            print(' Quiz 1:',students[x].quiz)
            for score in students[x].scores:
                i += 1
                print(' Test '+str(i-1),score)

            return
    if name == 'q':
        return
    else:
        print('Invalid choice please try again')
        printStudent(students)

def addStudent(students):
    name = input('What is the name of the student?\n')
    name = name.split(' ',1)
    try:
        if len(name[1]) < 1:
            raise Exception('Invalid entry, please try again')
        id = int(input('What is the ID of the student?\n'))
        students[0].append(Student(name[0],(name[1]+' ')))
        print('What is the quiz Score for '+name[0]+'?\n')
        students[0][-1].id = id
        students[0][-1].add_quiz(int(input()))
        for i in range(6):
            print('What is the Score for test '+str(i+1)+'?\n')
            students[0][-1].add_score(int(input()))
    except:
        print('Invalid entry, please try again')
        addStudent(students)


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
    print('\n------------------------------\n1: Print Report\n2: Print Student List\n3: View Student\n4: Save Report to File\n5: Edit Scores\n6: Add Student\n7: Quit\n------------------------------')
    return (int(input('What would you like to do?\n')))

def main():
    students = fileImport()
    input = 0
    while input != 7:
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
        else:
            menu()
if __name__ == '__main__':
    main()
