class FlowerAttributes:
    color = 'color'
    stem_length = 'stem_length'
    freshness_level = 'freshness_level'
    cost = 'cost'
    days_to_fade = 'days_to_fade'
    name = 'name'


class Flower:
    def __init__(self, name, color, stem_length, freshness, cost, shelf_life):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.__freshness = freshness
        self.freshness_level = self.__is_fresh()
        self.cost = cost
        self.shelf_life = shelf_life
        self.days_to_fade = self.__days_to_fade()

    def __is_fresh(self):
        return self.__freshness <= 3

    def __days_to_fade(self):
        return self.shelf_life - self.__freshness

    def __str__(self):
        return (f"{self.name}: color - {self.color}, stem length - {self.stem_length} centimeters, "
                f"freshness - {self.__is_fresh()}, "
                f"cost - ${self.cost}, days to fade - {self.days_to_fade} days")


class Rose(Flower):
    def __init__(self, name, color, stem_length, freshness, cost, shelf_life, thorns):
        super().__init__(name, color, stem_length, freshness, cost, shelf_life)
        self.thorns = thorns

    def __str__(self):
        return f"{super().__str__()}, Thorns: {self.thorns}"


class Tulip(Flower):
    def __init__(self, name, color, stem_length, freshness, cost, shelf_life, petals_count):
        super().__init__(name, color, stem_length, freshness, cost, shelf_life)
        self.petals_count = petals_count

    def __str__(self):
        return f"{super().__str__()}, Petals count: {self.petals_count}"


class Chamomile(Tulip):
    def __init__(self, name, color, stem_length, freshness, cost, shelf_life, petals_count, petals_length):
        super().__init__(name, color, stem_length, freshness, cost, shelf_life, petals_count)
        self.petals_length = petals_length

    def __str__(self):
        return f"{super().__str__()}, Petals length: {self.petals_length}"


class Bouquet:
    def __init__(self, *args):
        self.__flowers = list(args)
        self.__cost_bouquet = self.__calculate_cost()
        self.__shelf_life_bouquet = self.__calculate_shelf_life()
        self.__count_flowers = len(self.__flowers)

    @property
    def cost_bouquet(self):
        return self.__cost_bouquet

    @property
    def average_fading_time(self):
        return self.__shelf_life_bouquet

    @property
    def count_flowers(self):
        return self.__count_flowers

    @property
    def flowers(self):
        return self.__flowers

    def __calculate_cost(self):
        return sum([floret.cost for floret in self.__flowers])

    def __calculate_shelf_life(self):
        return round(sum([floret.days_to_fade for floret in self.__flowers]) / len(self.__flowers))

    def sort_by_choice(self, choice, reverse=True):
        self.__flowers.sort(key=lambda floret: getattr(floret, choice), reverse=reverse)

    def search_by(self, attribute, value):
        return [floret for floret in self.__flowers if getattr(floret, attribute) == value]

    def __str__(self):
        return "Bouquet with flowers:\n" + "\n".join(str(floret) for floret in self.__flowers)


bouquet = Bouquet(
    Rose("Red Rose", "Red", 40, 2, 5, 7, 12),
    Rose("White Rose", "White", 35, 3, 6, 6, 10),
    Rose("Yellow Rose", "Yellow", 50, 3, 7, 8, 15),
    Tulip("Red Tulip", "Red", 30, 0, 3, 5, 6),
    Tulip("Yellow Tulip", "Yellow", 25, 5, 4, 6, 6),
    Tulip("White Tulip", "White", 35, 2, 5, 7, 6),
    Chamomile("Common Chamomile", "White", 20, 1, 2, 4, 15, 1),
    Chamomile("Medicinal Chamomile", "White", 22, 1, 3, 5, 18, 1.2),
    Chamomile("Double Chamomile", "White", 25, 2, 4, 6, 20, 1.5)
)


def print_by_choice(choice, reverse=True):
    print(f"\nSorted by {choice}:")
    bouquet.sort_by_choice(choice, reverse)
    print(bouquet)


def print_by_search(attribute, value):
    print(f"\nSearch by {attribute}: {value}")
    search_result = bouquet.search_by(attribute, value)
    for floret in search_result:
        print(floret)


print(f'Cost of the bouquet: ${bouquet.cost_bouquet}')
print(f'The average fading time of the bouquet: {bouquet.average_fading_time} days')
print(f'Count of flowers in the bouquet: {bouquet.count_flowers}')
print("\nUnsorted bouquet:")
print(bouquet)

print_by_choice(FlowerAttributes.cost)
print_by_choice(FlowerAttributes.stem_length)
print_by_choice(FlowerAttributes.freshness_level)
print_by_choice(FlowerAttributes.days_to_fade)
print_by_choice(FlowerAttributes.name)


print_by_search(FlowerAttributes.color, 'White')
print_by_search(FlowerAttributes.freshness_level, True)
print_by_search(FlowerAttributes.days_to_fade, 3)
print_by_search(FlowerAttributes.stem_length, 25)
