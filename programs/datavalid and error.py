datavalid=False
while datavalid==False:
	grade1=input("enter the first grade: ")
	
	try:
	    grade1=float(grade1)
	    print("GRADE 1= ",grade1)
	except:
               print("Enter proper grade")
               continue
        
	if grade1<0 or grade1>10:
	   print("grade must be between 0 and 10")
	   continue
	else:
	     datavalid=True
	     
	     
	     #CONTINUE THE REST OF THE CALCULATION#
