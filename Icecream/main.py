
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QLabel, QFileDialog
)

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg, NavigationToolbar2QT
)

from About import AboutWindow


class IceCreamWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ice Cream Revenue")
        self.setFixedSize(800, 700)

        self.temperatures = []
        self.revenues = []

       
        self.title = QLabel("Ice Cream Revenue", self)
        self.title.setObjectName("title")
        self.title.setGeometry(30, 15, 500, 40)

      
        self.load_button = QPushButton("Choose CSV File", self)
        self.load_button.setGeometry(30, 75, 190, 40)

        self.file_label = QLabel("No file selected", self)
        self.file_label.setGeometry(235, 75, 400, 40)

       
        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(650, 75, 120, 40)

        self.fig, self.ax = plt.subplots(1, 1)

        self.canvas = FigureCanvasQTAgg(self.fig)
        self.canvas.setParent(self)
        self.canvas.setGeometry(30, 140, 740, 480)

       
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.setGeometry(30, 625, 740, 35)

     
        self.load_button.clicked.connect(self.load_file)
        self.about_button.clicked.connect(self.open_about)

       
        style_path = Path(__file__).parent / "style.qss"

        with open(style_path, "r", encoding="utf-8") as file:
            self.setStyleSheet(file.read())

        self.draw_graph()

    def load_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )

        if filename == "":
            return

        self.file_label.setText(Path(filename).name)

        
    self.temperatures = []
    self.revenues = []

    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            self.temperatures.append(float(row[0]))
            self.revenues.append(float(row[1]))

    self.draw_graph()


    def draw_graph(self):
        self.ax.clear()

      
        if len(self.temperatures) == 0:
            self.ax.set_title("Choose a CSV file")
            self.ax.set_xlabel("Temperature")
            self.ax.set_ylabel("Revenue")
            self.fig.tight_layout()
            self.canvas.draw()
            return

       
            self.ax.scatter(
        self.temperatures,
        self.revenues,
        s=1,
        color="blue",
        label="Data"
    )

       
        coefficients = np.polyfit(
            self.temperatures, self.revenues, 1
        )

        line_function = np.poly1d(coefficients)

        line_x = np.linspace(
            min(self.temperatures),
            max(self.temperatures),
            100
        )

        line_y = line_function(line_x)

        self.ax.plot(
            line_x, line_y,
            color="red",
            label="Trend Line"
        )

     
        self.ax.text(
            0.05, 0.90,
            f"y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}",
            transform=self.ax.transAxes,
            color="red"
        )

        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        self.ax.set_xlabel("Temperature")
        self.ax.set_ylabel("Revenue")
        self.ax.set_title("Ice Cream Revenue vs Temperature")

        self.ax.legend()

        self.fig.tight_layout()
        self.canvas.draw()

    def open_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()


app = QApplication(sys.argv)

window = IceCreamWindow()
window.show()

sys.exit(app.exec())
