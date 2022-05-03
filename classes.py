from abc import abstractmethod

class Storage:

   @abstractmethod
   def add(self, name, count):
        pass

   @abstractmethod
   def remove(self, name, count):
        pass

   @abstractmethod
# `get_free_space()` - вернуть количество свободных мест
   def get_free_space(self):
        pass

   @abstractmethod
# `get_items()` - возвращает содержание склада в словаре {товар: количество}
   def get_items(self):
        pass

   @abstractmethod
# `get_unique_items_count()` - возвращает количество уникальных товаров.
   def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_free_space() > count:
            for item in self.items.keys():
                if name == item:
                    self.items[item] = self.items[item] * count
                    is_found = True
            if not is_found:
                self.items[item] = count
            print(f"Товар {name.title()} добавлен")
        else:
            print(f"Товар не может быть добавлен, так как свободных мест {self.get_free_space()} ")

    def remove(self, name, count):
        for item in self.items.keys():
            if name == item:
                if self.items[item] - count >=0:
                    self.items[item] = self.items[item] - count
                else:
                    print(f"Слишком мало {name}")
            else:
                print(f"{name.title()} такого товара нет на складе")
                is_found = True

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    # `get_items()` - возвращает содержание склада в словаре {товар: количество}
    def get_items(self):
        return self.items

    # `get_unique_items_count()` - возвращает количество уникальных товаров.
    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.capacity = 20
        self.limit = limit

    @property
    def get_item_limit(self):
        return self.limit

    def add(self, name, count):
        if self.get_unique_items_count() < self.limit:
            super.add(name, count)
        else:
            print (f"Товар {name} не может быть добавлен")


class Request:
    def __init__(self, str):
        lst = self.get_info(str)
        self.from_ = lst[4]
        self.to = lst[6]
        self.amount = int(lst[1])
        self.product = lst[2]

    def get_info(self, str):
        return str.split(" ")

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"







