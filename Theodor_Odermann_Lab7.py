"""
Lab 7
Functions and List review
"""




#Problem 1

def calc_toll(hour, is_morning, is_weekend):
	if is_morning :
		if hour < 7 :
			total_toll = 1.15
		elif hour < 10 :
			total_toll = 2.95 
		elif hour < 15 :
			total_toll = 1.90
		elif hour < 20 :
			total_toll = 3.95
		else :
			total_toll = 1.40
	if is_weekend :
		if hour < 7 :
			total_toll = 1.05
		elif hour < 20 : 
			total_toll = 2.15
		else :
			total_toll = 1.10


hour = int(input("Enter the current hour (0-23): "))
is_morning = input("Is it morning? (True/False): ").strip().lower() == "True"
is_weekend = input("Is it the weekend? (True/False): ").strip().lower() == "True"

total_toll = calc_toll(hour, is_morning, is_weekend)

print("Total toll fee:", total_toll)


#Problem 2

def gcd(interger1, interger2):
	"""This function will find the greatest common divisor of two intergers."""
	while interger2:
		interger1, interger2 = interger2, interger1 % interger2
	return interger1

def lcm(interger1, interger2):
	"""This function will take two interger arguments and return the least common multiple."""
	return abs(interger1 * interger2) // gcd(interger1, interger2)
	
interger1 = int(input("Enter the first interger: "))
interger2 = int(input("Enter the second interger: "))

print(f"The least common multiple of {interger1} and {interger2} is {lcm(interger1, interger2)}.")



#Problem 3


def factorial() :
	if n == 0 :
		return 1
	else :
		result = 1
		for i in range(1, n + 1) :
			result *= i
		return result 

def combination() :
	return factorial(m) // (factorial(k) * factorical(m - k))
	
m = int(input("Enter the value of m: "))
k = int(input("Enter the value of k: "))

print(f"The combination of {m} choose {k} is: {combination(m, k)}")

	


	






