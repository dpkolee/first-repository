user_info = [
				{
					'first_name': 'deepak',
					'last_name': 'oli',
					'email': 'deepakolee@gmail.com',
					'address': 'kathmandu'
				},

				{
					'first_name': 'naryan',
					'last_name': 'kc',
					'email': 'olinaryan@gmail.com',
					'address': 'lalitpur'
				}
]

user_input = input('enter an email address: ')

user_detail = [ x for x in user_info[] if  '%s' % user_input in user_info[]['email'] ]

print('first_name: %s ' % user_detail[]['first_name'])
print('last_name: %s ' % user_detail[]['last_name'])
print('email: %s ' % user_detail[]['email'])
print('address: %s ' % user_detail[]['address'])