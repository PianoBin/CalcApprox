# CalcApprox
AP Calculus Final Project


In the future, perhaps adding parantheses, special function/trig support (i.e. sin, cos, tan, pi, e)

This program will run two approximations for definite integrals:
	1. Simpson's Rule
		Partitioning the interval into sub-intervals and calculating the areas of each subinterval using parabolas.
		Formula is AREA=((widthOfSubinterval)/2)(f[x(0)]+4f[x(1)]+2f[x(2)]+4f[x(3)]+2f[x(4)]+...+f[x(n)])
	2. Trapezoidal Rule
		Partitioning the interval into sub-intervals and calculating the areas of each subinterval using trapezoids.
		Formula is AREA=((widthOfSubinterval)/2)(f[x(0)]+2f[x(1)]+2f[x(2)]+...+2f[x(n-1)]+f[x(n)])
	widthOfSubinterval = (upper bound - lower bound) / number of subintervals
	In Simpson's Rule, number of subintervals MUST BE EVEN

---

Simpson's Rule:
![Simpson's Rule](https://github.com/PianoBin/CalcApprox/blob/master/src/pics/simp.PNG)

Trapezoidal Rule:
![Trapezoidal Rule](https://github.com/PianoBin/CalcApprox/blob/master/src/pics/trap.PNG)

(Courtesy of [Paul's Online Math Notes](http://tutorial.math.lamar.edu/Classes/CalcII/ApproximatingDefIntegrals.aspx))


Graph Example:
![Example](https://github.com/PianoBin/CalcApprox/blob/master/src/pics/graph.PNG)
