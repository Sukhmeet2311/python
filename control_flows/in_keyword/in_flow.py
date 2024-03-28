movies_watched= {"the matrix", "Green Book", "Her"}
user_movie= input("Enter the move u watched recently")
print (user_movie in movies_watched)

if (user_movie in movies_watched):
    print (f"I have watched {user_movie} too!")
else:    
    print (f"I have not watched {user_movie}")