import random
from src.models.repositories.musics_repository import musics_repository


class PlaylistCreatorController:
    def create_playlist(self) -> dict:
        # Princípio de responsabilidade única
        try:
            musics = self.__get_all_musics_and_verify()
            playlist = self.__create_playlist(musics)
            return self.__format_response(playlist)
        except Exception as e:
            self.__format__error_response(e)

    def __get_all_musics_and_verify(self) -> list:
        musics = musics_repository.get_all_songs()
        if musics is []:
            raise Exception("Não há músicas cadastradas para criar uma playlist.")
        
        return musics

    def __create_playlist(self, musics: list) -> list:
        random.shuffle(musics)
        return musics

    def __format_response(self, playlist: list) -> dict:
        return {
            "success": True,
            "playlist": playlist
        }

    def __format__error_response(self, error: Exception) -> dict:
        return {
            "success": False,
            "error": str(error)
        }