#
# Insurance lCode Fee  .txt to .xls
#
# Jason Sigler
# 2/13.2019
#
#  
#####################

from os import listdir
from os.path import *
import xlwt 
import xlutils

#Initialize the workbook and define the output target
data_destination = xlwt.Workbook()
sheet = data_destination.add_sheet('feeSchedule')  

#Initialize variables
row = 0
modifierRequired = '00'
lCode = ''
allowable = ''
codeModifier = ''

#open the source file
file = open('MedicaidInput.txt')

#Iterates through the input, separates each line and transforms it into a list, then writes
#only codes with the specified modifier to the file. 
#
for line in file:                     
	line = line.strip()
	if line:
		splitLine = line.split(" ")
		lCode = splitLine[0]
		codeModifier = splitLine[1]
		allowable = splitLine[-1]
		if codeModifier == modifierRequired:
			sheet.write(row,0,lCode)
			sheet.write(row,1,allowable)
			row += 1
		
		
			

	
			
#Save the destination target
data_destination.save('formattedschedule.xls')
