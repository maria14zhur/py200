# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 2. Инкапсуляция, наследование, полиморфизм
# Абстрактные классы

# Лабораторная работа № 2.3 (6 ак.ч.)

# Слушатель (ФИО): Журавлева М.А.

# ---------------------------------------------------------------------------------------------

# 1
# Разработайте два абстрактных класса:
# - IReader с абстрактным методом read, который принимает строку с названием файла,
#   а возвращает словарь со ключами и их значениями или None;
# - IWriter с методом write, который принимает строку с названием файла и 
#   словарь со ключами и их значениями. Возвращает True, если запись успешно выполнена,
#   иначе False
# Метод IReader.read читает данные из файла
# Метод IWriter записывает данные в файла
# Наследуйтесь от класса IReader:
# - JSONReader: читает файл формата json;
# - CSVReader: читает файл формата csv;
# Наследуйтесь от класса IWriter:
# - JSONWriter: записывает файл формата json;
# - CSVWriter: записывает файл формата csv;

from abc import ABCMeta, abstractmethod
import csv
import json
from ast import literal_eval as le


class IReader(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def read(path: str):
        pass


class IWriter(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def write(path: str, data):
        pass


class JSONReader(IReader):
    @staticmethod
    def read(path: str):
        try:
            with open(path, 'r', newline='') as file:
                data = json.load(file)
            return data
        except Exception:
            return None


class CSVReader(IReader):
    @staticmethod
    def read(path: str, delimiter=','):
        data = []
        try:
            with open(path, 'r', newline='') as file:
                reader = csv.DictReader(file, delimiter=delimiter)
                for row in reader:
                    data.append(dict(row))
            return data
        except Exception:
            return None


class JSONWriter(IWriter):
    @staticmethod
    def write(path: str, data: list)->bool:
        try:
            with open(path, 'w') as file:
                json.dump(data, file)
            return True
        except Exception:
            return False


class CSVWriter(IWriter):
    @staticmethod
    def write(path: str, data: list, delimiter=',')->bool:
        try:
            with open(path, 'a', newline='') as file:
                headers = [key for key in data[0]]
                writer = csv.DictWriter(file, delimiter=delimiter, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
            return True
        except Exception:
            return False

# 2
# Шаблон стратегия
# Класс ReadClient содержит ссылки на JSONReader и CSVWriter.
# Нужный драйвер чтения файла автоматически выбирается исходя из расширения файла .csv или .json.


class ReadClient:
    def __init__(self):
        self.__readers = {'none': 'None', 'cvs': CSVReader, 'json': JSONReader}
        self.__current_reader = self.__readers['none']

    def read(self, path):
        if not self.__set_reader(self.__get_ext_from_path(path)):
            return False
        return self.__current_reader.read(path)

    def add_reader(self, reader, file_extension):
        if not issubclass(reader, IReader):
            raise TypeError('Invalid reader type')
        self.__readers[file_extension] = reader

    def __set_reader(self, file_extension):
        try:
            self.__current_reader = self.__readers[file_extension]
            return True
        except Exception:
            return False

    @staticmethod
    def __get_ext_from_path(path):
        try:
            return path.split('.')[-1]
        except Exception:
            raise TypeError('Invalid path')


# 3
# Шаблон стратегия
# Класс WriteClient содержит ссылки на JSONWriter и CSVWriter.
# Нужный драйвер выбирает пользователь с помощью метода WriteClient.set_driver(driver_name)


class WriteClient:
    def __init__(self, writer='none'):
        self.__writers = {'none': None, 'csv': CSVWriter, 'json': JSONWriter}
        self.__current_writer = self.__writers[writer]

    def write(self, path, data):
        if self.__current_writer is None:
            return False
        return self.__current_writer.write(path, data)

    def add_writer(self, writer, driver_name):
        if not issubclass(writer, IWriter):
            raise TypeError('Invalid writer type')
        self.__writers[driver_name] = writer

    def set_driver(self, driver_name):
        try:
            self.__current_writer = self.__writers[driver_name]
            return True
        except Exception:
            return False

# 4
# Интерактивное взаимодействие с ReadClient и WriteClient.
# С помощью input() пользователь может выбрать ReadClient или WriteClient.
# Далее пользователь пишет название файл. Если WriteClient, то запрашивает формат.
# Если ReadClient, то автоматически читает файл с нужным форматом и выводит на экран в виде словаря.
# Если WriteClient, то пользователь пишет словарь в виде строки, а затем передаётся в exec.


class Interface():
    def __init__(self):
        self.__modes = {'none': None, 'read': ReadClient, 'write': WriteClient}
        self.__mode = self.__modes['none']

    def __set_mode(self):
        mode = input('read or write? -> ')
        try:
            self.__mode = self.__modes[mode]
            return True
        except Exception:
            return False

    def execute(self):
        if not self.__set_mode():
            raise ValueError('Invalid input')
        path = input('Enter path> ')
        if self.__mode == ReadClient:
            print(ReadClient.read(ReadClient(), path))
        elif self.__mode == WriteClient:
            driver = input('Enter driver> ')
            data = le(input('Enter data> '))
            print(WriteClient.write(WriteClient(writer=driver), path, data))


a = Interface()
a.execute()
