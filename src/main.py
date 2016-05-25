#FYI, raw_input was renamed to input in Python 3. That's a conflict between our versions.
#The current implementation of the for loop in trapezoidal and simpson's is incorrect, does not reflect formula. Will fix.

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
Simpson's Rule (DONE-UNTESTED)
Trapezoidal Rule (DONE-UNTESTED)
FindX (DONE-UNTESTED)
Solve (DONE-UNTESTED)
Graph
Compare Error b/t Simpson's & Trapezoidal
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
import numpy as nump
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#INPUT
print ("Integrates the following function in two ways.")
prompt1 = "Enter Function: "
function = input(prompt1)
prompt2 = ("Enter dx: ")
dx = input(prompt2)
prompt3 = ("Enter upperbound of integration: ")
upbnd = input(prompt3)
prompt4 = ("Enter lowerbound of integration: ")
lwbnd = input(prompt4)

#Simpson's Rule
def simpRule (function, dx, upbnd, lwbnd):
	range = upbnd - lwbnd
	n = range / dx
	h = range / n

	listy = []
	listy = function.split()

	sum = 0
	tempListy = []	
	for num in range(lwbnd, upbnd, dx):
	    tempListy = FindX(listy, num) #change the list, replace x with num
	    y = Solve(tempListy) #parse the function and solve now we have dx	
	    if counter == 0 or counter == n:
		    sum += y
	    elif counter % 2 == 1:
		    sum += 4 * y #multiply by 4
	    else:
		    sum += 2 * y #multiply by 2
	counter += 1
	coeff = h / 3
	sum *= coeff



#Trapezoidal Rule
def trapRule (function, dx, upbnd, lwbnd):
	range = (upbnd - lwbnd)
	n = range / dx #number of subintervals
	h = range/n 
	
	#deleted Function_Evaluation, moved to here
	listy = []
	listy = function.split()

	sum = 0
	counter = 0
	tempListy = [] #do not modify the original listy while looping
	for num in range(lwbnd, upbnd, dx):
		tempListy = FindX(listy, num) #change the list, replace x with num
		y = Solve(tempListy) #parse the function and solve now we have dx	
		if counter == 0 or counter == n:
			sum += y
		else:
			sum += 2 * y #multiply by 2
		counter += 1
	coeff = h / 2
	sum *= coeff

def FindX (listy, xitdx) : #Change the x to given number, modified listy 
	for val in listy:
		if listy[val].equals("x"):
			listy[val] = xitdx
	return listy

def Solve (listy): #Find y
	sum = 0
	operations1 = {"^", "*", "-"} #* and / carry equal weight, as well as - and +
	operations2 = {"^", "/", "+"}
	for ops in range(3): #order of operations
		for part in listy: #parse through listy
			if  listy[part].equals(operations1[ops]) or listy[part].equals(operations2[ops]): 
				num1 = listy[part - 1] #2 numbers to operate on
				num2 = listy[part + 1]

				if listy[part].equals("^"): #power
					sum += math.pow(num1, num2)
					del listy[part + 1] #delete three items and replace with sum
					del listy[part]
					del listy[part - 1]

					listy.append(sum)
				elif listy[part].equals("*"): #multiplication
					sum += num1 * num2
					del listy[part + 1]
					del listy[part]
					del listy[part - 1]

					listy.append(sum)
				elif listy[part].equals("/"): #division
					sum += num1 / num2
					del listy[part + 1]
					del listy[part]
					del listy[part - 1]

					listy.append(sum)	
				elif listy[part].equals("-"): #subtraction
					sum += num1 - num2
					del listy[part + 1]
					del listy[part]
					del listy[part - 1]

					listy.append(sum)
				else: #addition
					sum += num1 + num2
					del listy[part + 1]
					del listy[part]
					del listy[part - 1]

					listy.append(sum)

def graph:
