import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, \
                            QToolBar, QAction, QStatusBar, \
                            QCheckBox, QWidget, QVBoxLayout, \
                            QTimeEdit, QPushButton, QLineEdit
from PyQt5.QtCore import Qt, QSize, QTime
from PyQt5.QtGui import QIcon
from qt_material import apply_stylesheet

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Calc Time')

        layout = QVBoxLayout()

        title = QLabel('Calculate Working Hours')
        title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.addWidget(title)

        events = [
            {'label': 'Enter start time:',
             'time': (7, 0)},
            {'label': 'Enter lunch start time:',
             'time': (11, 30)},
            {'label': 'Enter lunch end time:',
             'time': (12, 0)},
            {'label': 'Enter end time:',
             'time': (15, 30)}
        ]

        self.time_widgets = []

        for event in events:
            label = QLabel(event['label'])
            layout.addWidget(label)
            time = QTimeEdit(QTime(*event['time']))
            time.setDisplayFormat('HHmm')
            layout.addWidget(time)
            self.time_widgets.append(time)

        total_hours_label = QLabel('Total hours:')
        layout.addWidget(total_hours_label)
        total_hours = QLineEdit()
        layout.addWidget(total_hours)
        self.total_hours = total_hours


        calc_button = QPushButton('&Calculate')
        calc_button.clicked.connect(self.calculate)
        layout.addWidget(calc_button)

        layout_widget = QWidget()
        layout_widget.setLayout(layout)
        self.setCentralWidget(layout_widget)

        self.setStatusBar(QStatusBar(self))

    def calculate(self):
        start_time = datetime.strptime(self.time_widgets[0].time().toString(), '%H:%M:%S')
        lunch_start_time = datetime.strptime(self.time_widgets[1].time().toString(), '%H:%M:%S')
        lunch_end_time = datetime.strptime(self.time_widgets[2].time().toString(), '%H:%M:%S')
        end_time = datetime.strptime(self.time_widgets[3].time().toString(), '%H:%M:%S')

        total_time = end_time - start_time - (lunch_end_time - lunch_start_time)
        self.total_hours.setText(str(total_time))


app = QApplication(sys.argv)
apply_stylesheet(app, theme='dark_cyan.xml')

window=MainWindow()
window.show()

app.exec()
