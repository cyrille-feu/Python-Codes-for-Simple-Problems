""" this program find the magic number with four digit"""
#########################################################################################
#########################################################################################
### the process is take any four-digit number n. Rearrange the digits to make the     ###
### largest possible number called n max . Also rearrange the digits to make the smal-###
### lest possible number,n min . if n max −n min = n then our n is a magic number     ###
#########################################################################################
#########################################################################################
n=1000
while n<=9999:                  # take all the number in range (1000,10000)
	n1=list(str(n))             # transform a number into two same list
	n2=list(str(n))
	t1=[]                       #create two empty list
	t2=[]
	for i in range(len(n1)):    # forn new list t1 which contain the componemt 
		t1.append(max(n1))      # of our number in decroissant order 
		k=n1.index(max(n1))
		del(n1[k])
	for i in range(len(n2)):    # forn new list t2 which contain the componemt 
		t2.append(min(n2))      # of our number in croissant order
		v=n2.index(min(n2))
		del(n2[v])
	s1="" 
	s2=""
	for i in range(len(t1)):    # concatenate each of our two new list to have 
		s1+=t1[i]               # a string
		s2+=t2[i]
	if (int(s1)-int(s2)==n):    # convert our two string into integer and test 
		magic=n                 # te condition. if it is true we out a loop while
		n=10000                 # and save our number into magic
	else:
		n=n+1                   # else add 1 to our number and restart the process
		
print ("the magic number is",magic)

print("the max is",s1,"and the min is",s2)
	
	
	
	
				
					
			
				

