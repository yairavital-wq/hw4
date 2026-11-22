
from PySide6.QtWidgets import QWidget, QLabel


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("About")
        self.setFixedSize(450, 240)

        title = QLabel("Ice Cream Revenue", self)
        title.setGeometry(30, 20, 390, 40)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        name = QLabel("Created by: Yair Avital", self)
        name.setGeometry(30, 75, 390, 30)

        email = QLabel("Email: yair.avital@s.afeka.ac.il", self)
        email.setGeometry(30, 110, 390, 30)

        github = QLabel(
            '<a href="https://github.com/yairavital-wq/hw4/tree/master/Icecream">GitHub repository</a>',
            self
        )

        github.setGeometry(30, 155, 390, 30)
        github.setOpenExternalLinks(True)
