import random

debug = 0
lines = 0

f = open("sowpods.txt","r")
f1 = f.readlines()

for line in f1:
    lines += 1

chosen_num = random.randint(0, lines)

if debug == 1:
    print(lines)
    print(chosen_num)
    print(f1[chosen_num])
#word = "shoopy"    
word = f1[chosen_num].lower()
print(word)
print(isinstance(word, str))

game_over = False

#prints out the blank space words
for letter in word:
    print("_", end = " ")
print("\n")

def sort_guesses(player_guess, word, correct_letters, wrong_letters):
    ordered_letters=[]
    match = False
    print("You guessed: %s" %player_guess)
    for i in word:
        if i == player_guess:
            for k in correct_letters:
                if k == player_guess:
                    print("You already got that one!")
            print("Correct!")
            correct_letters.append(i)
            match = True
    if not match:
        for j in wrong_letters:
            if j == player_guess:
                print("You already guess that! Try again!")
        print("Incorrect!")
        wrong_letters.append(player_guess)

    for x in word:
        for y in correct_letters:
            if x == y:
                ordered_letters.append(x)
                break
        if x != y:
            ordered_letters.append("_")
    #print(ordered_letters)
    compare_string = ''.join(ordered_letters)
    print_string = ' '.join(ordered_letters)
    print(print_string)
    if compare_string == word:
        print("You got the word!")
        game_over = True
        return game_over

correct_letters = []
wrong_letters = []

while not game_over:
    player_guess = input("What is your guess?")
    if sort_guesses(player_guess, word, correct_letters, wrong_letters):
        game_over = True



           
