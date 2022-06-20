playlist = []

def addSong(song):
    playlist.append(song)

def playNextSong():
    print(playlist.pop())

addSong('Aretha Franklin')
addSong('Elvis')
addSong('Elton')

print(playlist)

playNextSong()

print(playlist)
