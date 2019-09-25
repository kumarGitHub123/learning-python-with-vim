command = ""
car_started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("Car is already started!")
        else:
            car_started = True
            print("Car started. Ready to go!")
    elif command == "stop":
        if not car_started:
            print("Car is already stopped!")
        else:
            car_started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        if car_started == True:
            print("You need to stop the car before quitting")
        else:
            break
    else:
        print("Sorry, I don't understand that")
