# osnovnoi fail
import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMenu
from PyQt5.QtCore import Qt, QTimer, QSettings, QPoint
from PyQt5.QtGui import QPainter, QRadialGradient, QLinearGradient, QColor, QFont, QIcon

class XamperDesktop(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Xamper")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(QApplication.primaryScreen().geometry())

        self.settings = QSettings("~/.config/xamper/config", QSettings.IniFormat)
        self.gradient_type = self.settings.value("gradient_type", "black_blue")

        self.font = QFont("Monospace", 120)
        self.font.setBold(True)

        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 120px; color: white;")
        self.time_label.setFont(self.font)
        self.update_time()
        self.time_label.setGeometry(0, self.height() // 2 - 100, self.width(), 150)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.select_gradient_button = QPushButton(self)
        self.select_gradient_button.setGeometry(10, 10, 30, 30)
        self.select_gradient_button.setStyleSheet("background-color: rgba(255, 255, 255, 0.3); border: none;")
        self.select_gradient_button.setIcon(QIcon.fromTheme("preferences-desktop-theme"))
        self.select_gradient_button.clicked.connect(self.select_gradient)

        self.weather_label = QLabel(self)
        self.weather_label.setAlignment(Qt.AlignLeft)
        self.weather_label.setStyleSheet("font-size: 24px; color: white;")
        self.weather_label.setText("Weather: ☀️ 25°C")
        self.weather_label.setGeometry(20, self.height() - 100, 300, 50)

        self.cpu_label = QLabel(self)
        self.cpu_label.setAlignment(Qt.AlignLeft)
        self.cpu_label.setStyleSheet("font-size: 24px; color: white;")
        self.cpu_label.setGeometry(20, self.height() - 150, 300, 50)

        self.memory_label = QLabel(self)
        self.memory_label.setAlignment(Qt.AlignLeft)
        self.memory_label.setStyleSheet("font-size: 24px; color: white;")
        self.memory_label.setGeometry(20, self.height() - 200, 300, 50)

        self.metrics_timer = QTimer()
        self.metrics_timer.timeout.connect(self.update_metrics)
        self.metrics_timer.start(2000)

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect()

        gradient = QLinearGradient(rect.topLeft(), rect.bottomRight())
        if self.gradient_type == "black_blue":
            gradient.setColorAt(0, QColor(0, 0, 0))
            gradient.setColorAt(1, QColor(0, 0, 64))
        elif self.gradient_type == "black_green":
            gradient.setColorAt(0, QColor(0, 0, 0))
            gradient.setColorAt(1, QColor(0, 64, 0))
        elif self.gradient_type == "black_purple":
            gradient.setColorAt(0, QColor(0, 0, 0))
            gradient.setColorAt(1, QColor(64, 0, 64))
        elif self.gradient_type == "black_orange":
            gradient.setColorAt(0, QColor(0, 0, 0))
            gradient.setColorAt(1, QColor(64, 32, 0))
        elif self.gradient_type == "black_red":
            gradient.setColorAt(0, QColor(0, 0, 0))
            gradient.setColorAt(1, QColor(64, 0, 0))
        elif self.gradient_type == "black_white":
            gradient.setColorAt(0, QColor(0, 0, 0))
            gradient.setColorAt(1, QColor(64, 64, 64))

        painter.fillRect(rect, gradient)

        self.draw_gradient_circles(painter)

    def draw_gradient_circles(self, painter):
        rect = self.rect()
        center_x, center_y = rect.center().x(), rect.center().y()

        gradient1 = QRadialGradient(center_x + 200, center_y + 200, 150, center_x + 200, center_y + 200)
        gradient1.setColorAt(0, QColor(255, 255, 255, 100))
        gradient1.setColorAt(1, QColor(0, 0, 0, 0))
        painter.setBrush(gradient1)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(center_x + 100, center_y + 100, 300, 300)

        gradient2 = QRadialGradient(center_x - 200, center_y - 200, 150, center_x - 200, center_y - 200)
        gradient2.setColorAt(0, QColor(255, 255, 255, 100))
        gradient2.setColorAt(1, QColor(0, 0, 0, 0))
        painter.setBrush(gradient2)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(center_x - 400, center_y - 400, 300, 300)

    def update_time(self):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        self.time_label.setText(current_time)

    def update_metrics(self):
        cpu_percent = psutil.cpu_percent()
        self.cpu_label.setText(f"CPU: {cpu_percent}%")

        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent
        self.memory_label.setText(f"RAM: {memory_percent}%")

    def select_gradient(self):
        menu = QMenu(self)
        gradients = {
            "Black-Blue": "black_blue",
            "Black-Green": "black_green",
            "Black-Purple": "black_purple",
            "Black-Orange": "black_orange",
            "Black-Red": "black_red",
            "Black-White": "black_white"
        }
        for name, gradient_type in gradients.items():
            action = menu.addAction(name)
            action.triggered.connect(lambda _, gt=gradient_type: self.set_gradient(gt))
        menu.exec_(self.select_gradient_button.mapToGlobal(QPoint(0, 0)))

    def set_gradient(self, gradient_type):
        self.gradient_type = gradient_type
        self.settings.setValue("gradient_type", gradient_type)
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    desktop = XamperDesktop()
    desktop.show()
    sys.exit(app.exec_())

