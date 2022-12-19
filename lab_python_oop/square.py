from pymorphy2 import MorphAnalyzer
from translate import Translator
from webcolors import rgb_to_name

from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    """
    Класс «Квадрат» наследуется от класса «Прямоугольник».
    """
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, side_param):
        """
        Класс должен содержать конструктор по параметрам «сторона» и «цвет».
        """
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            MorphAnalyzer(lang='ru').parse(Translator(to_lang="Russian").translate(
                rgb_to_name(self.fc.colorproperty._color, spec='css3'))
            )[0].inflect({'gent'}).word,
            self.side,
            self.square()
        )
