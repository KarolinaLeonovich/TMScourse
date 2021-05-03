# 1. В отеле есть 3 типа номеров: royal (2-3 комнаты), lux (1-2 комнаты), standard (1 комната). надо добавить метод для создания номеров и хранения их в виде словаря.
class Hotel():
    def __init__(self):
        self.room_catalog = {"royal_two": 0, "royal_three": 0, "lux_one": 0, "lux_two": 0, "standard": 0}

    def create_room(self, room_category, room_numbers):
        self.room_catalog[room_category] = room_numbers
        return self.room_catalog

    def __str__(self):
        self.royal = self.room_catalog["royal_two"] + self.room_catalog["royal_three"]
        self.lux = self.room_catalog["lux_one"] + self.room_catalog["lux_two"]
        self.standard = self.room_catalog["standard"]
        return f'Welcome to our hotel! We have {self.royal} royal\n' \
               f'apartments for special guests. For those who\n' \
               f'appreciate comfort, we can offer {self.lux} lux apartments.\n' \
               f'For practical people there are {self.standard} standard rooms.'

hotel_1 = Hotel()
print(hotel_1.create_room("royal_two", 1))
print(hotel_1.create_room("royal_three", 1))
print(hotel_1.create_room("lux_one", 2))
print(hotel_1.create_room("lux_two", 2))
print(hotel_1.create_room("standard", 10))
print(hotel_1)


# 2. В комнате есть мебель для ванной, спальни и зала (если есть зал). нужно добавить метод для добавления и удаления из комнаты мебели в любом количестве.
class Room():
    """1 room = standart/lux. Only bedroom.
    2 room = lux or royal. Bedroom and bathroom.
    3 room - royal. Bedroom, bathroom and living room.
    I assume that the set of furniture is standard,
    i.e. you can't put a bed in a bathroom."""
    def __init__(self, number_of_rooms):
        self.number_of_rooms = number_of_rooms
        self.bedroom = {'bed': 0, 'locker': 0, 'carpet': 0, 'chair': 0, "table": 0}
        self.bathroom = {'shower': 0, 'bath': 0, 'dryer': 0}
        self.living_room = {'armchair': 0, 'television': 0, 'coffee_table': 0, 'sofa': 0}
        self.additionally_provided = {}  #Non-standard pieces of furniture that may be in the room.

    def quantity_of_furniture(self, name_of_furniture, number_of_furniture):
        if name_of_furniture in self.bedroom:
            self.bedroom[name_of_furniture] = number_of_furniture
            return self.bedroom
        elif name_of_furniture in self.bathroom:
            self.bathroom[name_of_furniture] = number_of_furniture
            return self.bathroom
        elif name_of_furniture in self.living_room:
            self.living_room[name_of_furniture] = number_of_furniture
            return self.living_room
        else:
            self.additionally_provided[name_of_furniture] = number_of_furniture
            return self.additionally_provided

    def __str__(self):
        self.temp_string1 = ""
        for k, v in self.bedroom.items():
            if v:
                self.temp_string1 += k
                self.temp_string1 += " - "
                self.temp_string1 += str(v)
                self.temp_string1 += "\n"
        self.temp_string2 = ""
        for k, v in self.bathroom.items():
            if v:
                self.temp_string2 += k
                self.temp_string2 += " - "
                self.temp_string2 += str(v)
                self.temp_string2 += "\n"
        self.temp_string3 = ""
        for k, v in self.living_room.items():
            if v:
                self.temp_string3 += k
                self.temp_string3 += " - "
                self.temp_string3 += str(v)
                self.temp_string3 += "\n"
        self.temp_string4 = ""
        for k, v in self.additionally_provided.items():
            if v:
                self.temp_string4 += k
                self.temp_string4 += " - "
                self.temp_string4 += str(v)
                self.temp_string4 += "\n"
        if self.number_of_rooms == 1:
            return f'This apartment has a nice bedroom.\nYou can find:\n{self.temp_string1} \nAdditionnaly we provide: {self.temp_string4}'
        elif self.number_of_rooms == 2:
            return f'This apartment has a nice bedroom.\nYou can find:\n{self.temp_string1} \nFurniture in bathroom: \n{self.temp_string2} \nAdditionnaly we provide: {self.temp_string4}'
        else:
            return f'This apartment has a nice bedroom.\nYou can find:\n{self.temp_string1} \nFurniture in bathroom: \n{self.temp_string2} \nFurniture in living room: \n{self.temp_string3} \nAdditionnaly we provide: {self.temp_string4}'

room_1 = Room(2)
print(room_1.quantity_of_furniture('bed', 1))
print(room_1.quantity_of_furniture('locker', 1))
print(room_1.quantity_of_furniture('chair', 2))
print(room_1.quantity_of_furniture('shower', 1))
print(room_1.quantity_of_furniture('dryer', 1))
print(room_1.quantity_of_furniture('jacuzzi', 1))
print(room_1)
        

# 3. Нужно создать один метод для изменения любого номера по заданным параметрам, в том числе удалению и изменению номеров и комнат.

# [ Рекомендую выполнить задание с кем-то ещё из группы ]
