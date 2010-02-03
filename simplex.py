#! /usr/bin/env python
import pylab

const_less = []
const_great = []


#print 'Enter the coefficientes of the objective function divided by space'
#print 'Ex: Z = 2x1 + 3x2 ->	 2 3'
#objective = raw_input(': ')

#object_tmp = [float(x.strip()) for x in objective.split(' ') if x.strip() ]

object_tmp = [3,5]

n_x = len(object_tmp)

#while True:
#	print 'Enter the coefficients of the constraints function divided by space, with the last value as the right hand side'
#	print 'Ex: 2x1 + 3x2 < 300 	-> 2 3 300'
#	const = raw_input(': ')
#	const_tmp = [float(x.strip()) for x in const.split(' ') if x.strip() ]
#	print 'Is the equation "less than" or greater than" the right side? (< or >)'	
#	print 'Ex: 2x1 + 3x2 < 300 	->         <  '
#	answer = raw_input(': ')
#	if answer == '<':
#		const_less.append(const_tmp)
#	elif answer == '>':
#		const_great.append(const_tmp)
#	else:
#		print 'Wrong Value!!!'
#		break

	
#	answer = raw_input('Do you want to add a new constraint? Y/N: ')
#	if answer.lower() == 'n': break

const_less = [[1,0,4],[0, 2, 12],[3,2,18]]

new_n_x = n_x

for i in range(len(const_less)):
	new_n_x = new_n_x + 1

for i in range(len(const_great)):
	new_n_x = new_n_x + 1
	new_n_x = new_n_x + 1

n_const = len(const_less)


#Construct the matrix

first_line = []
ini_matrix = []
line_tmp = []


#first line
for i in range(len(object_tmp)):
	first_line.append(-object_tmp[i])

for i in range(len(const_less)+1):
	first_line.append(0)

#Other lines

ini_matrix.append(first_line)

for i in range(len(const_less)):
	count_tmp = 0
	for j in range(n_x):
		line_tmp.append(const_less[i][j])
	while count_tmp < n_const:	
		if i == count_tmp:
			line_tmp.append(1)
		else:
			line_tmp.append(0)
		count_tmp = count_tmp + 1
	line_tmp.append(const_less[i][-1])
	ini_matrix.append(line_tmp)
	line_tmp = []

ori_matrix = ini_matrix

#Pivoting

#Discovering minimum 1st line

counter = 0

print ini_matrix

while counter >= 0:


	column_min = ini_matrix[0].index(min(ini_matrix[0]))
	print column_min 
	value_tmp = []
	for i in range(len(ini_matrix)-1):
		try:
			value_tmp.append(ini_matrix[i+1][-1] / ini_matrix[i+1][column_min])
		except:
			value_tmp.append(ini_matrix[i+1][-1]*10)
	
	row_piv = value_tmp.index(min(value_tmp)) + 1 

	new_line = [float(x)/float(ini_matrix[row_piv][column_min]) for x in ini_matrix[row_piv]]

	#recreate matrix
	new_matrix = []


	for i in range(len(ini_matrix)):
		
		new_line_tmp = []

		if i == row_piv:
			new_matrix.append(new_line)
		else:
			line_tmp = [float(ini_matrix[i][column_min])*float(x) for x in new_line]
			for j in range(len(ini_matrix[i])):

				new_line_tmp.append(ini_matrix[i][j] - line_tmp[j])
			new_matrix.append(new_line_tmp)
	

	ini_matrix = new_matrix


	if min(new_matrix[0]) < 0:
		counter = counter + 1
		print 'Finished iteration ', counter

	else:
		print 'Optimum found, iteration', counter +1 
		counter == -1
		break

x_values = []

for i in range(n_x):
	for j in range(len(ini_matrix)):
		if ini_matrix[j+1][i] == 1:
			x_values.append(ini_matrix[j+1][-1])
			break
	

print x_values




