
# Name: HUANGWENBO 13724715
# Date started: 25/04/2020
# GitHub URL: https://github.com/HUANGWENBO001030/assignment-1-cp1404
#class to save song data
class Song(object):
    def __init__(self, title, artist, year, completed):
        self.title = title
        self.artist = artist
        self.year = int(year)
        self.completed = completed.lower()
    def getTitle(self):
        return self.title
    def getArtist(self):
        return self.artist
    def getYear(self):
        return self.year
    def getCompleted(self):
        return self.completed
    def setCompleted(self, completed):
        self.completed = completed

#list songs when choose "L" in the menu
def listSongs(songs):
    learnedCount = 0
    for i in range(len(songs)):
        line = " " + str(i) + ". "
        if songs[i].getCompleted().lower() == 'u':
            line = line + '* '
        else:
            line = line + '  '
        line = line + '%-31s'%(songs[i].getTitle()) + "- " #append title
        line = line + '%-26s'%(songs[i].getArtist()) #append artist
        line = line + "(" + str(songs[i].getYear()) + ")" #append year
        print(line)
        if songs[i].getCompleted() != 'u':
            learnedCount = learnedCount + 1
    print(str(learnedCount) + " songs learned, " + str(len(songs) - learnedCount) + " songs still to learn")

#add new songs when choose "A" in the menu
def addNewSong(songs):
    title = input("Title: ") #enter title
    while len(title.strip()) == 0:
        print("Input can not be blank")
        title = input("Title: ")

    artist = input("Artist: ") #enter artist
    while len(artist.strip()) == 0:
        print("Input can not be blank")
        artist = input("Artist: ")

    year = -1
    while year < 0: #enter year
        try:
            year = int(input("Year: "))
            if year < 0:
                print("Number must be >= 0")
        except:
            print("Invalid input; enter a valid number")
    songs.append(Song(title, artist, year, 'u'))
    songs = sortSongs(songs)
    print(title + " by " + artist + " (" + str(year) + ") added to song list")

#complete a song when choose "C" in the menu
def completeASong(songs):
    #get song count which is not learned
    unlearnedCount = 0
    for s in songs:
        if s.getCompleted() == 'u':
            unlearnedCount = unlearnedCount + 1
    if unlearnedCount == 0:
        print("No more songs to learn!")
        return

    #enter the number
    print("Enter the number of a song to mark as learned")
    n = -1
    success = False
    while not success:
        try:
            n = int(input())
            if n < 0:
                print("Number must be >= 0")
            elif n > len(songs):
                print("Invalid song number")
            elif songs[n].getCompleted() != 'u':
                print("You have already learned " + songs[n].getTitle())
                success = True
            else:
                print(songs[n].getTitle() + " by " + songs[n].getArtist() + " learned")
                songs[n].setCompleted('l')
                success = True
        except:
            print("Invalid input; enter a valid number")

#quit the program and save songs to the csvFile
def quitProgram(songs, csvFile):
    file = open(csvFile, 'w')
    for s in songs:
        file.write(s.getTitle() + "," + s.getArtist() + "," + str(s.getYear()) + "," + s.getCompleted())
        file.write("\n")
    file.close()
    print(str(len(songs)) + " songs saved to " + csvFile) #display message
    print("Have a nice day :)")

#display menu and ask user choose option until user select "Q"
def displayMenu(songs):
    option = ''
    while option != 'Q': #quit until user select "Q"
        print("Menu:")
        print("L - List songs")
        print("A - Add new song")
        print("C - Complete a song")
        print("Q - Quit")
        option = input().upper()
        if option == 'L':
            listSongs(songs)
        elif option == 'A':
            addNewSong(songs)
        elif option == 'C':
            completeASong(songs)

#sort songs by artist in ascending order
def sortSongs(songs):
    for i in range(len(songs)):
        min = i
        for j in range(i+1, len(songs)):
            if songs[min].getArtist() > songs[j].getArtist():
                min = j
        if min != i:
            temp = songs[i]
            songs[i] = songs[min]
            songs[min] = temp

def main():
    csvFile = 'songs.csv'
    songs = []
    print("Songs to Learn 1.0 - by Lindsay Ward")
    file = open(csvFile, 'r') #load songs in file data.csv
    for line in file:
        values = line.strip().split(',')
        if len(values) >= 4:
            songs.append(Song(values[0], values[1], values[2], values[3]))
    file.close()
    sortSongs(songs)
    print(str(len(songs)) + " songs loaded") #display how many songs loaded
    displayMenu(songs)
    quitProgram(songs, csvFile)
main()
