class Pi:

    @staticmethod
    def g_pi():
        return 3.14

    @property
    def get_pi(self):
        return self.g_pi

p = Pi()
print(p.get_pi())

class A:
    var = 2
    _pvar = 3
    __ppvar = 4

    def __init__(self):
        self.varie = 5
        self._pvarie = 6
        self.__ppvarie = 7

    def meth(self):
        return 1

    def _pmeth(self):
        return 2

    def __ppmeth(self):
        return 3

    @classmethod
    def cmeth(cls):
        return 4

    @classmethod
    def _pcmeth(cls):
        return 7

    @classmethod
    def __ppcmeth(cls):
        return '!'

    @staticmethod
    def smeth():
        return 4

    @staticmethod
    def _psmeth():
        return 7

    @staticmethod
    def __ppsmeth():
        return A._A__ppcmeth()


class B(A):

    def __init__(self):
        A.__init__(self)
        self.j = self.varie
        self.h = self._pvarie
        self.k = self._A__ppvarie
        self.m = self.meth()
        self.n = self._pmeth()
        self.v = A._A__ppmeth(self)


    a = A.smeth()
    b = A._psmeth()
    c = A._A__ppsmeth()
    d = A.var
    e = A._pvar
    f = A._A__ppvar
    g = A.cmeth()
    h = A._pcmeth()
    i = A._A__ppsmeth()


a = B()
print(A._A__ppcmeth())
