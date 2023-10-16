print("you stand at a cross road")
print("do you go left or right?")
while True:
    N1choice = input("> ")

    if N1choice == "right":
        while True:
            print("You find a staircase. Do you want to go up or down?")
            N2choice = input("> ")

            if N2choice == "up":
                print("You found the sky!")
                break
            elif N2choice == "down":
                print("You found the bottom!")
                break
            else:
                print("Invalid input. Please enter 'up' or 'down'.")

        break

    elif N1choice == "left":
        print("you found nothing else")
        break
    else:
        print("Invalid input. Please enter 'left' or 'right'.")
