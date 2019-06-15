from abc import ABCMeta, abstractmethod
import csv
import json
from ast import literal_eval as le

class Searchclient:
    def execute():
        a = input('Search by author, title, or year? -> ')
        b = input()





class Interface:
    def __init__(self):
        self.__modes = {'none': None, 'add': AddClient, 'search': SearchClient, 'delete': DeleteClient}
        self.__mode = self.__modes['none']

    def __set_mode(self):
        mode = input('add, search, or delete book? -> ')
        try:
            self.__mode = self.__modes[mode]
            return True
        except Exception:
            return False

    def execute(self):
        if not self.__set_mode():
            raise ValueError('Invalid input')
        self.__mode.execute()


if name == '__main__':
    a = Interface()
    a.execute()