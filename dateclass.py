class Date:
    '''
Разработка класса данных
Примеры:
date = Date(2018, 11, 23)
print(date) # 23.11.2018
repr(date)  # Date(2018, 11, 23)

date = Date(2018, 11, 31)

date.date = '31.11.2018'
print(date.date) # '31.11.2018'

date.day   = 31 # Запрет
date.month = 50 #
date.month = 11 # 02 -> 01.03
date.year       # на след. месяц

Example:
date = Date(2019, 5, 22)
print(date)
    '''

    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))

    def __init__(self, year, month, day):
        '''
        year:  int otherwise TypeError
        month: int 1 < month <= 12

        '''

        self.is_valid_date(year, month, day)
        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self):
        return self.date

    def __repr__(self):
        return f'Date({repr(self.__year)}, {self.__month!r}, {self.__day!r})'

    @staticmethod
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100) or not year % 400:
            return True
        else:
            return False

    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month - 1]

    @property
    def date(self):
        return f'{self.__day}.{self.__month}.{self.__year}'

    @classmethod
    def is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')

        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')

        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format')

        try:
            day = int(value[0])
            month = int(value[1])
            year = int(value[2])
            self.is_valid_date(year, month, day)
        except:
            raise ValueError('Invalid date format')

        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    #     @day.setter
    #     def day(self, value):
    #         value = int(value)
    #         self.is_valid_date(self.__year, self.__month, value)
    #         self.__day = value

    @property
    def month(self):
        return self.__month

    #     @month.setter
    #     def month(self, value):
    #         value = int(value)
    #         self.is_valid_date(self.__year, value, self.__day)
    #         self.__month = value

    @property
    def year(self):
        return self.__year

    #     @year.setter
    #     def year(self, value):
    #         value = int(value)
    #         self.is_valid_date(value, self.__month, self.__day)
    #         self.__year = value

    def add_day(self, day):
        pass

    def add_month(self, month):
        pass

    def add_year(self, year):
        pass

    @staticmethod
    def date2_date1(date2, date1):
        pass
        # date2-date1
d = Date(2000, 6, 23)
print(repr(d))


class A:


    def __str__(self):
        return f'Привет!'

    def __repr__(self):
        return f'A()'


class B:

    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'B({self.a!r})'



a = A()
b = B(a)

print(repr(b))