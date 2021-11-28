import os


print("     BEM-VINDOS AO FCDL-GAMES.RAJ       ")
print("========================================")
print("              J O G O S                 ")
print("+======================================+")
print("|                                      |")
print("|    1 – Forca                         |")
print("|    2 – Jogo da Velha                 |")
print("|    3 – JokenPo                       |")
print("|    4 - Sair                          |")
print("|                                      |")
print("+======================================+")
print()
menu = int(input("QUAL JOGO DESEJA JOGAR? "))
os.system("cls")


if menu == 1:
    import JogoDeForca
elif menu == 2:
    import JogoDaVelha
elif menu == 3:
    import JogoJokenpo
elif menu == 4:
    print()
    print('Obrigado por jogar!!!Espero que tenha gostado!!!')
    print()
    exit()
else:
    print("VOCÊ DIGITOU UM VALOR INVÁLIDO!!!")
    print()
    print("Digite um valor que tenha na faixa de opções =>")
    print()
    import Menu

print()
voltaraomenu = int(input("DESEJA VOLTAR AO MENU? 1 PARA SIM E 2 PARA NÃO: => "))

if voltaraomenu == 1:
    print("     BEM-VINDOS AO FCDL-GAMES.RAJ       ")
    print("========================================")
    print("              J O G O S                 ")
    print("+======================================+")
    print("|                                      |")
    print("|    1 – Forca                         |")
    print("|    2 – Jogo da Velha                 |")
    print("|    3 – JokenPo                       |")
    print("|    4 - Sair                          |")
    print("|                                      |")
    print("+======================================+")
    print()
    menu = int(input("QUAL JOGO DESEJA JOGAR? "))
    os.system("cls")
    if menu == 1:
        import JogoDeForca
    elif menu == 2:
        import JogoDaVelha
    elif menu == 3:
        import JogoJokenpo
    elif menu == 4:
        print()
        print('Obrigado por jogar!!!Espero que tenha gostado!!!')
        exit()
    else:
        print()
        print("Você digitou um valor inválido!!!!!")
        print()
        print("Digite um valor que tenha na faixa de opções =>")
        print()
        import Menu
elif voltaraomenu == 2:
    print()
    print('Obrigado por jogar!!!Espero que tenha gostado!!!')
    exit()  
else:
    print()
    print("Você digitou um valor inválido!!!!!")
    print()
    print("Digite um valor que tenha na faixa de opções =>")
    print()
    import Menu

