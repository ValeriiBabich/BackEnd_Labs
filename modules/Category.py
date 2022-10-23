from uuid import uuid1


class Category:

    def __init__(self, name):
        self.__id = uuid1()
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
