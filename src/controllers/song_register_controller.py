class SongRegisterController:
    def insert(self, new_song_informations: dict) -> dict:
        try:
            self._verify_songs_infos(new_song_informations)
            self._verify_if_song_already_registered(new_song_informations)
            self._verify_songs_infos(new_song_informations)
            self._insert_song(new_song_informations)
            self._format_response(new_song_informations)

        except Exception as e:
            self.__format_error_response(e)

    def _verify_if_song_already_registered(self, new_song_informations: dict) -> None:
        if len(new_song_informations["title"]) > 100:
            raise Exception("Song title is too long")

        year = int(new_song_informations["year"])
        if year >= 2026:
            raise Exception("Song year is invalid")
        

    def _verify_songs_infos(self, new_song_informations: dict) -> None:
        pass

    def _insert_song(self, new_song_informations: dict) -> None:
        pass

    def _format_response(self, new_song_informations: dict) -> dict:
        return {
            "success": True,
            "count": 1,
            "attributes": {
                new_song_informations["title"]
            }
        }

    def __format_error_response(self, err: Exception) -> dict:
        return {
            "success": False,
            "error": str(err)
        }