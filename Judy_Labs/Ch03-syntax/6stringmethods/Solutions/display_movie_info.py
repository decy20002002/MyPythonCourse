import sys

# get the file name
program_name = sys.argv[0]
print('original name\t\t', program_name)
print('uppercase\t\t',program_name.upper())
print('original name\t\t', program_name)
 
# replace underscores with space
program_name = program_name.replace('_',' ')
print('removed under\t\t', program_name)

# replace .\ if exists
program_name = program_name.replace('.\\','')
print('removed .\\\t\t', program_name)

# replace .py if exists
program_name = program_name.replace('.py','')
print('removed .py\t\t', program_name)

#upper
program_name = program_name.upper()
print('upper\t\t', program_name)

welcome_message = 'Welcome to {}'
welcome_message = welcome_message.format(program_name)
print(welcome_message)

# use center to display of certain width
print('length is', len(program_name))
welcome_message = welcome_message.center(len(welcome_message)*3,'*')
print(welcome_message)

movie = input("What is your favorite movie? ")

good_year = False

while not good_year:
    year = input("What year is your favorite movie from? ")

    if(year.isdecimal()):
        good_year = True
    else:
        print('Please enter a valid year')


movie = movie.title()
print(movie)

#put in after testing and seeing spaces are weird
movie = movie.strip()
print(movie)

message = "In {}, the movie {} debuted"
print(message.format(year, movie))

movie = movie.strip()
print(movie)

message = "In {}, the movie {} debuted"
print(message.format(year, movie))

