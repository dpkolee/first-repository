x = input("enter value of x: " )
y = input("enter value of y: ")
if x==0:
	print("x-axis")
elif y==0:
	print("y-axis")
elif x>0 and y>0:
	print("1st quadrant")
elif x<0 and y>=0:
	print("2nd quadrant")
elif x<0 and y<0:
	print("3rd quadrant")
else:
	print("4th quadrant")
