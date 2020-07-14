from PyQt5 import QtGui, QtWidgets


class StatTracker(QtWidgets.QWidget):

    def __init__(self, label_text, current_value, max_value, min_value=0):
        super(StatTracker, self).__init__()

        self._label = QtWidgets.QLabel(self, text=label_text)

        label_font = QtGui.QFont()
        label_font.setBold(True)
        label_font.setPointSize(11)

        self._label.setFont(label_font)

        # Create Spin box and set necessary values
        self._spinbox = QtWidgets.QSpinBox(self)

        self._spinbox.setMaximum(max_value)
        self._spinbox.setMinimum(min_value)
        self._spinbox.setValue(current_value)

        # Set spinbox font
        spinbox_font = QtGui.QFont()
        spinbox_font.setPointSize(label_font.pointSize())

        self._spinbox.setFont(spinbox_font)

        # Create HBox layout and add above widgets
        layout = QtWidgets.QGridLayout(self)

        layout.addWidget(self._label, 0, 0, 1, 4)
        layout.addWidget(self._spinbox, 0, 5, 1, 1)

        layout.setContentsMargins(20, 2, 20, 0)

        self.setLayout(layout)
        self._spinbox.setFixedWidth(50)

    def getLabelText(self):
        return(self._label.text())

    def setLabelText(self, text):
        self._label.setText(text)

    def getSpinBoxMax(self):
        return(self._spinbox.maximum())

    def setSpinBoxMax(self, max):
        self._spinbox.setMaximum(max)

    def getSpinBoxMin(self):
        return(self._spinbox.minimum())

    def setSpinBoxMin(self, min):
        self._spinbox.setMinimum(min)

    def getSpinBoxValue(self):
        return self._spinbox.value()

    def setSpinBoxValue(self, value):
        self._spinbox.setValue(value)

    def spinBoxSignal(self):
        return(self._spinbox.valueChanged)
