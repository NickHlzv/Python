class Storage:
    def __init__(self, name):
        self.name = name
        self._storage = {}

    def add(self, office_equip, count):
        if isinstance(office_equip, OfficeEquipment) and isinstance(count, int):
            if office_equip in self._storage:
                self._storage[office_equip.name] += count
            else:
                self._storage.update({office_equip.name: count})
            print(f'{office_equip.name} добавлен на {self.name} в количестве {count}')
        else:
            print('Невозможно выполнить. Нужно передать объект техники и количество')

    def remove(self, office_equip, count):
        if isinstance(office_equip, OfficeEquipment) and isinstance(count, int):
            if count <= self._storage[office_equip.name]:
                self._storage[office_equip.name] -= count
            else:
                self._storage[office_equip.name] = 0
        else:
            print('Невозможно выполнить. Нужно передать объект техники и количество')

    def delete(self, office_equip):
        if office_equip.name in self._storage:
            del self._storage[office_equip.name]
        else:
            print('Такую операцию невозможно произвести т.к такой техники нет')

    def move(self, other_storage, office_equip, count):
        if isinstance(other_storage, Storage) and isinstance(office_equip, OfficeEquipment) and isinstance(count, int):
            if count <= self._storage[office_equip.name]:
                other_storage.add(office_equip, count)
            else:
                other_storage.add(office_equip, self._storage[office_equip.name])
            self.remove(office_equip, count)

    def get(self):
        return self._storage


class OfficeEquipment:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def do(self):
        print(f'{self.name} {self.action}')


class Printer(OfficeEquipment):
    def __init__(self, name, action_printer=None):
        self.name = 'Принтер. ' + name
        self.action = action_printer


class Scanner(OfficeEquipment):
    def __init__(self, name, action_scanner=None):
        self.name = 'Сканер. ' + name
        self.action = action_scanner


class Xerox(OfficeEquipment):
    def __init__(self, name, action_xerox=None):
        self.name = 'Ксерокс. ' + name
        self.action = action_xerox


thermal_printer = Printer('Термопринтер Posiflex', 'печатать чек')
laser_printer = Printer('Лазерный принтер HP', 'печатать на бумаге')
scanner = Scanner('Panasonic', 'Сканирует бумагу')
bio_scanner = Scanner('Smarttek', 'Сканирует опечатки пальцев')
xerox = Xerox('Ксерок Xerox', 'Делает ксерокопию')
storage = Storage('Главный склад')
office = Storage('Главный офис')
storage.add(thermal_printer, 15)
storage.add(laser_printer, 20)
storage.add(scanner, 17)
storage.add(bio_scanner, 23)
storage.add(xerox, 40)
print(storage.get())
storage.move(office, thermal_printer, 17)
storage.move(office, laser_printer, 15)
storage.move(office, scanner, 10)
print(office.get())
print(storage.get())
storage.delete(thermal_printer)
print(storage.get())
scanner.do()
bio_scanner.do()
laser_printer.do()
