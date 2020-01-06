def ReveX(b):
	""" this function takes a string as input, and return a new string
with the same letters in reverse order"""
	a=""                   #create an empty string
	i=len(b)-1
	while i>=0:
		a+=b[i]
		i-=1
	return (a)
	
##############################################################################
#################                test of our function            #############
##############################################################################	
s=str(input("enter a string        "))
b=ReveX(s)
print("the enter string is %s and the reverse is %s"%(s,b))


