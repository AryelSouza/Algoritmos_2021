"""//---------------bibliotek---------------\\"""
import random

"""//---------------variaveis---------------\\"""

gridPlayerA = [0] * 100  # campo da maquina
gridPlayerB = [0] * 100  # campo do jogador

gridGamePlayerA = [0] * 100  # cria uma cópia do campo da maquina e mostra apenas o campo vazio

OnGame = True  # liga o jogo

PrevPlayerShoots = []
PrevIAShoots = []

"""//---------------funçoes---------------\\"""


def main():
    BoatTouchedByPlayer = 0
    BoatTouchedByIA = 0
    print(gridPlayerB)

    put_boats(gridPlayerA)  # coloca os navios da maquina aleatoriamente
    put_boats(gridPlayerB)  # coloca os navios do jogador aleatoriamente(temporario)
    while OnGame == True:  # enquanto estiver no jogo

        print(gridGamePlayerA)  # printa o campo da maquina (sem navios)

        PlayerShoot = input("Onde você quer atirar ? (Digite as coordenadas assim : A,1) ")
        PlayerShoot.split(",")  # Split the coords
        Lettre = PlayerShoot[0]  # take the lettre
        Number = int(PlayerShoot[2])  # take the number, convert into an integer

        Player_Shoot = int(ord(Lettre)) - 65 + 10 * (
                    Number - 1)  # transform the lettre and the number into a number coord

        if can_shoot(PrevPlayerShoots, Player_Shoot) == True:  # if we can shoot

            if gridPlayerA[Player_Shoot] == 1:  # if we touch a boat in the IA's board
                shoot_Touched(gridGamePlayerA,
                              Player_Shoot)  # call the shoot function that replace the coord by an F on the empty board
                print("touched")
                BoatTouchedByPlayer = BoatTouchedByPlayer + 1  # count until 14 (number of boat "parts")
                End_Game("Player")  # check if the player won


            else:
                shoot(gridGamePlayerA, Player_Shoot)  # show the shot next time to remind the player where he has shoot
                print("missed, IA's turn : ")
                IA_shot = random.randint(0, 99)  # make the IA shot randomly
                if gridPlayerB[IA_shot] == 1:  # if IA touch a boat in the player's board
                    print("IA touched one of your boat")
                    shoot_Touched(gridPlayerB, IA_shot)  # call the shoot function that replace the coord by an F
                    print(gridPlayerB)  # print the player's board
                    BoatTouchedByIA = BoatTouchedByIA + 1  # count until 14 (number of boat "parts")
                    End_Game("IA")  # check if the IA won

                else:
                    shoot(gridPlayerB, IA_shot)  # replace the shoot by an X
                    print("Deu sorte, a maquina errou !")


def shoot_Touched(grid, shot):
    grid.pop(shot)
    grid.insert(shot, 'F')


def shoot(grid, shot):
    grid.pop(shot)
    grid.insert(shot, 'X')


def End_Game(grid):
    if grid == "IA":
        if grid == 14:  # if IA has touched all the player's boat
            OnGame = False  # turn off the game
            print("Que pena,você foi humilhado por uma maquina!")

    elif grid == "Player":
        if grid == 14:
            OnGame = False  # turn off the game
            print("Boa,você venceu!")


def can_shoot(List, shot):
    for x in range(len(List)):  # check if the shoot didnt already done
        if List[x] == shot:
            print("Você já atirou aqui !")
            return False
    List.append(shot)
    return True


def put_boats(grid):
    for n in range(2, 6):
        x, y, direction = random.randint(0, 9), random.randint(0, 9), random.randint(0, 1)
        while cant_put_boat(n, x, y, direction, grid):
            x, y, direction = random.randint(0, 9), random.randint(0, 9), random.randint(0, 1)
        put_boat(n, x, y, direction, grid)


def put_boat(length, x, y, direction, grid):
    if direction == 0:  # direçao horizontal
        for i in range(length):
            position = x + i + 10 * y
            grid[position] = 1

    if direction == 1:  # direção vertical
        for i in range(length):
            position = x + 10 * (y + i)
            grid[position] = 1


def cant_put_boat(length, x, y, direction, grid):
    return direction == 0 and x + length >= 10 or direction == 1 and y + length >= 10


"""//----------------codigo main----------------\\"""

main()  # dá run na função main