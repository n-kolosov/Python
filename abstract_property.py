from abc import ABCMeta, abstractmethod
class MyClass1(metaclass=ABCMeta):
    def __init__(self, value):
        self.__var = value
    @property
    @abstractmethod
    def v(self):
        return self.__var
    @v.setter
    @abstractmethod
    def v(self, value):
        self.__var = value
    @v.deleter
    @abstractmethod
    def v(self):
        del self.__var