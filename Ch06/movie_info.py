
def print_movie_info(movie,year):
    print(f'The movie {movie} is from {year}')
    
favorite_movie = "Stars"
movie_year = int(1999)

print_movie_info(favorite_movie,movie_year)

def movie_info(movie,year):
    if(year>1900):
        return f'The movie {movie} is from {year}'
    else:
        print('Invalid year')

favorite_movie = "Stars"
movie_year = int(1999)

movie_info(favorite_movie,movie_year)

#call function from within a loop
#define the movie dictionary
movie_list = [
                {"year":1980,"name":"MP Movie #1"},
                {"year":1981,"name":"MP Movie #2"},
                {"year":1982,"name":"MP Movie #3"},
            ]

for movie in movie_list:
    print_movie_info(movie["name"], movie["year"])
