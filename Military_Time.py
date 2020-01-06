def Military(s):
	""" this function take as imput a string of time from 12 format and convert it into 24 format"""
	
	if s[-1]=='M' :                                    # test the last element of our string
		if s[-2]=='P':                                 # test the element before the last
			h=int(s[0]+s[1])+12                        # convert hour into interger and add twelve 
			m=(s[3]+s[4])                              
			out=print("%d:%s"%(h,m))                   # save result into out
		elif s[-2]=='A':
			h=s[0]+s[1]
			m=s[3]+s[4]
			out=print("%s:%s"%(h,m))
		else:
			out=print("error check the input format")
	else:
		out=print("error check the input format")
	return out                                         # return the finil result
	

###################################################################################################
#######################           test of our function              ###############################
################################################################################################### 
Military("04:52PM")
Military("02:34AM")
Military("02:34AP")
