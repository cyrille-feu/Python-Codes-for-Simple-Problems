def SumOverX(n):
	""" this function takes an integer as input and returns the
sum over all the integers between zero and that integer, including it"""
	s=0
	if n>0:
		for i in range (0,n+1):
			s+=i
	elif n<0:
		for i in range (n,1):
			s+=i
	else:
		s=s
	return (s)
	
##############################################################################
#################                test of our function            #############
##############################################################################


n=int(input("enter an integer       "))
a=SumOverX(n)
print("the sum over all the integers between 0 and %d, including it is %d"%(n,a))
