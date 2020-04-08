command=""
flag=False
while True:
    command=input('> ').lower()
    if command =="start":
        if flag:
            print("Car is already started")
        else:
            flag=True
            print("car started")

    elif command =="stop":
        if not flag:
            print("Car is alredy stopped")
        else:
             flag=False
             print("Car stopped")
    elif command=="help":
        print("""start-to start the car
    stop-to stop the car
    quit-to quit""")
    elif command =="quit":
        break
    else:
        print("Sorry,I don't understand this")
