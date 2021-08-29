import playsound
import random


def winner_sound():
    winner_music = "electro-win-sound.wav"
    try:
        playsound.playsound(winner_music)
    except Exception as e:
        print(e)

def draw_sound():
    draw_music = "draw.mpeg"
    try:
        playsound.playsound(draw_music)
    except Exception as e:
        print(e)

def looser_sound():
    looser_music = "lose.mpeg"
    try:
        playsound.playsound(looser_music)
    except Exception as e:
        print(e)

def win_sound():
    win_music = "win2.mpeg"
    try:
        playsound.playsound(win_music)
    except Exception as e:
        print(e)


def lose_sound():
    lose_music = "negative-failure.mp3"
    try:
        playsound.playsound(lose_music)
    except Exception as e:
        print(e)


print('\033[1m' + '\033[4m' + '\033[95m' + "\nWelcome to Stone-Paper-Scissor Game\n" + '\033[0m')
# print("aef")
user = 0
comp = 0
attempt = 0
while attempt <= 5:
    lst = ["scissor", "paper", "stone"]
    rand = random.choice(lst)

    inp = (input(
        '\033[1m' + '\033[94m' + '\033[1m' + "\n\t\t(Stone or Paper or Scissor) \nenter your choice: " + '\033[0m'))
    inp = inp.lower()

    if inp == rand:
        print('\033[36m' + "\nIts a Tie" + '\033[0m')
        user = user + 0
        comp = comp + 0
        attempt += 1

    elif inp == "stone" and rand == "paper":
        print('\033[91m' + "\nYou Lost this Round" + '\033[0m')
        lose_sound()
        user = user + 0
        comp = comp + 1
        attempt += 1
        print(f"\nYou Entered: {inp}\t||\tComputer Entered: {rand}")
        print(f"\nYour Points:{user}"
              f"\t||\tComputer Points:{comp}")

    elif inp == "stone" and rand == "scissor":
        print('\033[92m' + "\nYou win this Round" + '\033[0m')
        win_sound()
        print(f"\nYou Entered: {inp}\t||\tComputer Entered: {rand}")
        user = user + 1
        comp = comp + 0
        attempt += 1
        print(f"\nYour Points:{user}"
              f"\t||\tComputer Points:{comp}")
    elif inp == "paper" and rand == "scissor":
        print('\033[91m' + "\nYou lost this Round" + '\033[0m')
        lose_sound()
        user = user + 0
        comp = comp + 1
        attempt += 1
        print(f"\nYou Entered: {inp}\t||\tComputer Entered: {rand}")
        print(f"\nYour Points:{user}"
              f"\t||\tComputer Points:{comp}")

    elif inp == "paper" and rand == "stone":
        print('\033[92m' + "\nYou Win this Round" + '\033[0m')
        win_sound()
        user = user + 1
        comp = comp + 0
        attempt += 1
        print(f"\nYou Entered: {inp}\t||\tComputer Entered: {rand}")
        print(f"\nYour Points:{user}"
              f"\t||\tComputer Points:{comp}")

    elif inp == "scissor" and rand == "paper":
        print('\033[92m' + "\nYou Win this Round" + '\033[0m')
        win_sound()
        user = user + 1
        comp = comp + 0
        attempt += 1
        print(f"\nYou Entered: {inp}\t||\tComputer Entered: {rand}")
        print(f"\nYour Points:{user}"
              f"\t||\tComputer Points:{comp}")

    elif inp == "scissor" and rand == "stone":
        print('\033[91m' + "\nYou lost this Round" + '\033[0m')
        lose_sound()
        user = user + 0
        comp = comp + 1
        attempt += 1
        print(f"\nYou Entered: {inp}\t||\tComputer Entered: {rand}")
        print(f"\nYour Points:{user}"
              f"\t||\tComputer Points:{comp}")

    else:
        print("\nInvalid Input. Please Try Again!")
        continue
    print(f"\nNo. of Guesses left: {5 - attempt}")
else:
    print('\033[4m' + '\033[94m' + '\033[1m' + "\nFinal Result" + '\033[0m')
    print(f"\nYour Points:{user}\t|| Computer Points:{comp}")
    if user > comp:
        print('\033[92m' + '\033[1m' + "\nYou won the Match" + '\033[0m')
        winner_sound()
    elif user < comp:
        print('\033[91m' + '\033[1m' + "\nYou lost the Match." + '\033[0m')
        looser_sound()
    else:
        print('\033[94m' + '\033[1m' + "\nMatch is Tied." + '\033[0m')
        draw_sound()