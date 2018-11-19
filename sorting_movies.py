directors = ['Munich, Steven Spielberg', 
             'The Prestige, Christopher Nolan', 
             'The Departed, Martin Scorsese', 
             'Into the Wild, Sean Penn', 
             'The Dark Knight, Christopher Nolan', 
             'Mary and Max, Adam Elliot', 
             'The King\'s Speech, Tom Hooper', 
             'The Artist, Michel Hazanavicius', 
             'The Help, Tate Taylor',
             'Argo, Ben Affleck', 
             '12 Years a Slave, Steve McQueen', 
             'Birdman, Alejandro G. Inarritu',
             'Spotlight, Tom McCarthy', 
             'The BFG, Steven Spielberg']

movie_dict = {directors[0] : '2005',
              directors[1] : '2006', 
              directors[2] : '2006', 
              directors[3] : '2007',
              directors[4] : '2008', 
              directors[5] : '2009', 
              directors[6] : '2010', 
              directors[7] : '2011', 
              directors[8] : '2011', 
              directors[9] : '2012',
              directors[10] : '2013', 
              directors[11] : '2014',
              directors[12] : '2015', 
              directors[13] : '2016', 
              }

menu = ('MENU\n'
        'Sort by:\n'
        'y - Year\n'
        'd - Director\n'
        't - Movie title\n'
        'q - Quit\n'
        )   

def choose_movie_year():
     user_input = input('Enter a year between 2005 and 2016:\n')
     if (user_input > '2016') or (user_input < '2005'): 
          print('N/A')
     else: 
          for director_and_movie, year in movie_dict.items(): 
               if year == user_input: 
                    print('%s' % director_and_movie)
          print()
     

def choose_menu_option():
     while True:
          print(menu)
          user_input = input('Choose an option:\n')
          if user_input == 'q':
               break
          elif user_input == 'y':
               last_year = None
               check = False
               for director_and_movie in range(len(directors)):
                    year = movie_dict.get(directors[director_and_movie])
                    if last_year == year:   
                        print('\t%s' % directors[director_and_movie])
                    elif check == True:
                         print('\n%s:\n\t%s' % (movie_dict.get(directors[director_and_movie]), 
                                         directors[director_and_movie]))
                         check = False
                    else:
                        print('%s:\n\t%s' % (movie_dict.get(directors[director_and_movie]), 
                                         directors[director_and_movie]))
                    last_year = year
                    check = True
               print()   
          elif user_input == 'd':
               names_list = []
               last_name = None 
               for director_and_movie in directors: 
                    movie, name = director_and_movie.split(',')
                    names_list.append([name.strip(), movie.strip()])
               names_list.sort()  
               check = False
               for index, name_and_movie in enumerate(names_list):
                    name = names_list[index][0]
                    movie = names_list[index][1]
                    dict_key = ('%s, %s' % (movie, name))
                    year = movie_dict[dict_key]
                    if last_name == name:
                         print('\t%s, %s' % (movie, year))
                    elif check == True:
                         print('\n%s:\n\t%s, %s' % (name, movie, year))
                         check = False
                    else:
                         print('%s:\n\t%s, %s' % (name, movie, year))
                    last_name = name
                    check = True
               print()
          elif user_input == 't': 
               names_list = []
               last_name = None 
               for director_and_movie in directors: 
                    movie, name = director_and_movie.split(',')
                    names_list.append([movie.strip(), name.strip()])
               names_list.sort()  
               check = False
               for index, movie_and_name in enumerate(names_list):
                    movie = names_list[index][0]
                    name = names_list[index][1]
                    dict_key = ('%s, %s' % (movie, name))
                    year = movie_dict[dict_key]
                    if last_name == name:
                         print('\t%s, %s' % (name, year))
                    elif check == True:
                         print('\n%s:\n\t%s, %s' % (movie, name, year))
                         check = False
                    else:
                         print('%s:\n\t%s, %s' % (movie, name, year))
                    last_name = name
                    check = True
               print()
                    
choose_movie_year()                    
               
choose_menu_option()        
