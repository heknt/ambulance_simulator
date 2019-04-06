class Station:
    __id = 0

    def __init__(self, address):
        self.__address = address
        self.calls = []
        self.cars = []

    def get_id(self):
        return self.__id

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def count_cars(self):
        return len(self.cars)

    def count_calls(self):
        return len(self.calls)

    def __make_call(self, call):
        pass

