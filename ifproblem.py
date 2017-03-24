age = input('enter your age: ')
if age <= 0:
	print('invalid input for age')
elif age <= 1:
	print("you'r an infant")
elif age >= 2 and age <= 12 :
	print("you'r just a kid")
elif age >= 13 and age <= 19:
	print("you'r a teenager")
elif age >= 20 and age <= 45:
	print("you'r adult now")
elif age >= 46 and age <= 59:
	print("you'r middle aged")
elif age in range(60, 120):
	print("you'r old enough")
else:
	print("you are too old to be still alive")