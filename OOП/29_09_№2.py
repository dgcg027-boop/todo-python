class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    def info(self):
        print(f'"{self.title}" - {self.artist}')

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, title, artist):
        song = Song(title, artist)
        self.songs.append(song)
    def show(self):
        if len(self.songs) == 0:
            print("Плейлист пуст")
            return
        for i, song in enumerate(self.songs, start=1):
            print(f"{i}. ", end="")
            song.info() 
    def remove_song(self, index):
        if index < 1 or index > len(self.songs):
            print("Нет такого номера")
        else:
            self.songs.pop(index - 1)
    def count(self):
        print(f"Всего песен: {len(self.songs)}")

playlist = Playlist("Мой плейлист")
playlist.add_song("Bohemian Rhapsody", "Queen")
playlist.add_song("Imagine", "John Lennon")
playlist.add_song("Yesterday", "The Beatles")

playlist.show()
playlist.remove_song(2)
playlist.show()
playlist.count()
    


