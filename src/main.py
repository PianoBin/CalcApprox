#FYI, raw_input was renamed to input in Python 3. That's a conflict between our versions.

#First file!

print ("Integrates the following function in two ways.")
prompt1 = "Enter Function: "
function = input(prompt1)
prompt2 = ("Enter dx: ")
dx = input(prompt2)
prompt3 = ("Enter upperbound of integration: ")
upbnd = input(prompt3)
prompt4 = ("Enter lowerbound of integration: ")
lwbnd = input(prompt4)

#Simpsons Method






#Trapazoidal Rule
def traprule (function, dx, upbnd, lwbnd):
	range = (upbnd - lwbnd)
	n = range / dx
	h = (range)/n


#Function Evaluation
def Function_Evaluation (function):

	listyMclistFace = []
	#leng_function = function.length
	#for x in function (0,leng_function):
	#	theChar = 
	#	listyMclistFace.append(x)
	
	#instead, we can just split
	listyMclistFace = function.split()

	#testing
	for theChar in listyMclistFace:
		print (theChar)

#testing, running the Function_Evaluation method
Function_Evaluation(function)




