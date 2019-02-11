newpassword = input('wat is u nieuwe passwoord')
oldpassword = 'Python'

numbers = [0,1,2,3,4,5,6,7,8,9]

if newpassword != oldpassword and len(newpassword) > 6 and int(numbers) in newpassword:
    print('true')
else:
    print('false')

print(30*'_')

newpassword = input('wat is u nieuwe passwoord')
oldpassword = 'Python'

if newpassword != oldpassword and len(newpassword) > 6:
    print('true')
else:
    print('false')