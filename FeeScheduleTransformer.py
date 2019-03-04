#
# Insurance lCode Fee  .txt to .xls
#
# Jason Sigler
# 2/13/2019
#
#  
#####################
import xlwt


def ConvertToExcel(inputFile, outputFile, modifier):
    row = 0
    modifierRequired = modifier
    #Try to open the user-defined file any catch any errors that occur
    try:
        file = open(inputFile)
    except FileExistsError:
        print("Invalid filename\n")
        UserMenu()
    except FileNotFoundError:
        print("File Not Found\n")
        UserMenu()
    except:
        print("Something went horribly wrong\n")
        UserMenu()

    #Initialize the new Excel document
    data_destination = xlwt.Workbook()
    sheet = data_destination.add_sheet('feeSchedule')


    for line in file:
        line = line.strip()
        if line:
            splitLine = line.split(" ")
            lCode = splitLine[0]
            codeModifier = splitLine[1]
            allowable = splitLine[-1]
            if codeModifier == modifierRequired:
                sheet.write(row, 0, lCode)
                sheet.write(row, 1, allowable)
                row += 1
    data_destination.save(outputFile)
    print(str(row) + " Rows Processed.\n")
    UserMenu()

def UserMenu():
    print("Fee Schedule Transformer")
    print("................")
    print("1. Convert TXT to XLS")
    print("2. Quit\n")
    userChoice = input("Make a Selection:")

    if userChoice == '1':
        sourceFile = input("Enter the source filename:")
        destinationFile = input("Enter the destination filename:")
        requiredModifier = input("Enter the modifier to search against:")
        ConvertToExcel(sourceFile, destinationFile, requiredModifier)
    elif userChoice == '2':
        exit(0)
    else:
        print("Not a valid entry")
        UserMenu()


UserMenu()
