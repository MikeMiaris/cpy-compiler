#int counterFunctionCalls


def calculate_area_rectangle(length, width):
#{
    ##Calculate the area of a rectangle given its length and width##
    
	#int y
	
	global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 1
    
	y = length * width
	
	return y+1
#}	
	
	

#def main

	#int length
	#int width
    
	length = int(input())
	width = int(input())
	
	counterFunctionCalls = 0
	
	print(calculate_area_rectangle(length, width))