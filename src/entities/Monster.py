from entities.Base import Base


class Monster(Base):
    def __init__(
        self,
        name="Anonymous",
        entity_type="monster",
        mana=100,
        life=100,
        attack=10,
        defense=0,
        level=1,
        alive=True,
    ):
        super().__init__(
            name=name,
            entity_type=entity_type,
            mana=mana,
            life=life,
            attack=attack,
            defense=defense,
            level=level,
            alive=alive,
        )

    def __str__(self):
        return f"Name: {self.name}\nType: {self.entity_type}\nMana: {self.mana}\nLife: {self.life}\nAttack: {self.attack}\nDefense: {self.defense}\nLevel: {self.level}\nAlive: {self.alive}"

    def __repr__(self):
        return self.__str__()
