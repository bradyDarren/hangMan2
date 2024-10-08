import random

print("                             ...,?77??!~~~~!???77?<~.... ")
print("                        ..?7`                           `7!.. ")
print("                    .,=`          ..~7^`   I                  ?1. ")
print("       ........  ..^            ?`  ..?7!1 .               ...??7 ")
print("      .        .7`        .,777.. .I.    . .!          .,7! ")
print("      ..     .?         .^      .l   ?i. . .`       .,^ ")
print("       b    .!        .= .?7???7~.     .>r .      .= ")
print("       .,.?4         , .^         1        `     4... ")
print("        J   ^         ,            5       `         ?<. ")
print("       .%.7;         .`     .,     .;                   .=. ")
print("       .+^ .,       .%      MML     F       .,             ?, ")
print("        P   ,,      J      .MMN     F        6               4. ")
print("        l    d,    ,       .MMM!   .t        ..               ,, ")
print("        ,    JMa..`         MMM`   .         .!                .; ")
print("         r   .M#            .M#   .%  .      .~                 ., ")
print("       dMMMNJ..!                 .P7!  .>    .         .         ,, ")
print("       .WMMMMMm  ?^..       ..,?! ..    ..   ,  Z7`        `?^..  ,, ")
print("          ?THB3       ?77?!        .Yr  .   .!   ?,              ?^C ")
print("            ?,                   .,^.` .%  .^      5. ")
print("              7,          .....?7     .^  ,`        ?. ")
print("                `<.                 .= .`'           1 ")
print("                ....dn... ... ...,7..J=!7,           ., ")
print("             ..=     G.,7  ..,o..  .?    J.           F ")
print("           .J.  .^ ,,,t  ,^        ?^.  .^  `?~.      F ")
print("          r %J. $    5r J             ,r.1      .=.  .% ")
print("          r .77=?4.    ``,     l ., 1  .. <.       4., ")
print("          .$..    .X..   .n..  ., J. r .`  J.       `' ")
print("        .?`  .5        `` .%   .% .' L.'    t ")
print("        ,. ..1JL          .,   J .$.?`      . ")
print("                1.          .=` ` .J7??7<.. .; ")
print("                 JS..    ..^      L        7.: ")
print("                   `> ..       J.  4. ")
print("                    +   r `t   r ~=..G. ")
print("                    =   $  ,.  J ")
print("                    2   r   t  .; ")
print("              .,7!  r   t`7~..  j.. ")
print("              j   7~L...$=.?7r   r ;?1. ")
print("               8.      .=    j ..,^   .. ")
print("              r        G              . ")
print("            .,7,        j,           .>=. ")
print("         .J??,  `T....... %             .. ")
print("      ..^     <.  ~.    ,.             .D ")
print("    .?`        1   L     .7.........?Ti..l ")
print("   ,`           L  .    .%    .`!       `j, ")
print(" .^             .  ..   .`   .^  .?7!?7+. 1 ")
print(".`              .  .`..`7.  .^  ,`      .i.; ")
print(".7<..........~<<3?7!`    4. r  `          G% ")
print("                          J.` .!           % ")
print("                            JiJ           .` ")
print("                              .1.         J ")
print("                                 ?1.     .' ")
print("                                     7<..% ")

print("\n\nThis game of Hangman is pertaining to the classic tv show/movie/video game Sonic the Hedgehog.")

# List of word the user could possible be given. 
sonic_list = [
    "sonic the hedgehog",
    "tails",
    "knuckles",
    "dr. robotnik",
    "chaos emeralds",
    "green hill zone",
    "super sonic",
    "amy rose",
    "shadow the hedgehog",
    "chili dogs"
]

# random generation of a word from sonic_list. 
rand_word = random.choice(sonic_list)
# designation of the max amount of lives a player is allowed to have.
max_lives = 6

# function used to determine the amount of blank spaces displayed according to the generated random word.
def blank_spaces(word):
    blanks = []
    for x in word:
        if x == " ":
            blanks += " "
        elif x == "-":
            blanks += "-"
        elif x == ".":
            blanks += "."
        else:
            blanks += "_"
    return blanks

#TEST
print(rand_word)

blank_word = blank_spaces(rand_word)

while max_lives > 0:
    # Showing the player the amount of spaces within the word.
    print("".join(blank_word))
    user_guess =  input("Guess a letter: ")
    if user_guess in rand_word: 
        for i, char in enumerate(rand_word):
            if char == user_guess:
                blank_word[i] = user_guess
                print(f"your letter {user_guess} was in our word. Has been added")
                print(f"***************{max_lives}/6 remaining***************")
    elif user_guess not in rand_word: 
        max_lives -= 1
        print(f"your letter {user_guess} was not in our word. Lose a life.")
        print(f"***************{max_lives}/6 remaining***************")

    if "_" not in blank_word: 
        print(f"Congrats you did it with {max_lives} lives left.")
        break
    
    if max_lives == 0: 
        print(f"Game over. You have used all of your lives.")
        


            







