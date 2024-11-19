import random
import time

# Introduction to the game
def introduction():
    print("Welcome to ReRun, where you will solve a series of riddles as you progress and then finally escape with your pet.")
    input("Press Enter to start...")
    start_game()

# Player status
def initialize_player():
    return {"health": 100, "pet": None, "inventory": []}

# Reviving the player
def respawn(player, stage="first"):
    player["health"] = 100
    print("\nYou have been revived.")
    if stage == "first":  # Respawn in the first stage
        print("You have returned to the starting point.")
        choose_room(player)
    elif stage == "second":  # If you are in the second stage
        print("You have returned to the second stage with rooms labeled 4, 5, and 6.")
        second_stage(player)

# Starting the game
def start_game():
    player = initialize_player()
    choose_room(player)

# Picking the room
def choose_room(player):
    while True:
        print("\nYou are standing in front of three rooms labeled 1, 2, and 3.")
        choice = input("Please select a room (1, 2, or 3): ")
        if choice == '1':
            room_one(player)
        elif choice == '2':
            room_two(player)
        elif choice == '3':
            room_three(player)
        else:
            print("Invalid choice. Try again.")

# Room 1 - Death trap
def room_one(player):
    print("You have come face to face with the Kraken. He twists your legs and eats them up...you died.")
    player["health"] = 0
    respawn(player)

# Room 2 - Riddle and pet reward
def room_two(player):
    print("You have entered Room 2.")
    riddle = "What goes up but doesn't come down?"
    answer = "age"
    hint = "Think, how long have you lived?"
    # Variable that decides if the player has passed or not
    success = attempt_riddle(player, riddle, answer, hint, pet_name="squirrel")
    if success:
        print("\nA portal opens up to the next stage.")
        second_stage(player)
    else:
        respawn(player)

# Room 3 - Empty room with crates
def room_three(player):
    print("The room is empty and there seems to be some crates. Do you wish to search the crates?")
    choice = input("Type 'yes' to search or 'no' to return: ").lower()
    if choice == "yes":
        print("You look through the crates and find a raggedy cloak. Wear it?")
        wear_choice = input("Type 'yes' to wear or 'no' to leave it: ").lower()
        if wear_choice == "yes":
            player["inventory"].append("cloak")
            print("You wear the raggedy cloak.")
    print("Returning to the starting point...")
    choose_room(player)

# Second stage with new rooms 4, 5, and 6
def second_stage(player):
    print("\nYou arrive at the next stage with three new rooms labeled 4, 5, and 6.")
    while True:
        choice = input("Please select a room (4, 5, or 6): ")
        if choice == '4':
            room_four(player)
        elif choice == '5':
            room_five(player)
        elif choice == '6':
            room_six(player)
        else:
            print("Invalid choice. Try again.")

# Room 4 - Riddle with chimera and pet hint
def room_four(player):
    print("You are faced with a chimera that's half medusa and a frog. It's fast and deadly. Hurry and solve the riddle to escape!")
    riddle = "What has to be broken before you use it?"
    answer = "egg"
    hint = "Think of chickens."
    
    print(r"""
           .--._.--.
          ( O     O )
          /   . .   \
         .`._______.'.
        /(           )\
      _/  \  \   /  /  \_
   .~   `  \  \ /  /  '   ~.
  {    -.   \  V  /   .-    }
_ _`.    \  |  |  |  /    .'_ _
>_       _} |  |  | {_       _<
 /. - ~ ,_-'  .^.  `-_, ~ - .\
         '-'|/   \|`-`
    """)

    # First attempt
    success = attempt_riddle(player, riddle, answer, hint)
    
    if success:
        print("The squirrel helps you defeat the chimera. A new portal opens to the final level...")
        final_stage(player)
    else:
        print("The chimera attacks you, and you lose half your health.")
        player["health"] -= 50
        
        # Check if player still has health to retry
        if player["health"] > 0:
            retry = input("Do you want to try again with a hint from your pet? (yes/no): ").lower()
            if retry == "yes":
                print("The squirrel says: Think of chickens.")
                # Second attempt with a hint
                success = attempt_riddle(player, riddle, answer, hint)
                if success:
                    print("You defeated the chimera and move on!")
                    final_stage(player)
                else:
                    print("Lava pours down on you, and you die.")
                    player["health"] = 0
                    respawn(player, stage="second")
            else:
                print("Okay, please guess the correct answer.")
                success = attempt_riddle(player, riddle, answer, hint)
                if success:
                    print("You defeated the chimera and move on!")
                    final_stage(player)
                else:
                    print("Lava pours down on you, and you die.")
                    player["health"] = 0
                    respawn(player, stage="second")
        else:
            respawn(player, stage="second")

# Room 5 - Redirect to Room 4
def room_five(player):
    print("This room redirects you to Room 4.")
    room_four(player)

# Room 6 - Death trap
def room_six(player):
    print("You entered a trap room and got crushed by falling rocks. You died.")
    player["health"] = 0
    respawn(player, stage="second")

# Final stage with SongBird
def final_stage(player):
    print("\nYou have arrived in the final stage. You are face to face with the strongest foe, the SongBird.")
    riddle = "The more you take, the more you leave behind."
    answer = "footsteps"
    hint = "Every time you take a step, what do you leave behind?"
    print(r"""   \\
   (o>
\\_//)
 \_/_)
  _|_



""")
    # First riddle attempt
    success = attempt_riddle(player, riddle, answer, hint)
    
    if success:
        print("Congrats! You have escaped ReRun with your pet. Thanks for playing!")
    else:
        print("Oh no! SongBird altered your mind, and you have to solve two riddles now!")
        riddle_two = "What has hands but can't clap?"
        answer_two = "clock"
        
        print("\nRiddle 1:", riddle)
        guess_one = input("Your guess: ")
        if guess_one.lower() == answer:
            print("Good job! You've solved the first riddle.")
        else:
            print("SongBird has confused you more!")
        
        print("\nRiddle 2:", riddle_two)
        guess_two = input("Your guess: ")
        if guess_two.lower() == answer_two:
            print("You've escaped with your pet. Well done!")
        else:
            print("SongBird defeated you... You have to start again from the final stage.")
            final_stage(player)

# Function to attempt a riddle with hint and pet reward
def attempt_riddle(player, riddle, answer, hint, pet_name=None):
    print("\nRiddle:", riddle)
    guess = input("Your guess: ")
    if guess.lower() == answer:
        if pet_name:
            print(f"\nYou guessed correctly! You got a pet {pet_name}.")
            player["pet"] = pet_name
        return True
    else:
        print("Oops, sorry that is wrong. Try again.")
        print("Hint:", hint)
        second_guess = input("Your second guess: ")
        if second_guess.lower() == answer:
            if pet_name:
                print(f"\nYou guessed correctly! You got a pet {pet_name}.")
                player["pet"] = pet_name
            return True
        else:
            print("Lava pours down on you, and you die.")
            player["health"] = 0
            return False

# Start the game
introduction()
