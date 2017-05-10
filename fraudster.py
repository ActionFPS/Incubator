#curl -s 'https://actionfps.com/logs.tsv?from=2017-01-01T00:00:00Z&to=2099-04-10T11:02:03Z' > AFPS2017.txt
#python fraudster.py < AFPS2017.txt > fraudster.csv

import sys

all_servers = {"AssaultCube[local#1999]": 0, "AssaultCube[local#2999]": 0, "AssaultCube[local#3999]":0, "AssaultCube[local#4999]":0, "AssaultCube[califapublic]": 0, "ActionFPS[local#7654]": 0, "ac_server[32337]": 0}
fragCLA = dict(all_servers)
flagCLA = dict(all_servers)
fragRVSF = dict(all_servers)
flagRVSF = dict(all_servers)
time = dict(all_servers)
players = {}
print "old name,new name,minutes remaining,status"
for line in sys.stdin:
    splitted = line.split()
    #Get cla's flags and frags
    if "Team  CLA" in line and "players" in line and "frags" in line and "flags" in line:
        #3 -> server 8-> frags 10->flags
        fragCLA[splitted[3]] = splitted[8]
        flagCLA[splitted[3]] = splitted[10]
    #Get rvsf's flags and frags
    if "Team RVSF" in line and "players" in line and "frags" in line and "flags" in line:
        fragRVSF[splitted[3]] = splitted[8]
        flagRVSF[splitted[3]] = splitted[10]
    #Get the team of each player
    if "normal  0.0.0.0" in line:
        players[splitted[5]] = splitted[6]
    #Get the time remaining on each server
    if "minutes remaining" in line and "ctf" in line:
        time[splitted[3]] = splitted[9]
    #if someone change his name, we look which team is winning on the server
    if "changed name" in line:
        if flagRVSF > flagCLA:
            winner = "RVSF"
        elif flagRVSF < flagCLA:
            winner = "CLA"
        else:
            winner = "Tie"

        try:
            if players[splitted[5]] == "RVSF" or players[splitted[5]] == "CLA":
                if players[splitted[5]] != winner:
                    print splitted[5] + "," + splitted[9] + "," + str(time[splitted[3]]) + "," + "LOSING"
                else:
                    print splitted[5] + "," + splitted[9] + "," + str(time[splitted[3]]) + "," + "WINNING"

        except(KeyError, ValueError):
            pass
