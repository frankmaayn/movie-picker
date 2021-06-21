import random

# Opens and reads the movie list
my_file = open("movie-list.txt", "r")
content = my_file.read()
movie_list = content.split('\n')
my_file.close()

# Get a random number
random_index = random.randint(0,len(movie_list)-1)

# Get a movie
chosen_movie = movie_list[random_index]


# Remove the chosen movie from the list
movie_list.remove(chosen_movie)

# Show Result
print('Total number of movies left to watch: ',len(movie_list))
print('The movie you are going to watch is: ',chosen_movie)

# Update and save the list
textfile = open("movie-list.txt", "w")
for element in movie_list:
    textfile.write(element + '\n')
textfile.close()