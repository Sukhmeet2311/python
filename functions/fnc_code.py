def hello():
    print("Hello")

hello()
print(hello())   

def user_age_in_seconds():
    user_age=int(input("enter ur age: "))
    age_seconds = user_age* 365 *24 * 60 * 60
    print(f"Your age in seconds {age_seconds}")

user_age_in_seconds()

friends = ["Rolf", "Neil"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    friends.append(friend_name)
    print(friends)
    friends_local = friends
    print(friends_local)

add_friend()
