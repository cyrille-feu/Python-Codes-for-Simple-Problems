def ClockX(n):
	""" this fuction takes as input a certain number of minutes,
and returns a string that formats the number into ‘hours:minutes‘. the format is 24h"""
	n=n%(24*60)  # compute the number of minutes in one day
	h=n//60                                             
	m=n%60
	if h<10:
		if m<10:
			print('0%d:0%d'%(h,m))
		else:
			print('0%d:%d'%(h,m))
	else:
		if m<10:
			print('%d:0%d'%(h,m))
		else:
			print('%d:%d'%(h,m))
	return
	
#########################################################################################
#################                test of our function            ########################
######################################################################################### 
	
a=int(input("enter the number of minute       "))	
ClockX(a)

		
			
