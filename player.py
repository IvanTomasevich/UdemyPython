class Player:
    vocation = "No vocation"
    spell = "Puff!"
    movement_speed = "50"

    def __init__(self, **kwargs):
        self.name = input("Elije tu nombre: ")
        self.hit_points = kwargs.get("hit_point", 50)
        self.mana = kwargs.get("mana", 50)

    def __str__(self):
        return "{} es un {} tiene {} de Hit y {} de mana, puede lanzar {} y se mueve a {} de velocidad\n"\
            .format(self.name,
                    self.vocation,
                    self.hit_points,
                    self.mana,
                    self.cast_spell(),
                    self.movement_speed)

    def cast_spell(self):
        return self.spell


class Sorcerer(Player):
    vocation = "sorcerer"
    spell = "Utevo Lux"
    movement_speed = "20"

    def cast_spell(self):
        return "{}, Exura!!".format(self.spell)


class Knight(Player):
    vocation = "knight"
    spell = "Exori!!"
    movement_speed = "60"


class Druid(Player):
    vocation = "druid"
    spell = "Kamejameha"
    movement_speed = "75"

    def cast_spell(self):
        return "{}, Exura!!".format(self.spell)


class Elfo(Player):
    vocation = "elfo"
    spell = "cinco ratoncitos!!"
    movement_speed = "80"
