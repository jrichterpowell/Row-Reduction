import sympy as sy
import numpy as np
from numpy.random import randint
from sympy import pprint


print("Welcome to the endless row reducer!")


def randomvalue(difficulty):
	root = randint(-5, 5)

	chance = randint(16)

	if(chance < difficulty):
		root = sy.Rational(root, randint(2, 5))

	return root

def generateRow(size, pos, difficulty ):
	row = []

	for i in range(1, size):
		if i == pos:
			row.append(1)
		else:
			row.append(0)
		
	row.append(randomvalue(difficulty))
	row = sy.Matrix([row])
	return row

def randomize(matrix, size, difficulty):

	for i in range(0, difficulty * 8):
		roll = randint(0, 2)

		#add rows to another row
		if roll == 1:
			source = randint(0, size - 1)
			dest = randint(0, size - 1 )

			while dest == source:
				dest = randint(0, size - 1)

			sourcerow = matrix.row(source)

			#add random scalar multiple of one row to another
			destrow = matrix.row(dest) + (matrix.row(source) * randint(size))
			pprint(destrow)

			matrix.row_del(dest)

			matrix = matrix.row_insert(0, destrow)

		#multiply rows
		else:
			chance = randint(1, size * 4)
			multplier = 0
			

			#set the multiplier
			if chance > size*2:
				multplier = 1
			else:
				multplier = chance

			print(multplier)


			row = randint(0, size -1)
			replacement = matrix.row(row) * multplier

			matrix.row_del(row)
			matrix = matrix.row_insert(0, replacement)

	return matrix



while True:
	print("Choose a difficulty:\n 1.Management\n 2.Arts\n 3.Honours Math/CS \n 4.Wang\n 5.Kelome's Multiple Choice\n 6+.Kicking a wall with a toothpick under your toenail\n")
	
	difficulty = int(input("Please enter your selection(1-5): "))

	size = difficulty + 2


	A = sy.Matrix()

	#rownum = np.clip(np.random.randint(size*2), difficulty - 1, size)
	rownum = size
	

	for i in range(1, rownum):
		chance = 2

		if chance == 2:
			row = generateRow(size, i, difficulty)
		else:
			row = row * randomvalue(difficulty)
			print("unnh?")

		A = A.row_insert(0, row)



	A = randomize(A, size, difficulty)

	pprint(A)

	input("When there is \"No Hope,\" press any key to see how off you were")

	print("The right answer was:")

	pprint(A.rref())




	exit()