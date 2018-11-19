print ('Enter arrow base height: ')
arrow_base_height = int(input())
  
print ('Enter arrow base width: ')
arrow_base_width = int(input())
    
arrow_head_width = 0    
while arrow_head_width <= arrow_base_height: 
    print ('Enter arrow head width: ')
    arrow_head_width = int(input())

# Generate base by looping for the number vale of base height, printing for the number value of base width each line. 
for height in range(arrow_base_height): 
    for width in range(arrow_base_width):
        print('*', end='')
    print()

# Make arrow head by reducing number of stars printed per line each loop. 
i = arrow_head_width
while i > 0:
    for width in range(arrow_head_width): 
        print('*', end='')
    print()
    i -= 1
    arrow_head_width -= 1
    
