from PyQt5 import QtWidgets
import sys

import gui_elements


class SethTracker(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SethTracker, self).__init__(*args, **kwargs)

        self.setWindowTitle("Seth Tracker")

        testTracker = gui_elements.StatTracker("Test:", 5, 10)

        self.setCentralWidget(testTracker)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle('Fusion')

    window = SethTracker()
    window.show()

    app.exec_()
