from PySide6.QtWidgets import QWidget, QApplication
from login import loginUI

# 登录UI显示函数
class Mywindow(QWidget, loginUI):
    def __init__(self):
        super().__init__()
        # 显示登录界面的ui
        self.setupUi(self)
        # 读取确定按键
        self.pushButton.clicked.connect(self.loginButtonFunction)

    def loginButtonFunction(self):
        account = self.lineEdit_2.text()
        password = self.lineEdit.text()
        # 密码账号检测
        if (account == '123' and password == '123'):
            print("欢迎登陆")
        else:
            print("密码错误！")

if __name__ == '__main__':
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()
