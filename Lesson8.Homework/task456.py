class Storage:
    def __init__(self, name):
        self.name = name


class OfficeEquipment:
    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, name, type_printer):
        self.name = name
        self.type = type_printer


class Scanner(OfficeEquipment):
    def __init__(self, name, type_scanner):
        self.name = name
        self.type = type_scanner


class Xerox(OfficeEquipment):
    def __init__(self, name, type_xerox):
        self.name = name
        self.type = type_xerox
