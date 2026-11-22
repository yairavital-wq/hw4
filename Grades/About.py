
from PySide6.QtWidgets import QWidget, QLabel


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("About")
        self.setFixedSize(420, 230)

        title = QLabel("Grades Correction", self)
        title.setGeometry(30, 20, 360, 35)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        author = QLabel("Created by: Yair Avital", self)
        author.setGeometry(30, 75, 360, 30)

        email = QLabel("Email: yair.avital@s.afeka.ac.il", self)
        email.setGeometry(30, 110, 360, 30)

        github = QLabel(
            '<a href="https://github.com/YOUR_USERNAME/HW4-Grades">GitHub repository</a>',
            self
        )
        github.setGeometry(30, 150, 360, 30)
        github.setOpenExternalLinks(True)
