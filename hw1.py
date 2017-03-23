words = ['beg','repulsive','quick','rejoice','gate','face','pray','number','visitor','boiling','fasten','glu','mundane','hose','innocent','art','remarkable','tongue','orange','huge']
a = input('enter the string: ')
suggestion = [x for x in words if '%s' % a.lower() in x.lower()]
print('suggestions: ', suggestion)