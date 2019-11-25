class Student:

    def __init__(self, firstName,lastName id):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName + lastName
        self.id = id
        self.scores[]
        self.quiz

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
while (inputFileOK == False):
    try:
        inputFileName = input("Enter name of input file: ")
        inputFile = open(inputFileName, "r")

    except IOError:
        print("File", inputFileName, "could not be opened")
    else:
        print("Opening file", inputFileName, " for reading.")
        inputFileOK = True
        studnets = []
        for line in inputFile:
            students.append(student())
            if not any(char.isdigit() for char in line):
                firstName,lastName = line.split(',')
            first,last = n.split()
            d1 = {'Name':last + ", "+ first,'Title':j,'salary':float(i)* float(bouns)+ float(i)}
            emp.append(d1)
        print("\t\tUnsorted List\n")
        outputFile.write("\t\tUnsorted List\n\n")
        printEmpList(outputFile,emp)
        BubbleSort(emp)
        print("\n\n\t\tAlphabetically sorted List")
        outputFile.write("\n\t\tAlphabetacally sorted List\n\n")
        printEmpList(outputFile,emp)

        inputFile.close()

    finally:
        if (inputFileOK == True):
            print ("Successfully read information from file", inputFileName)
        else:
            print ("Unsuccessfully attempted to read information from file", inputFileName)
