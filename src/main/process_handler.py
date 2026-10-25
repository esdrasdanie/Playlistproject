from src.view.first_view import introduction_page

def start() -> None: 
    while True:

        command = introduction_page()
        if command == '1': print("Inserindo uma nova música")
        elif command == '2': print("Criando uma nova playlist")
        elif command == '5': exit()
        else: print("\nComando inválido, tente novamente\n")