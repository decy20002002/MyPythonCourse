import sys

# geet the file name
program_name = sys.argv[0]
print('original name\t\t', program_name)
print('uppercase name\t\t', program_name.upper())
print('uppercase name\t\t', program_name.capitalize())

# replace _ if exists
program_name = program_name.replace('_', ' ')
print('removed underscore\t', program_name.upper())

# replace .py if exists
program_name = program_name.replace('.py', '')
print('removed .py\t\t', program_name.upper())

# UPPER case
# welcome_message = f'Welcome to {program_name}'
welcome_message = 'Welcome to {}'
welcome_message = welcome_message.format(program_name.upper())
print(welcome_message)

# user center to display of certain width
print('length is', len(program_name))
welcome_message = welcome_message.center(len(welcome_message)*2, '*')
print(welcome_message)

# str.isdecimal()
good_year = False

movie = input("What is your favorite movie? ")
movie = movie.strip() #strip out any leading and trailing spaces 

while not good_year:
    year = input("What year is your favorite movie from? ")
    
    if(year.isdecimal()):
        good_year = True
        message = "In {}, the movie {} debuted"
        #print(str(movie))
        #print("Your favorite movie from", str(year))
        print(movie)
        print(message.format(year, movie))
    else:
        print('Please enter a valid year')