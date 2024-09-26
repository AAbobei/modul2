class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Назавание: {self.name}, колличество этажей: {self.number_of_floors}'

    def go_to(self, new_floor):
        a = int(new_floor)
        if a < 1 or a > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(a):
                print(i + 1)

    def __eq__(self, other):
        if self.number_of_floors == other:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.number_of_floors < other:
            return True
        else:
            return False

    def __le__(self, other):
        if self.number_of_floors <= other:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.number_of_floors > other:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.number_of_floors >= other:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.number_of_floors != other:
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, int):
            return f'Назавание: {self.name}, колличество этажей: {self.number_of_floors + other}'
        else:
            return ('Не цисло')

    def __radd__(self, other):
        if isinstance(other, int):
            return f'Назавание: {self.name}, колличество этажей: {self.number_of_floors + other}'
        else:
            return ('Не цисло')

    def __iadd__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
            return self#f'Назавание: {self.name}, колличество этажей: {self.number_of_floors + other}'
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            return ('Не цисло')


house = House('ЖК Эльбрус', 30)
house.go_to(45)
house.go_to(0)
house.go_to(5)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(len(h1))
print(len(h2))

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__