from entities.Player import Player
from utils.line import line

def take_shield(entity):
    entity.defense += 10
    entity.items.append("shield")

def main():
    player = Player("Hiago", "player", 100, 100, 10, 0, 1, True)

    line()
    print(player)
    line()

    take_shield(player)

    line()
    print(player)
    line()


if __name__ == "__main__":
    main()
