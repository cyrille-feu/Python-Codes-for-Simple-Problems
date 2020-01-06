def VoweX (s):
	""" this function take as input a string and count the number of vowel in it"""
	nb=0                                                      # initialize the counter as 0
	for elt in s:
		if elt in ["a","e","i","o","u"]:                      # if condition is true increment 
			nb+=1                                             # the counter
	return print("the number of vowel in %s is %d"%(s,nb))    # return the number of vowel 
	
##############################################################################
#########                 test of our function              ##################
############################################################################## 	
n=str(input("enter a string        "))
VoweX(n)
