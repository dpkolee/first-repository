names = ['john doe', 'jane doe', 'johnny turk', 'molly morman']
print('users: ')
for name in names:
	end = ' and\n' if name == names[-2] else '\n'
	print(' - %s' % name, end=end)