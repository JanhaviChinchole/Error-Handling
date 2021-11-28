
try:
    while True:
        user_input=int(input("enter an integer: "))
        if user_input%2!=0:
            print("This number is odd")
            break
        else:
            print("This number is even please try again")
except Exception as e:
    print(e)

#second way
while True:
    try:
        number=int(input("enter an integer: "))
        print(number)
        break
    except ValueError:
        print("whoops! thats not a number try again")
        continue