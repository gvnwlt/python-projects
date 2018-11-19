# Prompt the user for a title for data. Output the title. (1 pt) 
user_input = input('Enter a title for the data: \n') 
title = user_input
print('You entered:', user_input)
print()

# Prompt the user for the headers of two columns of a table. Output the column headers. (1 pt) 
user_input = input('Enter the column 1 header: \n') 
column1 = user_input
print('You entered:', column1) 
print()

user_input = input('Enter the column 2 header: \n') 
column2 = user_input
print('You entered:', column2) 
print()

# Prompt the user for data points. Data points must be in this format: string, int. 
# Store the information before the comma into a string variable and the information after 
# the comma into an integer. The user will enter -1 when they have finished entering data 
# points. Output the data points. Store the string components of the data points in a list
# of strings. Store the integer components of the data points in a list of integers. (4 pts) 
user_input = input('Enter a data point (-1 to stop input): \n')
input_split = user_input.split(',')
first_input = input_split[0].strip()
if len(input_split) > 1:
    second_input = input_split[1].strip()
data_list = []
int_list = []
entry_count = 0 
while user_input != '-1': 
    if ',' not in user_input: 
        print('Error: No comma in string.\n')
        user_input = input('Enter a data point (-1 to stop input): \n')
        input_split = user_input.split(',')
        first_input = input_split[0].strip()
        if len(input_split) > 1:
            second_input = input_split[1].strip()
    elif user_input.count(',') > 1: 
        print('Error: Too many commas in input.\n')
        user_input = input('Enter a data point (-1 to stop input): \n')
        input_split = user_input.split(',')
        first_input = input_split[0].strip()
        if len(input_split) > 1:
            second_input = input_split[1].strip()
    elif second_input.isdigit() == False:
        print('Error: Comma not followed by an integer.\n') 
        user_input = input('Enter a data point (-1 to stop input): \n')
        input_split = user_input.split(',')
        first_input = input_split[0].strip()
        if len(input_split) > 1:
            second_input = input_split[1].strip()
    else: 
        print('Data string:', first_input)
        print('Data integer:', second_input)
        print()
        data_list.append(first_input)
        int_list.append(second_input)
        entry_count += 1
        user_input = input('Enter a data point (-1 to stop input): \n')
        input_split = user_input.split(',')
        first_input = input_split[0].strip()
        if len(input_split) > 1:
            second_input = input_split[1].strip()
print()  
    
# Output the information in a formatted table. The title is right justified with a minimum 
# field width value of 33. Column 1 has a minimum field width value of 20. Column 2 has a 
# minimum field width value of 23. (3 pts)     
print('%33s' % title) 
print('%-20s|%23s' % (column1,column2)) 
print('-' * 44)
for entry in range(entry_count):
    print('%-20s|%23s' % (data_list[entry], int_list[entry]))
print()

# Output the information as a formatted histogram. Each name is right justified with a 
# minimum field width value of 20. (4 pts) 
for entry in range(entry_count): 
    novel_num = '*' * int(int_list[entry])
    print('%20s %s' % (data_list[entry], novel_num)) 
    
    
    
    
    
    
    
    
    
