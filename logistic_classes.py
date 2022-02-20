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
        else:
            print("На складе недостаточно места, попробуйте что-то другое")

    @classmethod
    def remove(cls, title, qnt):
        if cls.__items[title] > qnt:
            cls.__items[title] -= qnt
        elif cls.__items[title] == qnt:
            cls.__items.pop(title, None)
        else:
            print("Не хватает на складе, попробуйте заказать меньше")

    @classmethod
    def _get_free_space(cls):
        return cls.__capacity - sum(cls.__items.values())

    @classmethod
    def _get_items(cls):
        return cls.__items

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
        else:
            print("В магазине недостаточно места, попробуйте что-то другое")

    @classmethod
    def remove(cls, title, qnt):
        if cls.__items[title] > qnt:
            cls.__items[title] -= qnt
        elif cls.__items[title] == qnt:
            cls.__items.pop(title, None)
        else:
            print("Не хватает в магазине, попробуйте заказать меньше")

    @classmethod
    def _get_free_space(cls):
        return cls.__capacity - sum(cls.__items.values())

    @classmethod
    def _get_items(cls):
        return cls.__items

    @classmethod
    def _get_unique_items_count(cls):
        return len(cls.__items.keys())
