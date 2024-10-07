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
    "Sonic the Hedgehog",
    "Tails",
    "Knuckles",
    "Dr. Robotnik",
    "Chaos Emeralds",
    "Green Hill Zone",
    "Super Sonic",
    "Amy Rose",
    "Shadow the Hedgehog",
    "Chili Dogs"
]

rand_word = random.choice(sonic_list)
max_lives = 6

def blank_spaces(word):
    blanks = []
    for x in word:
        if x == " ":
            blanks += " "
        elif x == "-":
            blanks += "-"
        else:
            blanks += "_"
    return "".join(blanks)

def guess_word(char, blanks):
    while "_" in blanks or max_lives != 0:
        user_guess = input("Guess a word: ")
        if user_guess in rand_word:
            blank_spaces(rand_word[user_guess])
            


            







