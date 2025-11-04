# movies=["Tom and Jerry", "Captain Bolt", "The terminator"]
# for movie in movies:

#      print(f"I like {movie}")

movies=[]

# while movie_name!="done":
#     movie_name=input("Please enter a movie: ")
#     movies.append(movie_name)
# movies.remove("done")   
# print(f"you have entered the following movies{movies}")

while True:
    movie_name=input("Please enter a movie (type done to finish)")
    if movie_name.lower()=="done":
        break
    movies.append(movie_name)
print(f"You have entered the following movies : {movies}")