from _datetime import datetime


def hello():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    split_time = current_time.split(':')

    H = split_time[0]

    if (int(H) < 12) & (int(H) > 00):
        print("Bonjour !")
    elif (int(H) < 14) & (int(H) > 12):
        print("Bon app !")
    elif (int(H) < 18) & (int(H) > 00):
        print("Bonsoir !")

def mirror():

    phrase = input("votre phrase a l'envers : ")
    alenvere = phrase[::-1]

    if alenvere == phrase:
        print("votre mot a l'enver est :", alenvere)
        print("bien joué")
    else:
        print("votre mot a l'enver est :", alenvere)

def by():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    split_time = current_time.split(':')

    H = split_time[0]
    M = split_time[1]
    S = split_time[2]

    if (int(H) < 12) & (int(H) > 00):
        print("Bonne journée !")
    elif (int(H) < 14) & (int(H) > 12):
        print("Bon app !")
    elif (int(H) < 18) & (int(H) > 00):
        print("Bonne soirée !")



hello()
mirror()
by()
