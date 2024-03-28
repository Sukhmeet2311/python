number=7


while True:
    user_input = input("Would like to play ? (y/n) :").lower
    if user_input == "n":
        break
    user_number = int(input("guess the numbers: "))
    
    if user_number == number:
        print("Hurray u guessed it right")
    elif abs(number-user_number)==1:
        print("You were off by 1")
    else:
        print("Sorry badly wrong!")

list= ["sukhmeet", "singh", "python"]
