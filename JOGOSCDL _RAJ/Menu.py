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
    exit()
else:
    print("Você digitou um valor inválido!!!!!")