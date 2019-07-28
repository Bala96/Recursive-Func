"""A recursive Python function"""
import sys
def recursive_func(the_list,indent=False,level=0,fh=sys.stdout):
	for each_item in the_list :
		if isinstance (each_item,list):
			recursive_func(each_item,indent,level+1,fh)
		else :
			if indent:
				for tab_stop in range(level):
					print("\t",end='',file=fh) #for tab spaces to show recursion and to write data into a file
			print(each_item,file=fh)
"""A simple recursive function to print nested lists""" 
