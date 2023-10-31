from PySide6.QtWidgets import QWidget, QApplication
from caculater import caculaterUI


class Mywindow(QWidget, caculaterUI):
    def __init__(self):
        super().__init__()
        # 定义一个空列表
        self.reuslt = ''
        self.setupUi(self)
        self.bindButton()

    def bindButton(self):
        self.pushButton_0.clicked.connect(lambda: self.addNum('0'))
        self.pushButton_1.clicked.connect(lambda: self.addNum('1'))
        self.pushButton_2.clicked.connect(lambda: self.addNum('2'))
        self.pushButton_3.clicked.connect(lambda: self.addNum('3'))
        self.pushButton_4.clicked.connect(lambda: self.addNum('4'))
        self.pushButton_5.clicked.connect(lambda: self.addNum('5'))
        self.pushButton_6.clicked.connect(lambda: self.addNum('6'))
        self.pushButton_7.clicked.connect(lambda: self.addNum('7'))
        self.pushButton_8.clicked.connect(lambda: self.addNum('8'))
        self.pushButton_9.clicked.connect(lambda: self.addNum('9'))
        self.pushButton_10.clicked.connect(lambda: self.addNum('.'))
        self.pushButton_plus.clicked.connect(lambda: self.addNum('+'))
        self.pushButton_sub.clicked.connect(lambda: self.addNum('-'))
        self.pushButton_mul.clicked.connect(lambda: self.addNum('*'))
        self.pushButton_div.clicked.connect(lambda: self.addNum('/'))
        self.pushButton_cal.clicked.connect(self.caculaterFunction)
        self.pushButton_back.clicked.connect(self.backFunction)
        self.pushButton_clear.clicked.connect(self.clearFunction)

    # 添加新的数字（字符）
    def addNum(self, Number):
        # 清屏
        self.lineEdit.clear()
        # 把输入的数字加进去
        self.reuslt += Number
        # 把加入后的数字（字符）进行显示
        self.lineEdit.setText(self.reuslt)

    # 计算函数
    def caculaterFunction(self):
        # 清屏
        self.lineEdit.clear()
        # 这里注意，Line输出必须是str类型，否则会报错，因此需要加强转换
        self.lineEdit.setText(str(eval(self.reuslt)))

    # 退格函数
    def backFunction(self):
        self.reuslt = self.reuslt[:-1]
        self.lineEdit.setText(self.reuslt)

    # 清屏函数
    def clearFunction(self):
        self.reuslt = ''
        self.lineEdit.setText(self.reuslt)


if __name__ == '__main__':
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()
