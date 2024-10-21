class Player(object):
    def __init__(self, name, entity_type, mana, life, attack, defense, level):
        self.name = name
        self.entity_type = entity_type
        self.mana = mana
        self.life = life
        self.attack = attack
        self.defense = defense
        self.level = level

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        if value < 0:
            self._life = 0
        else:
            self._life = value

        if self._life < 0:
            self._life = 0

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value < 0:
            self._mana = 0
        else:
            self._mana = value

        if self._mana < 0:
            self._mana = 0

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        if value < 0:
            self._attack = 0
        else:
            self._attack = value

        if self._attack < 0:
            self._attack = 0

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        if value < 0:
            self._defense = 0
        else:
            self._defense = value

        if self._defense < 0:
            self._defense = 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 0:
            self._level = 0
        else:
            self._level = value

        if self._level < 0:
            self._level = 0

    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"Name: {self.name}\nType: {self.entity_type}\nMana: {self.mana}\nLife: {self.life}\nAttack: {self.attack}\nDefense: {self.defense}\nLevel: {self.level}"

    def __repr__(self):
        return self.__str__()
