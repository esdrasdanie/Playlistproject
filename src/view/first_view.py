def introduction_page() -> str:
    message = '''
    Bem-vindo! ao Sistema Musical

    * Cadastrar uma nova música: Digite 1
    * Criar uma nova playlist: Digite 2
    * Sair: Digite 5
    '''
    print(message)
    command = input("Digite o comando desejado: ")
    return command