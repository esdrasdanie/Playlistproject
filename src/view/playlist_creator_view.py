import os


class PlaylistCreatorView:

    def create_playlist_initial(self) -> dict:
        self.__clear()

        print("Criar Nova Playlist\n\n")

        playlist_name = input("Digite o nome da playlist: ")

        return {
            "name": playlist_name
        }

    def __clear(self):
        os.system("cls||clear")

    def create_playlist_success(self, controller_response: dict) -> None:
        message = '''
        Playlist criada com sucesso!

        * Nome: {}
        * Quantidade: {}
        '''.format(
            controller_response["attributes"]["name"],
            controller_response["count"]
        )

        print(message)

    def create_playlist_fail(self, controller_response: dict) -> None:
        self.__clear()

        message = '''
        Falha ao criar playlist!

        * Erro: {}
        '''.format(
            controller_response["error"]
        )

        print(message)