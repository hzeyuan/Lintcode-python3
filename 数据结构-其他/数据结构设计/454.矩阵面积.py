"""
454. 矩阵面积
实现一个矩阵类Rectangle，包含如下的一些成员变量与函数：

两个共有的成员变量 width 和 height 分别代表宽度和高度。
一个构造函数，接受2个参数 width 和 height 来设定矩阵的宽度和高度。
一个成员函数 getArea，返回这个矩阵的面积。
样例
Java:
    Rectangle rec = new Rectangle(3, 4);
    rec.getArea(); // should get 12

Python:
    rec = Rectangle(3, 4)
    rec.getArea()
"""


class Rectangle:
    """
     * Define a constructor which expects two parameters width and height here.
    """

    def __init__(self, height, width):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    # write your code here

    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''


r = Rectangle(3, 4)
print(r.getArea())
