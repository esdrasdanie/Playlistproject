import os

class SongRegisterView:
    def registry_song_initial(self) -> dict:
        self.__clear()
        print("Implementar Nova Música\n\n")

        title = input("Digite o título da música: ")
        artist = input("Digite o artista da música: ")
        year = input("Digite o ano da música: ")

        new_song_informations = {
            "title": title,
            "artist": artist,
            "year": year
        }

        return new_song_informations

    def __clear(self):
        os.system("cls||clear")