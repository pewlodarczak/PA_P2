from queue import Queue
 
playlist = Queue(maxsize=20)

def addToPlaylist(song):
    playlist.put(song)

def getNextSong():
    return playlist.get()

def showSongs():
    print(list(playlist.queue))

addToPlaylist("Beethoven", "c:\music\symph9.mp3")
addToPlaylist("Miles Davis")
addToPlaylist("Mozart")

showSongs()

print(getNextSong())

showSongs()
