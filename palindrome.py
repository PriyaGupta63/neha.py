num = int(input("Enter any number: "))
temp = num

rev = 0

while temp!=0:
    rem = temp%10
    temp = temp//10
    rev = rev * 10 + rem

if num == rev:
    print("Is a palendrome number.")
else: 
    print("Is not a palendrome number")