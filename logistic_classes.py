from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, title, qnt):
        pass

    @abstractmethod
    def remove(self, title, qnt):
        pass

    @abstractmethod
    def _get_free_space(self):
        pass

    @abstractmethod
    def _get_items(self):
        pass

    @abstractmethod
    def _get_unique_items_count(self):
        pass


class Store(Storage):
    __items = {}
    __capacity = 100

    @classmethod
    def add(cls, title, qnt):
        if cls._get_free_space() >= qnt:
            cls.__items[title] = cls.__items.get(title, 0) + qnt
            return True
        else:
            print("На складе недостаточно места, попробуйте что-то другое")
            return False

    @classmethod
    def remove(cls, title, qnt):
        if cls.__items[title] > qnt:
            print("Нужное количество есть на складе")
            cls.__items[title] -= qnt
            return True
        elif cls.__items[title] == qnt:
            print("Нужное количество есть на складе")
            cls.__items.pop(title, None)
            return True
        else:
            print("Не хватает на складе, попробуйте заказать меньше")
            return False

    @classmethod
    def _get_free_space(cls):
        return cls.__capacity - sum(cls.__items.values())

    @classmethod
    def _get_items(cls):
        return cls.__items

    @classmethod
    def print_items(cls):
        print("На складе хранится:\n")
        [print(value, key) for key, value in cls._get_items().items()]
        return ""

    @classmethod
    def _get_unique_items_count(cls):
        return len(cls.__items.keys())


class Shop(Storage):
    __items = {}
    __capacity = 20

    @classmethod
    def add(cls, title, qnt):
        if cls._get_free_space() >= qnt and cls._get_unique_items_count() < 5:
            cls.__items[title] = cls.__items.get(title, 0) + qnt
            return True
        else:
            print("В магазине недостаточно места, попробуйте что-то другое")
            return False

    @classmethod
    def remove(cls, title, qnt):
        if cls.__items[title] > qnt:
            print("Нужное количество есть в магазине")
            cls.__items[title] -= qnt
            return True
        elif cls.__items[title] == qnt:
            print("Нужное количество есть в магазине")
            cls.__items.pop(title, None)
            return True
        else:
            print("Не хватает в магазине, попробуйте заказать меньше")
            return False

    @classmethod
    def _get_free_space(cls):
        return cls.__capacity - sum(cls.__items.values())

    @classmethod
    def _get_items(cls):
        return cls.__items

    @classmethod
    def print_items(cls):
        print("В магазине хранится:\n")
        [print(value, key) for key, value in cls._get_items().items()]
        return ""

    @classmethod
    def _get_unique_items_count(cls):
        return len(cls.__items.keys())


class Request:
    def __init__(self, str_request):
        lst = self._get_info(str_request)
        self.from_ = lst[4]
        self.to = lst[6]
        self.amount = int(lst[1])
        self.product = lst[2]

    @staticmethod
    def _get_info(str_request):
        return str_request.split(" ")

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'
