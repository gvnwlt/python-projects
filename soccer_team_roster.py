count = 5
roster = {}
jersey_list = [] 

for num in range(count):
    jersey_input = int(input('Enter player %s\'s jersey number: \n' % (num + 1)))
    rating_input = input('Enter player %s\'s rating: \n\n' % (num + 1))
    jersey_list.append(jersey_input) 
    roster[jersey_input] = rating_input

print('ROSTER')

jersey_list.sort()

for jersey_num in jersey_list: 
    print('Jersey number: %s, Rating: %s' % (jersey_num, roster[jersey_num]))
    
print()
    
menu = ('MENU\n'
       'a - Add player\n'
       'd - Remove player\n'
       'u - Update player rating\n'
       'r - Output players above a rating\n'
       'o - Output roster\n'
       'q - Quit\n')    
print(menu)

option_select = input('Choose an option: \n').strip().lower()

def outputRoster():
    print('ROSTER')
    jersey_list.sort()
    for jersey_num in jersey_list: 
        print('Jersey number: %s, Rating: %s' % (jersey_num, roster[jersey_num]))
    print()
    print(menu)
        
def addPlayer():
    jersey_input = int(input('Enter a new players jersey number: \n'))
    rating_input = input('Enter the player\'s rating: \n') 
    jersey_list.append(jersey_input) 
    roster[jersey_input] = rating_input
    
def deletePlayer(): 
    jersey_input = int(input('Enter a jersey number: \n')) 
    jersey_list.remove(jersey_input)
    del roster[jersey_input] 
    
def updatePlayer():
    jersey_input = int(input('Enter a jersey number: \n')) 
    rating_input = input('Enter a new rating for player: \n')
    roster[jersey_input] = rating_input
    
def outputAboveRating():
    rating_input = input('Enter a rating: ')
    print('ABOVE %s' % rating_input) 
    for jersey_num, rating in roster.items():
        if rating > rating_input:
            print('Jersey number: %s, Rating: %s' % (jersey_num, rating))
    print()
    print(menu)        
             
while True:      
     if option_select == 'o':
         outputRoster()
         option_select = input('Choose an option: \n').strip().lower()
     elif option_select == 'a':
         addPlayer()
         option_select = input('Choose an option: \n').strip().lower()
     elif option_select == 'd': 
         deletePlayer()
         option_select = input('Choose an option: \n').strip().lower()
     elif option_select == 'u':
         updatePlayer()
         option_select = input('Choose an option: \n').strip().lower()
     elif option_select == 'r':
          outputAboveRating()
          option_select = input('Choose an option: \n').strip().lower()
     elif option_select == 'q': 
          break     
    
