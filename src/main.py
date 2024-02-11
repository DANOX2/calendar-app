import sys
# import time
# from PyQt5.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class TimeBlockLayout(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.grid_layout = QGridLayout(self)
        self.setLayout(self.grid_layout)

        # Add days of the week labels
        for i, day in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]):
            label = QLabel(day)
            self.grid_layout.addWidget(label, 0, i + 1)

        # Add hour labels
        for hour in range(24):
            label = QLabel(f"{hour:02d}:00")
            self.grid_layout.addWidget(label, hour, 0)

        # Add time blocks (placeholder)
        # Replace this with your logic to create and add time block widgets
            
    # Create empty time block widgets (placeholder)
        self.time_blocks = [[None for _ in range(7)] for _ in range(24)]
        for hour in range(24):
            for day in range(7):
                self.time_blocks[hour][day] = QLineEdit("")
                self.time_blocks[hour][day].setStyleSheet("background-color: white")
                self.grid_layout.addWidget(self.time_blocks[hour][day], hour, day + 1)

    def set_time_block(self, hour, day, text, color="#ffffff"):
        """Sets the text and color of a specific time block."""
        if 0 <= hour < 24 and 0 <= day < 7:
            self.time_blocks[hour][day].setText(text)
            self.time_blocks[hour][day].setStyleSheet(f"background-color: {color}")

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    window = TimeBlockLayout()

    # Set some example time blocks
    window.set_time_block(9, 0, "Meeting", "#ff9999")
    window.set_time_block(14, 3, "Lunch break", "#99ff99")
    window.set_time_block(19, 5, "Workout", "#99ccff")
    window.set_time_block(17, 4, "Workout2", "#99ccff")


    window.show()
    sys.exit(app.exec())

# import sys
# import random
# from PySide6 import QtCore, QtWidgets, QtGui

# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

#         self.button = QtWidgets.QPushButton("Click me!")
#         self.text = QtWidgets.QLabel("Hello World",
#                                     alignment=QtCore.Qt.AlignCenter)

#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)

#         self.button.clicked.connect(self.magic)

#     @QtCore.Slot()
#     def magic(self):
#         self.text.setText(random.choice(self.hello))

# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])

#     widget = MyWidget()
#     widget.resize(800, 600)
#     widget.show()

#     sys.exit(app.exec())