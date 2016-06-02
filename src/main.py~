#FYI, raw_input was renamed to input in Python 3. That's a conflict between our versions.
#The current implementation of the for loop in trapezoidal and simpson's is incorrect, does not reflect formula. Will fix.
#I think the problem is due to decimal points
#found the index prob....also we need to change all my .equals to ==
#Still need to add functions to fix decimal numbers and multi-digit numbers
#need to fix for multiple x's in func
#FIX check if float/int in joinDecimal and greaterthan9

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
Simpson's Rule (DONE)
Trapezoidal Rule (DONE)
GreaterThan9 (WORKS)
JoinDecimal (WORKS)
FindX (WORKS)
Solve (WORKS)
Integrate(WORKS)
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
import math
from sympy import *

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

#Trapezoidal Rule
def trapRule (function, dx, upbnd, lwbnd):
	theRange = (upbnd - lwbnd)
	n = theRange / dx #number of subintervals

	#deleted Function_Evaluation, moved to here
	listy = list(function)
	
	listy = joinDecimal(listy)
	listy = greaterThan9(listy)

	#TESTINGTESTINGTESTING
	#print (listy)

	theSum = 0
	counter = 0
	tempListy = [] #do not modify the original listy while looping
	check = np.arange(lwbnd, upbnd, dx) #Use numpy for step sizes
	check = check.tolist() #change to list
	check.append(upbnd) #add high end num
	#TESTINGTESTINGTESTING
	#print (check)

	for num in range(len(check)):
		#print ("num " + str(num))
		#DO NOT EVER CHANGE LISTY
		listyKEEP = list(listy)
		#print (listyKEEP)
		#print ("LISTY ABOVE")
		tempListy = FindX(listyKEEP, check[num]) #change the list, replace x with num
		#TESTINGTESTINGTESTING
		#print (tempListy)

		y = Solve(tempListy) #parse the function and solve now we have dx
		#print ("y = " + str(y))
		if counter == 0 or counter == n:
			theSum += y
		else:
			theSum += (2 * y) #multiply by 2
		counter += 1
	coeff = dx / 2
	theSum *= coeff
	
	print ("Trapezoidal Rule Sum: " + str(theSum))


#Simpson's Rule
def simpRule (function, dx, upbnd, lwbnd):
	theRange = upbnd - lwbnd
	n = theRange / dx
	#deleted Function_Evaluation, moved to here
	listy = list(function)

	#print (listy)
	
	listy = joinDecimal(listy)
	listy = greaterThan9(listy)

	#TESTINGTESTING TESTING
	#print (listy)

	theSum = 0
	counter = 0
	tempListy = []	
	check = np.arange(lwbnd, upbnd, dx) #Use numpy for step sizes
	check = check.tolist() #change to list
	check.append(upbnd) #add high end
	for num in range(len(check)):
	    listyKEEP = list(listy)
	    tempListy = FindX(listyKEEP, check[num]) #change the list, replace x with num
	    y = Solve(tempListy) #parse the function and solve now we have dx	
	    if counter == 0 or counter == n:
	    	    theSum += y
	    elif counter % 2 == 1:
	 	    theSum += (4 * y) #multiply by 4
	    else:
		    theSum += (2 * y) #multiply by 2
	    counter += 1
	coeff = dx / 3
	theSum *= coeff

	print ("Simpson's Rule Sum: " + str(theSum))

def FindX (listy2, xitdx) : #Change the x to given number, modified listy
	#print (str(xitdx))
	val = 0
	while val < len(listy2):
		if listy2[val] == "x":
			#print (val)
			if val == 0: #at beginning
				if listy2[val + 1] == "+" or listy2[val + 1] == "-" or listy2[val + 1] == "^" or listy2[val + 1] == "*" or listy2[val + 1] == "/": 
					listy2[val] = xitdx #Just replace with new value
				else:
					listy2.insert(val + 1, "*") #manually insert sign
					listy2[val] = xitdx
			elif val == (len(listy2) - 1): #at end
				if listy2[val - 1] == "+" or listy2[val - 1] == "-" or listy2[val - 1] == "^" or listy2[val - 1] == "*" or listy2[val - 1] == "/": 
					listy2[val] = xitdx
				else:
					listy2.insert(val, "*")
					listy2[val + 1] = xitdx
			else: #somewhere in the middle
				try:
					float(listy2[val - 1]) # a num
					listy2.insert(val, "*")
					listy2[val + 1] = xitdx
				except ValueError:
					pass
		#print (listy2)
		val += 1
		#print (val)
	return listy2

