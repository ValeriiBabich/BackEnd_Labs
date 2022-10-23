from uuid import uuid1
from datetime import datetime


class Note:
    def __init__(self, user_id, category_id, cost):
        self.__id = uuid1()
        self.__user_id = user_id
        self.__category_id = category_id
        self.__date = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
        self.__cost = cost

    def get_id(self):
        return self.__id

    def get_user_id(self):
        return self.__user_id

    def get_category_id(self):
        return self.__category_id

    def get_date(self):
        return self.__date

    def get_cost(self):
        return self.__cost
