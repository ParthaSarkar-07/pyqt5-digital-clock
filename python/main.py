import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFontDatabase, QFont


class DigitalClock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 400, 150)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # Alignment
        self.time_label.setAlignment(Qt.AlignCenter)

        # Load Custom Font
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")

        if font_id == -1:
            print("Font not loaded! Check file path.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            custom_font = QFont(font_family, 150)
            self.time_label.setFont(custom_font)

        # Styling
        self.time_label.setStyleSheet("color: #25ff00;")
        self.setStyleSheet("background-color: black;")

        # Timer setup
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())