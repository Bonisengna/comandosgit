import os 
#menucadastroderestaurante
def exibir_nome_do_app():
    print ("===Menu de Cadastro===")
def exibir_opcoes():
    #cadastrarrestaurante
    print ("1. Cadastrar Restaurantes")
    #listarestaurantes
    print ("2. Listar Restaurantes")
    #editarrestaurante  
    print ("3. Editar Restaurante")
    #ativarrestaurante
    print ("4. Ativar Restaurante")
    #desativarrestaurante
    print ("5. Desativar Restaurante")
    #saircadastroderestaurante
    print ("6. Sair do Cadastro")
def escolher_opcao():    
    opcao_escolhida = int(input("Digite a opção desejada:"))
    print (f"Você escolheu a opção {opcao_escolhida}") #interpolação com f-strings
    if opcao_escolhida == 1:
        print ("Cadastrar Restaurantes")
    elif opcao_escolhida == 2:
        print ("Listar Restaurantes")
    elif opcao_escolhida == 3:
        print ("Editar Restaurantes")
    elif opcao_escolhida == 4:
        print ("Ativar Restaurante")
    elif opcao_escolhida == 5:
        print ("Desativar Restaurante")
    else:
        encerrar_app()

def main():
    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

def encerrar_app():
       os.system("cls") #limpar a tela no windows
       print ("Encerrando o aplicativo...")

if __name__ == "__main__":
    main()

    #bruno
    #testar com commit com a interface do vscode
