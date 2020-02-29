# assignment 4: Fantasy hockey team
# this program creates a fantasy hockey team from data in a csv file
import csv


# this function reads all the stats and puts the data in two dimensional list
def readStats(fileName) -> list:
    myData = []
    openFile = open(fileName, "r")
    readCSV = csv.reader(openFile, delimiter=',')
    for row in readCSV:
        for i in range(len(row)):
            if row[i].isnumeric():
                row[i] = int(row[i])
        myData.append(row)
    myData.remove(myData[0])
    return myData


# _________________________________________________________________
# this function returns the stats for a specified player
def statsForPlayer(my2DList, playerName) -> list:
    for i in range(len(my2DList)):
        if my2DList[i][0] == playerName:
            return my2DList[i]


# _________________________________________________________________
# this function finds all the players of a specified position
def filterByPos(my2DList, position) -> list:
    players = []
    for i in range(len(my2DList)):
        if my2DList[i][2] == position:
            players.append(my2DList[i])
    return players


# _________________________________________________________________
# this function sorts the list of all players into descending order of their points
def sortByPoints(my2DList) -> list:
    for i in range(len(my2DList)-1, 0, -1):
        for j in range(i):
            if my2DList[j][6] < my2DList[j+1][6]:
                temp = my2DList[j]
                my2DList[j] = my2DList[j+1]
                my2DList[j+1] = temp
    mySortedList = my2DList
    return mySortedList


# _________________________________________________________________
# this function builds a fantasy hockey team
def buildBestTeam(my2DList, fileName):
    openFile = open(fileName, 'w')
    openFile.write(my2DList[0][0] + "\n")
    position = my2DList[0][2]
    indexOfFirstDefence = 0
    for i in range(len(my2DList)):
        if not my2DList[i][2] in position:
            openFile.write(my2DList[i][0] + "\n")
            position += my2DList[i][2]
            if my2DList[i][2] == "D":
                indexOfFirstDefence = i
    for j in range(len(my2DList)):
        if not j == indexOfFirstDefence and my2DList[j][2] == "D":
            openFile.write(my2DList[j][0])
            break


# _________________________________________________________________
# this function displays the stats of the fantasy hockey team
def displayTeamStats(my2DList, fileName):
    print("Name              Team  Pos      Games  G     A    Pts    PIM  SOG   Hits   BS")
    print("==============================================================================")
    openFile = open(fileName, "r")
    hasNext = openFile.readline()
    while hasNext:
        playerName = hasNext.strip()
        for i in range(len(statsForPlayer(my2DList, playerName))):
            if i == 0:
                print("{0:18}".format(statsForPlayer(my2DList, playerName)[i]), end="")
            else:
                print("{0:6}".format(statsForPlayer(my2DList, playerName)[i]), end="")
        print("\n")
        hasNext = openFile.readline()


# _________________________________________________________________
# this function adds up all the points of a team
def pointsPerTeam(my2DList, fileName) -> int:
    totalPoints = 0
    openFile = open(fileName, "r")
    hasNext = openFile.readline()
    while hasNext:
        playerName = hasNext.strip()
        totalPoints += statsForPlayer(my2DList, playerName)[6]
        hasNext = openFile.readline()
    return totalPoints


# _________________________________________________________________
def main():
    allStats = readStats("./venv/nhl_2018.csv")
    print("All players:\n", allStats, "\n")
    print("Stats for Filip Chlapik:\n", statsForPlayer(allStats, "Filip Chlapik"), "\n")
    print("All RW players:\n", filterByPos(allStats, "RW"), "\n")
    sortedStats = sortByPoints(allStats)
    print("All players from most to least points:\n", sortedStats, "\n")
    buildBestTeam(sortedStats, "./venv/my_team.txt")
    print("Fantasy team: \n")
    displayTeamStats(sortedStats, "./venv/my_team.txt")
    print("Total points of fantasy team:", pointsPerTeam(sortedStats, "./venv/my_team.txt"))


if __name__ == "__main__":
    main()