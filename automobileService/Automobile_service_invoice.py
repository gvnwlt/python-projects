# Davy's Auto Shop Services
print('Davy\'s auto shop services\n'
      'Oil change -- $35\n'
      'Tire rotation -- $19\n'
      'Car wash -- $7\n'
      'Car wax -- $12\n')
# Select first service       
first_service = input('Select first service: \n')
# Select second service
second_service = input('\nSelect second service: ')
# Start invoice process 
print('\n\n\nDavy\'s auto shop invoice\n') 
# Check first service.  
if 'Oil change' in first_service:
    first_serv_amt = 35
    print('Service 1:', first_service + ', $' +  str(first_serv_amt))
elif 'Tire rotation' in first_service:
    first_serv_amt = 19
    print('Service 1:', first_service + ', $' +  str(first_serv_amt))
elif 'Car wash' in first_service:
    first_serv_amt = 7
    print('Service 1:', first_service + ', $' +  str(first_serv_amt))
elif 'Car wax' in first_service:
    first_serv_amt = 12
    print('Service 1:', first_service + ', $' +  str(first_serv_amt))
elif '-' in first_service:
    print('Service 1: No service')
    first_serv_amt = 0
# Check second service.
if 'Oil change' in second_service:
    second_serv_amt = 35
    print('Service 2:', second_service + ', $' +  str(second_serv_amt))
elif 'Tire rotation' in second_service:
    second_serv_amt = 19
    print('Service 2:', second_service + ', $' +  str(second_serv_amt))
elif 'Car wash' in second_service:
    second_serv_amt = 7
    print('Service 2:', second_service + ', $' +  str(second_serv_amt))
elif 'Car wax' in second_service:
    second_serv_amt = 12
    print('Service 2:', second_service + ', $' +  str(second_serv_amt))
elif '-' in second_service: 
    print('Service 2: No service')
    second_serv_amt = 0
# Print final total. 
print('\nTotal: $' +  str((int(first_serv_amt + second_serv_amt))))



