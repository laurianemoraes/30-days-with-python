word = "days"
guess = ""
guess_count = 0 #number of tries
guess_limit = 3 # limit of guesses
out_of_guesses = False #if the usuario have or no more guesses

while guess != word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lose !!! Good luck next time ")
else:
    print("you got it !!!")

