from lab_python_oop.circle import Circle
from lab_python_oop.color import FigureColor
from lab_python_oop.square import Square
from lab_python_oop.rectangle import Rectangle

N = 19


def main():
    rcol = FigureColor()
    rcol.colorproperty = (0, 0, 255)
    rect = Rectangle(rcol, N, N)
    print(rect.__repr__())

    ccol = FigureColor()
    ccol.colorproperty = (0, 0, 0
                          )
    circ = Circle(ccol, N)
    print(circ.__repr__())

    scol = FigureColor()
    scol.colorproperty = (255, 0, 0)
    sq = Square(scol, N)
    print(sq.__repr__())


if __name__ == "__main__":
    main()
