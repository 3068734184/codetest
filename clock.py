import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QTimer, QTime


class ClockWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cool Clock')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setFixedSize(300, 100)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size: 30px;')
        self.label.setGeometry(0, 0, 300, 100)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 更新时间间隔为1秒

    def update_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.label.setText(current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClockWindow()
    window.show()
    sys.exit(app.exec_())
