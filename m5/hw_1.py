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
