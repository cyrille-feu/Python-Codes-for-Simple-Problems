def Longest (s):
	""" takes a string (preferably a sentence) as input and returns the longest 
	word in the string. if we many words with the same lenght it will return all 
	this words into list"""
	
	b=s.split()                       # convert sentence into a list which contain all the word of this sentence
	maxi=[]                           # create an empty list maxi to save the longest word
	n= len(b)                         # check the length of list b
	t=0
	maxi.append(b[0])                 # add the first word of list b in maxi
	for i in range(1,n):
		if len(maxi[t])<len(b[i]):    #compare the length of this word with all the word and change it if we have
			maxi[t]=b[i]              #another word greater than it and repeat the process
		elif len(maxi[t])==len(b[i]):
			maxi.append(b[i])
			t=t+1
	return print (maxi)               #return the list of all the longest numbers
	

##############################################################################
#################                test of our function            #############
##############################################################################

Longest('today is my birthday')
Longest("i am coop students at Aims cameroon for the academic years 2019 to 2021")

