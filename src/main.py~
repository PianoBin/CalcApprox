#FYI, raw_input was renamed to input in Python 3. That's a conflict between our versions.
#The current implementation of the for loop in trapezoidal and simpson's is incorrect, does not reflect formula. Will fix.
#I think the problem is due to decimal points
#found the index prob....also we need to change all my .equals to ==

#INFO:
'''
This program will run two approximations for definite integrals:
	1. Simpson's Rule
		Partitioning the interval into sub-intervals and calculating the areas of each subinterval using parabolas.
		Formula is AREA=((widthOfSubinterval)/2)(f[x(0)]+4f[x(1)]+2f[x(2)]+4f[x(3)]+2f[x(4)]+...+f[x(n)])
	2. Trapezoidal Rule
		Partitioning the interval into sub-intervals and calculating the areas of each subinterval using trapezoids.
		Formula is AREA=((widthOfSubinterval)/2)(f[x(0)]+2f[x(1)]+2f[x(2)]+...+2f[x(n-1)]+f[x(n)])
	widthOfSubinterval = (upper bound - lower bound) / number of subintervals
	In Simpson's Rule, number of subintervals MUST BE EVEN
'''

#CHECKLIST:
'''
INPUT (DONE)
Simpson's Rule (DONE-STILL TESTING)
Trapezoidal Rule (DONE-STILL TESTING)
FindX (DONE-STILL TESTING)
Solve (DONE-STILL TESTING)
Graph
Compare Error b/t Simpson's & Trapezoidal & original
'''

