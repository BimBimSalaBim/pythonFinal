class Student:

    def __init__(self, firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName + lastName
        self.id = 0
        self.scores = []
        self.quiz = 0

    def add_quiz(self, quiz):
        self.quiz = quiz
    def add_score(self, score):
        self.scores.append(score)
    def get_gradeAverage(self):
        return self.scores


def BubbleSort(dicList):
    Sorted = False;
    size = len(dicList);
    while not Sorted:
        Sorted = True ;
        size -= 1 ;
        for i in range(size):
            if dicList[i]['Name'] > dicList[i+1]['Name']:
                temp = dicList[i]
                dicList[i] = dicList[i+1]
                dicList[i+1] = temp
                Sorted = False
    return

def printEmpList(outputFile,empList):
    outputFile.write("%-25s%-15s%-15s\n"%("Name","Job","Income"))
    outputFile.write("%-55s\n" %(55*'-'))
    for index in range(len(empList)):
               print("%-2dName: %-25sJob: %-15sIncome $%-15.2f"
                    %(index, empList[index]['Name'],empList[index]['Title'],empList[index]['salary']))
               outputFile.write("%-25s%-15s $%-15.2f\n" %
                                (empList[index]['Name'],empList[index]['Title'],empList[index]['salary']))
    return

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
        print("File", inputFileName, "could not be opened")
    else:
        print("Opening file", inputFileName, " for reading.")
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
                score = []
                tempLine = line
                id,quiz = line.split(' ',1)
                students[i-1].id = id
                students[i-1].quiz = quiz
                score.append((tempLine.split(" ",2)[2]))
                print(score)
                for x in score:
                    students[i-1].add_score(x)
                #print(score)
            prevLine = line

        inputFile.close()

print(students[1].get_gradeAverage())
