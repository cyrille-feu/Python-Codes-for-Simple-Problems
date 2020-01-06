######################################################################################
########### definition of a class which contain the method to compute ################
###########             factorial  of positiv integer                 ################
######################################################################################

class factpy:
	""" this class contain a method FacyoX wich compute the factorial of any integer
greater -1 """
	def __init__(self,number):
		self.number=number
		
	def FactoX(self):                      # method facto to compute factorial
		s=1
		for i in range(1,self.number+1):
			s=s*i
		return(s)

######################################################################################
###########             definition of a function which compute        ################
###########                factorial of positive integer              ################
######################################################################################


def FactoX(n):
		s=1
		for i in range(1,n+1):
			s=s*i
		return(s)

######################################################################################
###########             test of our method and our function           ################
###########                          factorial                        ################
######################################################################################

		
b=int(input("enter a number         "))	
n  =factpy(b)
x=n.FactoX()	
y=FactoX(b)

print("the value of factorial(%d)compute by method is %d"%(b,x))
print("the value of factorial(%d)compute by function is %d"%(b,y))
		
		

