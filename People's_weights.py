count = 4
weights_list = []

for num in range(count): 
    user_input = input('Enter weight %s: \n' % int(num + 1)).strip()
    weights_list.append(float(user_input)) 
   
print()     
print('Weights: %s' % weights_list)   

average_weight = sum(weights_list) / count
print('Average weight: %s' % average_weight) 
max_weight = max(weights_list)
print('Max weight: %s' % max_weight) 

print()
user_input = int(input('Enter a list index (1 - 4): \n'))
chosen_weight = weights_list[user_input - 1]
print('Weight in pounds: %s' % chosen_weight)
converted_weight = chosen_weight / 2.2
print('Weight in kilograms: %s\n' % converted_weight) 


weights_list.sort()
print('Sorted list: %s' % weights_list) 