'''
 _____       _       ___                             
/  __ \     | |     / _ \                            
| /  \/ __ _| | ___/ /_\ \_ __  _ __  _ __ _____  __ 
| |    / _` | |/ __|  _  | '_ \| '_ \| '__/ _ \ \/ / 
| \__/\ (_| | | (__| | | | |_) | |_) | | | (_) >  <  
 \____/\__,_|_|\___\_| |_/ .__/| .__/|_|  \___/_/\_\ 
                         | |   | |                   
                         |_|   |_|   
                         
Made by Steini(@SteiniDavid) and Shoji(@PianoBin)
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
#from sympy import integrals

#INPUT
print ("Integrates the following function in two ways.")
prompt1 = "Enter Function: "
function = input(prompt1) #remain as String
prompt2 = ("Enter dx: ")
dx = float(input(prompt2))
prompt4 = ("Enter lowerbound of integration: ")
lwbnd = int(input(prompt4))
prompt3 = ("Enter upperbound of integration: ")
upbnd = int(input(prompt3))

#Simpson's Rule
def simpRule (function, dx, upbnd, lwbnd):
	theRange = upbnd - lwbnd
	n = theRange / dx
	h = theRange / n

	#deleted Function_Evaluation, moved to here
	listy = list(function)

	theSum = 0
	counter = 0
	tempListy = []	
	check = np.arange(lwbnd, upbnd, dx) #Use numpy for step sizes
	check = check.tolist() #change to list
	check.append(upbnd) #add high end
	for num in range(len(check)):
	    tempListy = FindX(listy, check[num]) #change the list, replace x with num
	    y = Solve(tempListy) #parse the function and solve now we have dx	
	    if counter == 0 or counter == n:
		    theSum += y
	    elif counter % 2 == 1:
		    theSum += 4 * y #multiply by 4
	    else:
		    theSum += 2 * y #multiply by 2
	    counter += 1
	coeff = h / 3
	theSum *= coeff

	print ("Simpson's Rule Sum: " + str(theSum))

#Trapezoidal Rule
def trapRule (function, dx, upbnd, lwbnd):
	theRange = (upbnd - lwbnd)
	n = theRange / dx #number of subintervals
	h = theRange/n 
	
	#deleted Function_Evaluation, moved to here
	listy = list(function)

	#TESTINGTESTINGTESTING
	print (listy)

	theSum = 0
	counter = 0
	tempListy = [] #do not modify the original listy while looping
	check = np.arange(lwbnd, upbnd, dx) #Use numpy for step sizes
	check = check.tolist() #change to list
	check.append(upbnd) #add high end num
	#TESTINGTESTINGTESTING
	print (check)

	for num in range(len(check)):
		print ("num " + str(num))
		tempListy = FindX(listy, check[num]) #change the list, replace x with num
		#TESTINGTESTINGTESTING
		print (tempListy)

		y = Solve(tempListy) #parse the function and solve now we have dx	
		if counter == 0 or counter == n:
			theSum += y
		else:
			theSum += 2 * y #multiply by 2
		counter += 1
	coeff = h / 2
	theSum *= coeff
	
	print ("Trapezoidal Rule Sum: " + str(theSum))

def FindX (listy, xitdx) : #Change the x to given number, modified listy
	print (str(xitdx))
	leng = len(listy)
	for val in range(leng):
		if listy[val] == "x":
			if val == 0: #at beginning
				if listy[val + 1] == "+" or listy[val + 1] == "-" or listy[val + 1] == "^" or listy[val + 1] == "*" or listy[val + 1] == "/": 
					listy[val] = xitdx #Just replace with new value
				else:
					listy.insert(val + 1, "*") #manually insert sign
					listy[val] = xitdx
			elif val == leng: #at end
				if listy[val - 1] == "+" or listy[val - 1] == "-" or listy[val - 1] == "^" or listy[val - 1] == "*" or listy[val - 1] == "/": 
					listy[val] = xitdx
				else:
					listy.insert(val, "*")
					listy[val + 1] = xitdx
			else: #somewhere in the middle
				if listy[val - 1] == "0" or listy[val - 1] == "1" or listy[val - 1] == "2" or listy[val - 1] == "3" or listy[val - 1] == "4" or listy[val - 1] == "5" or listy[val - 1] == "6" or listy[val - 1] == "7" or listy[val - 1] == "8" or listy[val - 1] == "9":
					listy.insert(val, "*")
					listy[val + 1] = xitdx
	return listy

def Solve (listy): #Find y
	sum = 0
	leng = len(listy)
	operations1 = ["^", "*", "-"] #* and / carry equal weight, as well as - and +
	operations2 = ["^", "/", "+"]
	lengOps = len(operations1)
	for ops in range(lengOps): #order of operations
		#TESTINGTESTINGTESTING
		#print ("ops " + str(ops))
		for part in range(leng): #parse through listy
			#TESTINGTESTINGTESTING
			#print ("leng " + str(leng))
			#print ("part " + str(part))
			if  listy[part] == (operations1[ops]) or listy[part] == (operations2[ops]): 
				num1 = int(listy[part - 1]) #2 numbers to operate on
				num2 = int(listy[part + 1])

				if listy[part] == ("^"): #power
					sum += math.pow(num1, num2)
					listy.pop(part + 1) #delete three items and replace with sum
					listy.pop(part)
					listy.pop(part - 1)

					listy.insert(part - 1, sum)

				elif listy[part] == ("*"): #multiplication
					sum += num1 * num2
					listy.pop(part + 1) #delete three items and replace with sum
					listy.pop(part)
					listy.pop(part - 1)

					listy.insert(part - 1, sum)
				elif listy[part] == ("/"): #division
					sum += num1 / num2
					listy.pop(part + 1) #delete three items and replace with sum
					listy.pop(part)
					listy.pop(part - 1)

					listy.insert(part - 1, sum)
				elif listy[part] == ("-"): #subtraction
					sum += num1 - num2
					listy.pop(part + 1) #delete three items and replace with sum
					listy.pop(part)
					listy.pop(part - 1)

					listy.insert(part - 1, sum)
				else: #addition
					sum += num1 + num2
					listy.pop(part + 1) #delete three items and replace with sum
					listy.pop(part)
					listy.pop(part - 1)

					listy.insert(part - 1, sum)
			leng = len(listy) #AHA! List length was changing, needed to update leng
			part = 0 #full reset
			ops = 0
	return sum



simpRule(function, dx, upbnd, lwbnd)
trapRule(function, dx, upbnd, lwbnd)
