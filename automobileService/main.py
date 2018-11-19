# Type your code here
auto_service = input('Enter desired auto service: \n')
print('You entered:', auto_service,) 

if (auto_service == 'Oil change') or (auto_service == 'Tire rotation') or (auto_service == 'Car wash'):
    if 'Oil change' in auto_service: 
        print('\nCost of oil change: $35')
    
    if 'Tire rotation' in auto_service: 
        print('\nCost of tire rotation: $19')
    
    if 'Car wash' in auto_service: 
        print('\nCost of car wash: $7')    
else: 
    print('\nError: Requested service is not recognized.')