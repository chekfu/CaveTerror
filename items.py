class Weapon:
    def __init__(self):
        raise NotImplementedError(
            'Do not create raw weapon objects.'
        )

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = 'Rock'
        self.description = 'A fist sized rock, suitable for bludgeoing.'
        self.damage = 5
        self.vaue = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = 'Dagger'
        self.description = 'A small dagger with some rust'
        self.damage = 10
        self.value = 20


class RustySword(Weapon):
    def __init__(self):
        self.name = 'Rusty sword'
        self.description = 'This sword is showing its age, '\
                           'but still has some fight in it'
        self.damage = 20
        self.value = 100


class Axe(Weapon):
    def __init__(self):
        self.name = 'Viking axe'
        self.description = 'This axe is sharp and heavy, ' \
                           'slow but can do serious damage.'
        self.damage = 40
        self.value = 150


class Consumable:
    def __init__(self):
        raise NotImplementedError('Do not create raw Consumable objects.')

    def __str__(self):
        return '{} (+{} HP'.format(self.name, self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        self.name = 'Crusty Bread'
        self.healing_value = 10
        self.value = 12


class HealingPotion(Consumable):
    def __init__(self):
        self.name = 'Healing Potion'
        self.healing_value = 50
        self.value = 60