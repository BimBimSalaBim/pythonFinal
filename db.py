class Student:

    def __init__(self, firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName + lastName
        self.id = 0
        self.scores = 0
        self.quiz = 0

    def add_quiz(self, quiz):
        self.quiz = quiz
    def add_scores(self, score):
        self.score.append(trick)
    def get_gradeAverage(self):
        return self.quiz


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
            if not any(char.isdigit() for char in line):
                string = line.split(' ',1)
                students.append(Student(string[0],string[1]))

        inputFile.close()

    finally:
        print(students[0].firstName)
