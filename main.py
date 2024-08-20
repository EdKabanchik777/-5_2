import self


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name, self.number_of_floors


H = House('ЖК Эльбрус', 30)
print(H.name, H.number_of_floors)
H.go_to(5)
H.go_to(33)
print(len(H))
print(H.name, H.number_of_floors)
