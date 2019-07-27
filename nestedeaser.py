"""A recursive Python function"""

def recursive_func(the_list,level):
	for each_item in the_list :
		if isinstance (each_item,list):
			recursive_func(each_item,level+1)
		else :
			for tab_stop in range(level):
				print("\t",end='') #for tab spaces to show recursion
			print(each_item)
"""A simple recursive function to print nested lists""" 