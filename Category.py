import uuid

class Category():

    def __init__(self, name):
        self.__id = uuid.uuid1()
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name