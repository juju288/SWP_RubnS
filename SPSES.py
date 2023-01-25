import requests
from numpy import random
import csv
import os
from numpy.core.defchararray import upper

hand = ["Stein", "Papier", "Schere", "Spock", "Echse"]
host = 'http://localhost:5000/stats'
name = (input(f"Playername: "))

def determineWin(p1, p2):
    print(hand[p1] + " gegen " + hand[p2])
    if (p1 == p2):
        #print("Unentschieden")
        return None
    if hand[p1] == hand[(p2 - 2)] or hand[p2] == hand[(p1 - 1)]:
    #if p1 == (p2-2 if p2-2 > 0 else p2+3) or p1 == (p2+1 if p2+1 <= 4 else p2-5):
        #print("Du hast gewonnen!")
        return True
    #print("Du hast verloren!")
    return False

def getComputerHand():
    r = int(random.random() * 4)
    return r    #hand[r]

def getmyHand():
    print("Stein = 0", "Papier = 1", "Schere = 2", "Spock = 3", "Echse = 4")
    return int(input("Deine Zahl:")) #hand[int(input("Deine Zahl:"))]


def get_dic():
    dic = {}
    dic["TotalPlays"] = 0
    dic["Players-Wins"] = 0
    dic["Computers-Wins"] = 0
    dic["Draw"] = 0
    for i in hand:
        dic[f"{i} ChosenByPlayer"] = 0
    for i in hand:
        dic[f"{i} ChosenByComputer"] = 0
    return dic


def insertDic(dic, playerChose, computerChose):
    dic["TotalPlays"] += 1
    if determineWin(playerChose, computerChose):
        dic["Players-Wins"] += 1
    elif determineWin(playerChose, computerChose) == None:
        dic["Draw"] +=1
    else:
        dic["Computers-Wins"] += 1
    dic[f"{hand[playerChose]} ChosenByPlayer"] += 1
    dic[f"{hand[computerChose]} ChosenByComputer"] += 1


def play():
    playAgain = 'Y'
    dic = get_dic()
    while playAgain == 'Y':
        playersInput = getmyHand()
        computerChose = getComputerHand()
        print("Computer has chosen: ", hand[computerChose])
        if determineWin(playersInput, computerChose):
            print("You Win")
        elif determineWin(playersInput, computerChose) == None:
            print("Draw")
        else:
            print("Computer Wins")
        insertDic(dic, playersInput, computerChose)
        playAgain = upper(input("Do you want to play again? Y/N"))
    stats = dic
    return stats


def printStats():
    saved_data = {}
    with open("stats.csv", "r") as data:
        output = csv.DictReader(data, delimiter=";")
        for item in output:
            saved_data = item
    for item in saved_data:
        print(item + ":" + saved_data[item])


def uploadData(dic):
    if not os.path.exists('stats.csv'):
        w = csv.DictWriter(open("stats.csv", "w"), delimiter=";", fieldnames=dic.keys())
        w.writeheader()
        w.writerow(dic)
    else:
        saved_data = {}
        with open("stats.csv", "r") as data:
            output = csv.DictReader(data, delimiter=";")
            for item in output:
                saved_data = item
        for key in saved_data:
            if key in dic:
                saved_data[key] = int(saved_data[key]) + int(dic[key])
        w = csv.DictWriter(open("stats.csv", "w"), delimiter=";", fieldnames=dic.keys())
        w.writeheader()
        w.writerow(saved_data)


def uploadDataToServer(dic):
    print('Stats werden am Server gespeichert')
    save = str(dic)
    p = requests.put('%s/%s' % (host, name), data={'score': save})
    print(p)
    print(p.json())

def getServerStats():
    p = requests.get('%s/%s' % (host, name)).json()
    print(p)

def main():
    runIt = True
    stats = {}
    while runIt:
        print("PLAY, STATS, UPLOAD data, END")
        ip = upper(input())
        if ip == "PLAY":
            stats = play()
            print(stats)
        elif ip == "STATS":
            printStats()
            print("Server:")
            getServerStats()
        elif ip == "UPLOAD":
            if not stats == None:
                uploadData(stats)
                uploadDataToServer(stats)
        elif ip == "END":
            print("Bye")
            runIt = False

if __name__ == "__main__":
    main()

