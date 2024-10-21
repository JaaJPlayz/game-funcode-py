from entities.Player import Player
from utils.line import line


def main():
    player = Player("Hiago", "player", 100, 100, 10, 0, 1, True)
    print(player.__repr__())
    line(30)
    player.take_damage(90)
    print(player.__repr__())
    line(30)
    player.heal(23)
    print(player.__repr__())
    line(30)




if __name__ == "__main__":
    main()
