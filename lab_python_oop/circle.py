from pymorphy2 import MorphAnalyzer
from translate import Translator
from webcolors import rgb_to_name

from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
    """
    Класс «Круг» наследуется от класса «Геометрическая фигура».
    """
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, r_param):
        """
        Класс должен содержать конструктор по параметрам «радиус» и «цвет». В конструкторе создается объект класса «Цвет фигуры» для хранения цвета.
        """
        self.r = r_param
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def square(self):
        """
        Класс должен переопределять метод, вычисляющий площадь фигуры.
        """
        return math.pi * (self.r ** 2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {:.3f}.'.format(
            Circle.get_figure_type(),
            MorphAnalyzer(lang='ru').parse(Translator(to_lang="Russian").translate(
                rgb_to_name(self.fc.colorproperty._color, spec='css3')),
            )[0].inflect({'gent'}).word,
            self.r,
            self.square()
        )
