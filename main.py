from random import choice

choices = {
    'R': "rock",
    'P': "paper",
    'S': "scissors"
}


def user():
    print("""
    Please choose one of the following:
    R for rock
    P for paper
    S for scissors
    """)
    choice = input("Enter your choice: ").upper()
    while choice not in choices.keys():
        print('''
.........................................
     XXX Your input is incorrect. Try again!
.........................................
        ''')
        choice = user()
    return choice


def computer():
    options = ["R", "P", "S"]
    value = choice(options)
    return value


def play_game():
    user_input = user()
    computer_input = computer()
    print(
        f'Player ({choices[user_input].upper()}) : CPU ({choices[computer_input].upper()})')
    if user_input == computer_input:
        print("It's a TIE")
    elif user_input == 'R' and computer_input == "S":
        print("Player wins")
    elif user_input == 'S' and computer_input == "R":
        print("CPU wins")
    elif user_input == 'R' and computer_input == "P":
        print("CPU wins")
    elif user_input == 'P' and computer_input == "R":
        print("Player wins")
    elif user_input == 'P' and computer_input == "S":
        print("CPU wins")
    elif user_input == 'S' and computer_input == "P":
        print("Player wins")
    else:
        print("Something went wrong, Play again!")


play_game()
