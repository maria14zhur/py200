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
        day: int 1 <day <= 31
        '''

        self.__is_valid_date(year, month, day)
        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self):
        return self.date

    def __repr__(self):
        return f'Date({repr(self.__year)}, {self.__month!r}, {self.__day!r})'

    @staticmethod
    def __is_leap_year(year):
        if (year % 4 == 0 and year % 100) or not year % 400:
            return True
        else:
            return False

    @classmethod
    def __get_max_day(cls, year, month):
        leap_year = 1 if cls.__is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month - 1]

    @property
    def date(self):
        return f'{self.__day}.{self.__month}.{self.__year}'

    @classmethod
    def __is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')
        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')
        if not 0 < day <= cls.__get_max_day(year, month):
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
            self.__is_valid_date(year, month, day)
        except:
            raise ValueError('Invalid date format')

        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @classmethod
    def __days_of_year(cls, month, year):
        days = 0
        for i in range(month):
            days += cls.__get_max_day(year, i+1)
        return days

    @classmethod
    def date2_date1(cls, date2, date1):
        if date2.year == date1.year:
            date2_days = cls.__days_of_year(date2.month-1, date2.year) + date2.day
            date1_days = cls.__days_of_year(date1.month-1, date1.year) + date1.day
            delta = date2_days - date1_days
        else:
            date2_days = 365 + cls.__days_of_year(date2.month-1, date2.year) + date2.day
            if cls.__is_leap_year(date2.year - 1):
                date2_days += 1
            date1_days = cls.__days_of_year(date1.month-1, date1.year) + date1.day
            delta = date2_days - date1_days
            for i in range(date2.year - date1.year - 1):
                delta += 365
                if cls.__is_leap_year(date2.year - 2 - i):
                    delta += 1
        return delta



