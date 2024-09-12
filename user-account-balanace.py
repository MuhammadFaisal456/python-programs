# program to get user input as 
# when deposit an amount 
# and want to know new account balance

balance = 945.70

# taking input as a string, it will generate an error 

num = input('Deposit: ')
balance += num
print(f'Balance: {balance}')

balance = 945.70
num = float(input('Deposit: '))
balance += num
print(f'Balance: {balance}')

# Error free program
balance = 945.70
# Now if take input as a float, it will not generate an error
while True:
    try:
        num = float(input('Deposit: '))
        break
    except ValueError:
        print('Must be a valid quantity')
    
balance += num
print(f'Balance: {balance}')