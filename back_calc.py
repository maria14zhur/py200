class BackendCalc:

    @staticmethod
    def add(l, r):
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l + r

    @staticmethod
    def sub(l, r):
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l - r

    @staticmethod
    def mul(l, r):
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l * r

    @staticmethod
    def div(l, r):
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l / r


class SimpleCalcFrontend:
    @staticmethod
    def execute():
        s = input('Input expression ->')
        l = s.split()
        if len(l) != 3:
            print('Invalid format')
            return
        a, op, b = l

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('a and b must be int or float')
            return

        ops = {'+': BackendCalc.add, '-': BackendCalc.sub, '/': BackendCalc.div,
                   '*': BackendCalc.mul}
        try:
            ans = ops[op](a,b)
        except KeyError:
            print(f'Invalid format: operation "{op}" is not defined')
            return
        print(ans)


class BackendLogCalc:
    __add_cnt = 0
    __sub_cnt = 0
    __mul_cnt = 0
    __div_cnt = 0

    @classmethod
    def log(cls):
        return f'Invocations: add - {cls.__add_cnt}, sub - {cls.__sub_cnt}, mul - {cls.__mul_cnt}, div - {cls.__div_cnt}'

    @classmethod
    def add(cls, l, r):
        cls.__add_cnt += 1
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l + r

    @classmethod
    def sub(cls, l, r):
        cls.__sub_cnt += 1
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l - r

    @classmethod
    def mul(cls, l, r):
        cls.__mul_cnt += 1
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l * r

    @classmethod
    def div(cls, l, r):
        cls.__div_cnt += 1
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l / r


class LogCalcFrontend:
    @staticmethod
    def execute():
        s = input('Input expression ->')
        l = s.split()
        if len(l) != 3:
            print('Invalid format')
            return
        a, op, b = l

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('a and b must be int or float')
            return

        ops = {'+': BackendLogCalc.add, '-': BackendLogCalc.sub, '/': BackendLogCalc.div, '*': BackendLogCalc.mul}
        try:
            ans = ops[op](a, b)
        except KeyError:
            print(f'Invalid format: operation "{op}" is not defined')
            return
        print(ans, BackendLogCalc.log())


class BackendLogTypeCalc:
    __add_cnt = {}
    __sub_cnt = {}
    __mul_cnt = {}
    __div_cnt = {}

    def get_stat(self):
        return f'Invocations: add - {self.__add_cnt}, sub - {self.__sub_cnt}, mul - {self.__mul_cnt}, div - {self.__div_cnt}'

    @classmethod
    def add(cls, frontend, l, r):
        try:
            cls.__add_cnt[frontend] += 1
        except KeyError:
            cls.__add_cnt[frontend] = 1
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l + r

    @classmethod
    def sub(cls, frontend, l, r):
        try:
            cls.__sub_cnt[frontend] += 1
        except KeyError:
            cls.__sub_cnt[frontend] = 1
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l - r

    @classmethod
    def mul(cls, frontend, l, r):
        try:
            cls.__mul_cnt[frontend] += 1
        except KeyError:
            cls.__mul_cnt[frontend] = 1
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l * r

    @classmethod
    def div(cls, frontend, l, r):
        try:
            cls.__div_cnt[frontend] += 1
        except KeyError:
            cls.__div_cnt[frontend] = 1
        if not isinstance(l, (int, float)) and not isinstance(r, (int, float)):
            raise TypeError("l and r must be int or float")
        return l / r


class LogCalcTypeFrontend:
    @classmethod
    def execute(cls):
        s = input('Input expression ->')
        l = s.split()
        if len(l) != 3:
            print('Invalid format')
            return
        a, op, b = l
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('a and b must be int or float')
            return

        ops = {'+': BackendLogTypeCalc.add, '-': BackendLogTypeCalc.sub, '/': BackendLogTypeCalc.div, '*': BackendLogTypeCalc.mul}
        try:
            ans = ops[op](cls.__name__, a, b)
        except KeyError:
            print(f'Invalid format: operation "{op}" is not defined')
            return
        print(ans)


class LogCalcTypeFrontend2:
    def __init__(self, backend, name):
        self.__backend = backend
        self.__name = name

    def execute(self):
        s = input('Input expression ->')
        l = s.split()
        if len(l) != 3:
            print('Invalid format')
            return
        a, op, b = l
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('a and b must be int or float')
            return

        ops = {'+': self.__backend.add, '-': self.__backend.sub, '/': self.__backend.div, '*': self.__backend.mul}
        try:
            ans = ops[op](self.__name, a, b)
        except KeyError:
            print(f'Invalid format: operation "{op}" is not defined')
            return
        print(ans)


backend1 = BackendLogTypeCalc()
backend2 = BackendLogTypeCalc()

frontend1 = LogCalcTypeFrontend2(backend1, 'frontend1')
frontend2 = LogCalcTypeFrontend2(backend1, 'frontend2')
frontend3 = LogCalcTypeFrontend2(backend2, 'frontend3')

frontend1.execute()
frontend2.execute()
print(backend1.get_stat())