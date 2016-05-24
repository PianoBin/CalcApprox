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
Simpson's Rule
Trapezoidal Rule
FindX (DONE)
Solve
Graph
Compare Error b/t Simpson's & Trapezoidal
'''

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
		sum += Solve(tempListy) #parse the function and solve now we have dx	



#Trapezoidal Rule
def trapRule (function, dx, upbnd, lwbnd):
	range = (upbnd - lwbnd)
	n = range / dx #number of subintervals
	h = range/n 
	
	#deleted Function_Evaluation, moved to here
	listy = []
	listy = function.split()

	sum = 0
	tempListy = [] #do not modify the original listy while looping
	for num in range(lwbnd, upbnd, dx):
		tempListy = FindX(listy, num) #change the list, replace x with num
		sum += Solve(tempListy) #parse the function and solve now we have dx	

def FindX (listy, xitdx) : #Change the x to given number, modified listy 
	for val in listy:
		if listy[val].equals("x"):
			listy[val] = xitdx
	return listy

def Solve (listy): #Find y
	counter = 0
	
	if  listy[counter].equals("+"): #addition symbol
				
	elif listy[counter].equals("-"): #subtraction
	
	elif listy[counter].equals("*"): #multiplication

	elif listy[counter].equals("/"): #division

	elif  listy[counter].equals("^"): #power
	
	else : #Just a number


	counter++
