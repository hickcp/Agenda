
agenda_r = {
}
lista = ["Exit", "EXIT", "exit"]
adicionar = ["Adicionar", "adicionar", "ADICIONAR"]
remover = ["Remover", "REMOVER", "remover"]
mudar = ["Mudar", "mudar", "MUDAR"]
consultar = ["Consultar", "CONSULTAR", "consultar"]
ver_agenda = ["Ver agenda", "VER AGENDA", "ver agenda", "Ver Agenda"]
sair = ["Sair", "sair", "SAIR"]
def rlookup(dict):
    while True:
        print("Bem vindo a minha agenda eletronica! O que você deseja fazer?\n Adicionar \n Remover \n Mudar \n Consultar \n Ver agenda \n Sair")
        decisao = input("\n O que deseja fazer? ")
        if decisao in sair:
            break
        if decisao in adicionar:
            x = input("Digite o nome da pessoa: ")
            y = input("Digite o número da pessoa no formato: (XX)XXXXX-XXXX: ")
            dict[x] = y
            dict[y] = x
            print("Adicionado na agenda com sucesso!")
            if input("Deseja voltar do inicio? (S/N)") not in ('S', 's'):
                break
        if decisao in remover:
            x = input("Digite o nome da pessoa que quer remover: ")
            print(dict[x])
            for a in dict[x]:
                b = a
                dict.pop(b)
            dict.pop(x)
            print("Removido com sucesso!")
            if input("Deseja voltar do inicio? (S/N)") not in ('S', 's'):
                break
        if decisao in mudar:
            x = input("Digite o nome de quem você vai mudar: ")
            y = input("Digite o novo número do usuário no formato (XX)XXXXX-XXXX: ")
            dict[x] = y
            dict[y] = x
            print("Sucesso! O número de",x," mudou para",y, sep=" ")
            if input("Deseja voltar do inicio? (S/N)") not in ('S', 's'):
                break
        if decisao in consultar:
            x = input("Digite o nome da pessoa para conultar: ")
            if x in dict:
                print("Aqui está o nome e o número da pessoa:", dict[x])
            if x not in dict:
                print("O número informado não está em uso")
            if input("Deseja voltar do inicio? (S/N)") not in ('S', 's'):
                break
        if decisao in ver_agenda:
            print(dict)
        if input("Deseja voltar do inicio? (S/N)") not in ('S', 's'):
            break


rlookup(agenda_r)