def Solve (listy3): #Find y
	sum = float(0)
	leng = len(listy3)
	operations1 = ["^", "*", "-"] #* and / carry equal weight, as well as - and +
	operations2 = ["^", "/", "+"]
	lengOps = len(operations1)
	#WE NEED TO MAKE THESE WHILE LOOPS
	ops = 0
	part = 0
	while ops < lengOps:
	#for ops in range(lengOps): #order of operations
		#TESTINGTESTINGTESTING
		##print ("ops " + str(ops))
		#WE NEED TO MAKE THESE WHILE LOOPS
		while part < leng:
		#for part in range(leng): #parse through listy3
			#TESTINGTESTINGTESTING
			#print ("leng " + str(leng))
			#print ("part " + str(part))
			if  listy3[part] == (operations1[ops]) or listy3[part] == (operations2[ops]): 
				num1 = float(listy3[part - 1]) #2 numbers to operate on
				num2 = float(listy3[part + 1])

				if listy3[part] == ("^"): #power
					sum = math.pow(float(num1), float(num2))
					listy3.pop(part + 1) #delete three items and replace with sum
					listy3.pop(part)
					listy3.pop(part - 1)

					listy3.insert(part - 1, sum)

				elif listy3[part] == ("*"): #multiplication
					sum = float(num1) * float(num2)
					listy3.pop(part + 1) #delete three items and replace with sum
					listy3.pop(part)
					listy3.pop(part - 1)

					listy3.insert(part - 1, sum)
				elif listy3[part] == ("/"): #division
					sum = float(num1) / float(num2)
					listy3.pop(part + 1) #delete three items and replace with sum
					listy3.pop(part)
					listy3.pop(part - 1)

					listy3.insert(part - 1, sum)
				elif listy3[part] == ("-"): #subtraction
					sum = float(num1) - float(num2)
					listy3.pop(part + 1) #delete three items and replace with sum
					listy3.pop(part)
					listy3.pop(part - 1)

					listy3.insert(part - 1, sum)
				else: #addition
					sum = float(num1) + float(num2)
					listy3.pop(part + 1) #delete three items and replace with sum
					listy3.pop(part)
					listy3.pop(part - 1)

					listy3.insert(part - 1, sum)
				leng = len(listy3) #AHA! List length was changing, needed to update leng
				part = 0 #full reset
				ops = 0
			part += 1
			#print (listy3)
		ops += 1
		part = 0
	return sum

def greaterThan9 (listy4): #any numbers greater than 9, collapse together
	stillBehind = True
	num = 0
	while num < len(listy4):
		try:
			float(listy4[num]) #check if number
			stillBehind = True
			while stillBehind:
				try:
					float(listy4[num + 1])
					listy4[num] = listy4[num] + listy4[num + 1]
					listy4.pop(num + 1)
					
				except (ValueError, IndexError):
					stillBehind = False
					num += 1
		except ValueError:
			num += 1
	return listy4

def joinDecimal (listy5): #find decimal points in original function and join
	stillBehind = True
	stillBefore = True
	num = 0
	while num < len(listy5):	
		if listy5[num] == ".": #There must be a 0 in front of decimal
				while stillBefore:
					listy5[num] = listy5[num - 1] + listy5[num] #concat
					listy5.pop(num - 1)
					num -= 1

					#TESTINGTESTINGTESTING
					#print (listy5)
					#print (num)

					if num == 0:
						stillBefore = False

					try: #Handling ValueError exception
						float(listy5[num - 1])
					except (ValueError):
						stillBefore = False
				while stillBehind:
					listy5[num] = listy5[num] + listy5[num + 1] #concat
					listy5.pop(num + 1) #remove the item after concat

					#print (listy5)
					#print (num)

					try: #Handling ValueError exception
						float(listy5[num + 1])
					except (ValueError, IndexError):
						stillBehind = False
		num += 1
		#print (num)
		stillBehind = True
		stillBefore = True
	return listy5
		
trapRule(function, dx, upbnd, lwbnd)
simpRule(function, dx, upbnd, lwbnd)


def integToString (function):
	listy = list(function)
	
	listy = joinDecimal(listy)
	listy = greaterThan9(listy)

	stringy = ''.join(listy)
	return stringy	

def insertAst(theString):
	return theString.replace('^', '**')

def insertMult(theString):
	return theString.replace('x', '*x')

stringy = integToString(function)
stringy = insertAst(stringy)
stringy = insertMult(stringy)

x = Symbol("x")
expr = S(stringy)

I = integrate(expr, (x, lwbnd, upbnd))
print ("Actual: " + str(I))

