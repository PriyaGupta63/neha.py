a = 21
b = 23
if a > b:
    print('greater than a ')
else :
    print('greater than b') 



# simple interest 
# simple interest =( principal * rate * time)/100



# principal = int(input('enter the principal amount'))
# rate = float(input('enter the rate ')) 
# time = int(input('enter the time here '))

# simple_interest =(principal*rate*time)/100
# print(simple_interest, 'simple interest')



# # pythagorus theorum 


# base = int(input('enter the base'))
# height = int(input('enter the height '))
# hypotenuos =((base**2 + height**2)**0.5)
# print('the hypotenous is ', hypotenuos)





# choice =   (input('enter any choice'))
# if choice == 'hypotenous':
#     perpendicular = int(input('enter the value of perpendicular'))
#     base = int(input('enter the value of base '))  
#     hypotenous = (perpendicular**2 + base**2)**0.5
#     print('hypotenous is', hypotenous)
# elif choice == 'perpendicular':
#     hypotenous = int(input('enter the value of hypotenous'))
#     base = int(input('enter the value of base'))
#     perpendicular = (hypotenous**2 - base**2)**0.5
#     print('perpendicular is ', perpendicular)
# elif choice == 'base':
#     hypotenous = int(input('enter the value of hypotenous'))
#     perpendicular = int(input('enter the value of perpendicular'))
#     base = (hypotenous**2 - perpendicular**2)**0.5
#     print('base is', base)
# else:
#     ('invalid choice') 






# a = int(input('enter the first number'))
# b = int(input('enter the second number'))
# c = int(input('enter the third number'))
# d = int(input('enter the fourt nuber'))
# if a > b and  a > c and  a > d :
#     print(True,'a')
# elif b > a and b > c and  b > d:
#     print(True,'b') 
# elif c > a and c > b and  c > d:
#     print(True, 'c') 
# else : 
#     print(True,'d')         

# # for num in range (1,11):
# #     print(1*num,end =' , ' ) 
 
num = int(input('Enter a num hee : '))

count = 1
print('The multiplication table of : ', num)

while count<=10:
    num = num*1
    print (num, 'x', count, '=', num* count)
    count+=1 
    
    