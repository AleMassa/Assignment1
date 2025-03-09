import random as rand
import sys

def Number_Generator():
	num = rand.randint(0, 100)
	return num

def Operation_Generator():
	operation = {
			1: "+",
			2: "-",
			3: "*",
			4: "/"
		}
	choice = rand.randint(1,4)
	return operation[choice]

def Channel_Operation_Gen():
	n_operation = rand.randint(3,5)
	nums = [Number_Generator() for i in range(1,n_operation+1)]
	operations = [Operation_Generator() for i in range(1,n_operation)]
	string = ""
	count = 0
	for num,op in zip(nums,operations):
		count +=1
		string += str(num) + " "
		string += op + " "	
	string += str(nums[count])
	return string

def start(): 
	n = int(sys.argv[1])
	if(n<=0):
		print("\nError")
		exit()
	with open("result.txt", "w") as file:
		file.write("2359275\n")
		for i in range(n):
			channel = Channel_Operation_Gen()
			try:
				res = eval(channel)
				file.write(channel +" = " + str(round(res,2))+"\n")
			except Exception as e:
				continue
		
start()
