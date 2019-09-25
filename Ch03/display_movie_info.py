import sys

# geet the file name
program_name = sys.argv[0]
print('original name\t\t', program_name)
print('uppercase name\t\t', program_name.upper())
print('uppercase name\t\t', program_name.capitalize())

program_name = program_name.replace('_', ' ')
print('removed underscore\t\t', program_name)
