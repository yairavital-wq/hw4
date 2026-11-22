
import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QTableWidget, QTableWidgetItem, QSpinBox,
    QFileDialog, QMessageBox
)


class GradesWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grades Correction")
        self.setFixedSize(720, 640)

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ""

        # Title
        self.title_label = QLabel("Grades Correction", self)
        self.title_label.setObjectName("title")
        self.title_label.setGeometry(25, 15, 450, 40)

        # Choose file
        self.load_button = QPushButton("Choose grades.csv", self)
        self.load_button.setGeometry(25, 75, 200, 38)

        self.file_label = QLabel("No file selected", self)
        self.file_label.setGeometry(240, 75, 455, 38)

        # Grades table
        self.table = QTableWidget(self)
        self.table.setGeometry(25, 130, 670, 365)
        self.table.setRowCount(50)
        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Original Grades",
            "Corrected Grades"
        ])

        self.table.setColumnWidth(0, 205)
        self.table.setColumnWidth(1, 210)
        self.table.setColumnWidth(2, 230)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Bonus input
        self.bonus_label = QLabel("Bonus points:", self)
        self.bonus_label.setGeometry(25, 515, 115, 35)

        self.bonus_input = QSpinBox(self)
        self.bonus_input.setGeometry(145, 515, 110, 35)
        self.bonus_input.setRange(0, 100)

        # Update button
        self.update_button = QPushButton("Update File", self)
        self.update_button.setGeometry(275, 515, 185, 38)

        # About button
        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(480, 515, 215, 38)

        # Status
        self.status_label = QLabel("Choose a CSV file to begin.", self)
        self.status_label.setGeometry(25, 575, 670, 35)

        # Connect buttons
        self.load_button.clicked.connect(self.load_file)
        self.bonus_input.lineEdit().returnPressed.connect(
            self.update_grades
        )
        self.update_button.clicked.connect(self.save_file)
        self.about_button.clicked.connect(self.open_about)

        # Load QSS file
        style_path = Path(__file__).parent / "style.qss"

        with open(style_path, "r", encoding="utf-8") as style_file:
            self.setStyleSheet(style_file.read())

    def load_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select grades file", "", "CSV Files (*.csv)"
        )

        if filename == "":
            return

        self.selected_file = filename
        self.file_label.setText(Path(filename).name)

       self.student_ids = []
self.original_grades = []
self.corrected_grades = []

with open(self.selected_file, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    next(reader)


self.update_table()

        self.status_label.setText("File selected.")

    def update_table(self):
        self.table.clearContents()

        for i in range(min(len(self.student_ids), 50)):
            self.table.setItem(
                i, 0, QTableWidgetItem(str(self.student_ids[i]))
            )
            self.table.setItem(
                i, 1, QTableWidgetItem(str(self.original_grades[i]))
            )
            self.table.setItem(
                i, 2, QTableWidgetItem(str(self.corrected_grades[i]))
            )

    def update_grades(self):
        bonus = self.bonus_input.value()

        # YOUR CODE:
        # Calculate corrected grades
        # Maximum grade is 100

        self.status_label.setText(f"Bonus entered: {bonus}")

    def save_file(self):
        if self.selected_file == "":
            QMessageBox.warning(
                self, "Error", "Choose a CSV file first."
            )
            return

        # YOUR CODE:
        # Save corrected grades to original CSV file

        # QDesktopServices.openUrl(
        #     QUrl.fromLocalFile(self.selected_file)
        # )

        self.status_label.setText("Complete CSV saving code.")

    def open_about(self):
        from About import AboutWindow

        self.about_window = AboutWindow()
        self.about_window.show()


app = QApplication(sys.argv)

window = GradesWindow()
window.show()

sys.exit(app.exec())
