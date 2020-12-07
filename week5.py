'''
The academic office at the Hogwarts School of Witchcraft and Wizardry has compiled data about students' grades. The data is provided as text from standard input in three parts: information about courses, information about students and information about grades. Each part has a specific line format, described below..

    Information about courses
    Line format: Course Code~Course Name~Semester~Year~Instructor
    Information about students
    Line format: Roll Number~Full Name
    Information about grades
    Line format: Course Code~Semester~Year~Roll Number~Grade 

The possible grades are A, AB, B, BC, C, CD, D with corresponding grade points 10, 9, 8, 7, 6, 5 and 4. The grade point average of a student is the sum of his/her grade points divided by the number of courses. For instance, if a student has taken two courses with grades A and C, the grade point average is 8.50 = (10+7)÷2. If a student has not completed any courses, the grade point average is defined to be 0.

You may assume that the data is internally consistent. For every grade, there is a corresponding course code and roll number in the input data.

Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Courses. The second section begins with a line containing Students. The third section begins with a line containing Grades. The end of the input is marked by a line containing EndOfInput.

Write a Python program to read the data as described above and print out a line listing the grade point average for each student in the following format:

Roll Number~Full Name~Grade Point Average

Your output should be sorted by Roll Number. The grade point average should be rounded off to 2 digits after the decimal point. Use the built-in function round().

Here is a sample input and its corresponding output.

Sample Input
Courses
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput

Sample Output
SLY2301~Hannah Abbott~9.5
SLY2302~Euan Abercrombie~7.5
SLY2303~Stewart Ackerley~8.0
SLY2304~Bertram Aubrey~0
SLY2305~Avery~8.5
SLY2306~Malcolm Baddock~6.5
SLY2307~Marcus Belby~8.0
SLY2308~Katie Bell~9.5
SLY2309~Sirius Orion Black~9.0

'''

# program start's from here
try :
	grade = {'A':10 ,'AB':9 ,'B':8 ,'BC':7 ,'C':6 ,'CD':5 ,'D':4} 	#grade values 
	
	s = input()
	
	if s == 'Courses' :
		while(True) :
			t = input()
			if t == 'Students' :
				break
	
	di = dict()	#It stores student's roll number and name ,where rollNo is key
	order = list()	# It will stores order they entered ie.RollNo
	
	while(True) :
		t = input()
		if t == 'Grades' :
			break
		lst = t.split('~')	#split the string using '~' delimiter
		order.append(lst[0])	
		di[lst[0]] = di.get(lst[0] ,lst[1])
	
	lst = list()
	while(True) :
		t = input()
		if t == 'EndOfInput' :
			break 
		lst.append(t)
	
	marks_lst = list()
	for roll in order :
		sum_marks = 0
		i = 0
		for st in lst :
			t = st.split('~')
			if t[3] != roll :
				continue
			marks = grade.get(t[4])
			i += 1
			sum_marks = ( sum_marks + marks) / i
		marks_lst.append(sum_marks)
	
	#sorting of roll numbers using bubble sort
	for i in range(len(marks_lst) -1) :
		for j in range(i+1 ,len(marks_lst)) :
			if order[i] > order[j] :
				mtmp = marks_lst[i]
				otmp = order[i]
				marks_lst[i] = marks_lst[j]
				order[i] = order[j]
				marks_lst[j] = mtmp
				order[j] = otmp
				 
	#displaying output in desc order	
	for i in range( len(marks_lst)) :			
		output = "{}~{}~{}".format(order[i],di.get(order[i]) ,marks_lst[i])				# msg = "Hello, {0} {1}!".format(fn,ln)
		print(output)
		
#end of try block
except :
	print('Error')
	
#end of program

