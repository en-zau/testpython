from _datetime import datetime


def hello(now):
    current_time = now.strftime("%H:%M:%S")
    split_time = current_time.split(':')

    H = split_time[0]

    if (int(H) < 12) & (int(H) > 00):
        return "Bonjour !"
    elif (int(H) < 14) & (int(H) > 12):
        return  "Bon app !"
    elif (int(H) < 18) & (int(H) > 14):
        return "Bonjour !"
    elif (int(H) < 18) & (int(H) > 00):
        return "Bonsoir !"

def mirror(word):

    #phrase = input("votre phrase a l'envers : ")
    alenvere = word[::-1]

    if alenvere == word:
        print("votre mot a l'enver est :", alenvere)
        print("bien joué")
    else:
        print("votre mot a l'enver est :", alenvere)

def by():

    current_time = now.strftime("%H:%M:%S")

    split_time = current_time.split(':')

    H = split_time[0]

    if (int(H) < 12) & (int(H) > 00):
        return "Bonne journée !"
    elif (int(H) < 14) & (int(H) > 12):
        return "Bon app !"
    elif (int(H) > 14) & (int(H) < 18):
        return "Bon aprem !"
    elif (int(H) < 18) & (int(H) > 00):
        return "Bonne soirée !"


if __name__ == '__main__':
    now = datetime.now()
    hello(now)
    mirror(word)
    by(now)

