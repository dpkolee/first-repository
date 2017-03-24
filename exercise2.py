equation= input("enter any equation of  form y=mx+c: ")
rhs= equation.split('=')[1]
parts= rhs.split('+')
m= parts[0].replace('x','').strip()
c= parts[1].strip()
print('slope of line: {}' .format(m))
print('y-intercept: {}' .format(c))



