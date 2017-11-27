# This code will determine if the "Starting Number" has a winning advantage.
# The thought behind this is based on the total number of possible
# paths combinations to complete the game (the variable used is named "reps").
# If the number of combinations is 2, the number you select will always win.
# If the number of combinations is 4, you will always lose.
# If the number of combinations is above 4 but equal to or below 10, you could
# win or lose depending on your opponent's moves.
# If the number of combinations is above 10, the game is too complex at this
# point to determine the winner or loser.


# This is the recursive function:
def game_winner(n):
    if n<1:
        return 1
    else:
        return game_winner(n-1) + game_winner(n/2)

# This is the interface where you enter your starting number:
y = input("Enter your Starting Number: ")

# This runs the function and saves the output as a variable:
reps = game_winner(y)

# This if statement interprets the variable and determines the winner or loser:
if reps == 1:
    print "This number is too small to play this game."
elif reps <= 2:
    print "This number is cold, and you will always win."
elif reps <= 4:
    print "This number is hot, and you will always lose."
elif reps <=10:
    print "This number is hot, but you could still win depending on your opponent's move."
else:
    print "This number is cold, and you could win or lose."
    print "There are", reps,"possible path combinations in this game."
