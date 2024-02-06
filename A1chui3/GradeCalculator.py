#A1,Chi Heng Jeffrey Hui,CIS 345, T TH 12:00 PM
import os
gradePerCategory=0.0
finalGrade=0.0
#Create dictionaries for each item in the course
exercise={'eP':0,'tP':160,'w':3,'gPC':gradePerCategory}
assignment={'eP':0,'tP':210,'w':10,'gPC':gradePerCategory}
project={'eP':0,'tP':100,'w':17,'gPC':gradePerCategory}
quiz={'eP':0,'tP':80,'w':25,'gPC':gradePerCategory}
exam={'eP':0,'tP':200,'w':36,'gPC':gradePerCategory}
final={'eP':0,'tP':100,'w':9,'gPC':gradePerCategory}
#Create a nested dictionary structure
wholeCourse={'Exercise':exercise,'Assignment':assignment,'Project':project,'Quiz':quiz,'Exam':exam,'Finals':final}

print('Add up all points earned for each grade topic\n(do not add your lowest score for the 3 topics with a dropped score)\n\n')


#Store earned points and calculate the grade per category for each item by using the for loop
for key in wholeCourse.keys():

 wholeCourse[key]['eP']=float(input(f'Enter your total points earned for {key}:'))
 wholeCourse[key]['gPC']=round(wholeCourse[key]['eP']/wholeCourse[key]['tP']*wholeCourse[key]['w'],2)

#Add all the grade per category
finalGrade=(exercise['gPC']+assignment['gPC']+project['gPC']+ quiz['gPC']+exam['gPC']+final['gPC'])

os.system('cls')

print('\n\nGrade Information:\n\n')
#Create a dictionary for the header
header={'Cat':'Category','Pts':'Pts Earned','Total':'Total Pts','We':'Weight','Gr':'Grade'}
#Print out the header and align its position
print(f"{header['Cat']:<15}| {header['Pts']:>12} | {header['Total']:>10}| {header['We']:>6} | {header['Gr']:>6}|")
print('------------------------------------------------------------')
#Use the for loop to print out data row by row. Also, using specific values to align the table properly
for key in wholeCourse.keys():
 print(f'{key:<15}| {wholeCourse[key]["eP"]:>12} | {wholeCourse[key]["tP"]:>10}| {wholeCourse[key]["w"]:>6} | {wholeCourse[key]["gPC"]:>6}|')

#Print out the final grade and round it to 2 decimals
print(f'\n\nFinal Grade:  {finalGrade:.2f}')