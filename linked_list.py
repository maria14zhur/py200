# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Журавлева М.А.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        if not (isinstance(capacity_volume, float) and isinstance(occupied_volume, float)):
            raise TypeError
        if not (capacity_volume > 0 and 0 <= occupied_volume <= capacity_volume):
            raise ValueError
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.
small_glass = Glass(100., 0.)
middle_glass = Glass(200., 0.)
big_glass = Glass(400., 0.)

small_glass.occupied_volume = 100
small_glass.capacity_volume += 50


# print(small_glass.__dict__)
# print(middle_glass.__dict__)
# print(big_glass.__dict__)



# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:
    def __init__(self, capacity_volume, occupied_volume=0.):
        if not (isinstance(capacity_volume, float) and isinstance(occupied_volume, float)):
            raise TypeError
        if not (capacity_volume > 0 and 0 <= occupied_volume <= capacity_volume):
            raise ValueError
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


glass1 = GlassDefaultArg(250.)
glass2 = GlassDefaultArg(250., 200.)




# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?

class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)


glass3 = GlassDefaultListArg(200.)
glass4 = GlassDefaultListArg(200.)
glass5 = GlassDefaultListArg(200.)

 


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.

class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume):
        if not (isinstance(capacity_volume, float) and isinstance(occupied_volume, float)):
            raise TypeError
        if not (capacity_volume > 0 and 0 <= occupied_volume <= capacity_volume):
            raise ValueError
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def add_water(self, volume):
        volume = volume
        if not isinstance(volume, float):
            raise TypeError
        if not 0 <= volume <= (self.capacity_volume - self.occupied_volume):
            raise ValueError
        self.occupied_volume += volume

    def remove_water(self, volume):
        volume = volume
        if not isinstance(volume, float):
            raise TypeError
        if not (0 <= (self.occupied_volume - volume) and volume >= 0):
            raise ValueError
        self.occupied_volume -= volume


add_glass = GlassAddRemove(250., 100.)
add_glass.add_water(150.)
rem_glass = GlassAddRemove(250., 100.)
rem_glass.remove_water(100.)

# print(add_glass.__dir__())
# print(rem_glass.__dir__())
# print(GlassAddRemove.__dir__)
# print(type(add_glass))
# print(type(rem_glass))
# print(type(GlassAddRemove))

# 6. Создайте три объекта типа GlassAddRemove, 
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.

class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume):
        print('at beginning: ', self.__dir__())
        if not (isinstance(capacity_volume, float) and isinstance(occupied_volume, float)):
            raise TypeError
        if not (capacity_volume > 0 and 0 <= occupied_volume <= capacity_volume):
            raise ValueError
        self.capacity_volume = capacity_volume
        print('in middle: ', self.__dir__())
        self.occupied_volume = occupied_volume
        print('in the end: ', self.__dir__())


glassy = GlassAddRemove(200., 50.)
print('after: ', glassy.__dir__())



# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.

class Glass:
    def __init__(self):
        print(hex(id(self)))
        self.capacity_volume = 500
        self.occupied_volume = 0


print('Glass 1')
glass1 = Glass()
print(hex(id(glass1)))
print('Glass 2')
glass2 = Glass()
print(hex(id(glass2)))
print('Glass 3')
glass3 = Glass()
print(hex(id(glass3)))
# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.



# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d:
	def __init__(f, a=2):
		f.a = a
		
	def print_me(p):
		print(p.a)
		
# d.print_me(d())

# 10. Исправьте
class A:
	def __init__(self, a):
		if 10 < a < 50:
			return
		self.a = a;	

# Объясните так реализовывать __init__ нельзя?
# При такой реализации из-за return  прерывается выполнения метода  __init__ ,
# но поскольку ошибка не вызывается можно подумать, что объект успешно создан

# 11. Циклическая зависимость (стр. 39-44)

from weakref import ref


class LinkedList:
    class __Node:
        def __init__(self, data=None, prev=None, next_=None):
            if prev is None:
                self.__prev = prev
            else:
                self.__prev = ref(prev)
            self.__next = next_
            self.__data = data

        @property
        def next_(self):
            return self.__next

        @next_.setter
        def next_(self, next_):
            self.__next = next_

        @property
        def prev(self):
            return self.__prev()

        @prev.setter
        def prev(self, prev):
            self.__prev = ref(prev)

        @property
        def data(self):
            return self.__data

        def __str__(self):
            return f'previous:{self.__prev}, next:{self.__next}'

        def __repr__(self):
            return f'LinkedList.__Node({self.__data!r}, {self.__prev!r}, {self.__next!r})'

    def __init__(self, head=None, tail=None, size=0):
        if head is None:
            self.__head = LinkedList.__Node()
            self.__tail = LinkedList.__Node()
        self.__head.next_ = self.__tail
        self.__tail.prev = self.__head
        self.__size = size

    def __push(self, current_node, data):
        """
        Contain data in node, place node after current_node
        :return: None
        """
        new_node = LinkedList.__Node(data, current_node, current_node.next_)
        current_node.next_.prev = new_node
        current_node.next_ = new_node
        self.__size += 1

    def __pop(self, current_node):
        """
        Delete current_node
        :return: current_node
        """
        del_node = current_node
        del_node.prev.next_ = del_node.next_
        del_node.next_.prev = del_node.prev
        self.__size -= 1
        return del_node.data

    def insert(self, data, index=0):
        """
        Insert Node to any place of LinkedList
        :param data: node for insertion
        :param index: position of node
        :return: None
        """
        if type(index) != int or index < 0:
            raise ValueError('Invalid index')
        if index > (self.__size - 1):
            self.append(data)
        elif index < self.__size//2:
            current_node = self.__head
            for _ in range(index):
                current_node = current_node.next_
            self.__push(current_node, data)
        else:
            current_node = self.__tail.prev
            for _ in range(self.__size - index):
                current_node = current_node.prev
            self.__push(current_node, data)

    def append(self, data):
        """
        Append Node before tail of LinkedList
        :param data: node to append
        :return: None
        """
        self.__push(self.__tail.prev, data)

    def clear(self):
        """
        Clear LinkedList
        :return: None
        """
        self.__head.next_ = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def find(self, data):
        """
        Finds index of given node in LinkedList
        :param data: node to find
        :return: index of node in LinkedList
        """
        link = self.__head.next_
        for i in range(self.__size):
            if link.data == data:
                return i
            link = link.next_
        else:
            return 'No such node in LinkedList'

    def remove(self, data):
        """
        Remove node from LinkedList
        :param node: node to remove
        :return: None
        """
        link = self.__head.next_
        for i in range(self.__size):
            if link.data == data:
                self.__pop(link)
                return None
            link = link.next_

    def delete(self, index):
        """
        Delete node
        :param index: index of node to delete
        :return: node
        """
        if type(index) != int or index < 0:
            raise ValueError('Invalid index')
        elif index < self.__size//2:
            position = self.__head.next_
            for _ in range(index):
                position = position.next_
            return self.__pop(position)
        else:
            position = self.__tail.prev
            for _ in range(self.__size - index -1):
                position = position.prev
            return self.__pop(position)

    def __str__(self):
        return f'LinkedList. Number of elements:{self.__size}'

    def __repr__(self):
        return f'LinkedList({self.__head!r}, {self.__tail!r},{self.__size!r})'




















