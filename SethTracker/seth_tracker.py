from PyQt5 import QtWidgets, QtGui
import sys

from gui_elements import StatTracker as tracker
from backend import JSONBackend


class SethTracker(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SethTracker, self).__init__(*args, **kwargs)

        self.setWindowTitle("Seth Tracker")

        self.initGui()
        
        self._backend = JSONBackend(self._stat_tracker_list, "./data.json")

    def initGui(self):
        # Construct all the stat trackers
        hp_track = tracker("HP:", 22, 22)
        temp_hp_track = tracker("Temp HP:", 0, 999)
        hit_dice_track = tracker("Hit Dice:", 2, 4)
        lv1_spell_track = tracker("Lv.1 Spell Slots:", 1, 4)
        lv2_spell_track = tracker("Lv.2 Spell Slots:", 1, 3)
        bard_insp_track = tracker("Bardic Inspiration:", 2, 3)

        self._stat_tracker_list = [hp_track,
                                   temp_hp_track,
                                   hit_dice_track,
                                   lv1_spell_track,
                                   lv2_spell_track,
                                   bard_insp_track]

        # Group trackers into catagories
        health_layout = QtWidgets.QVBoxLayout()
        health_layout.addWidget(hp_track)
        health_layout.addWidget(temp_hp_track)
        health_layout.addWidget(hit_dice_track)

        spells_layout = QtWidgets.QVBoxLayout()
        spells_layout.addWidget(lv1_spell_track)
        spells_layout.addWidget(lv2_spell_track)

        bardic_layout = QtWidgets.QVBoxLayout()
        bardic_layout.addWidget(bard_insp_track)

        # Create set of group boxes and apply title font
        box_title_font = QtGui.QFont()
        box_title_font.setPointSize(11)
        box_title_font.setWeight(59)

        health_group = QtWidgets.QGroupBox()
        health_group.setTitle("Health")
        health_group.setFont(box_title_font)
        health_group.setLayout(health_layout)

        spells_group = QtWidgets.QGroupBox()
        spells_group.setTitle("Spell Slots")
        spells_group.setFont(box_title_font)
        spells_group.setLayout(spells_layout)

        bardic_group = QtWidgets.QGroupBox()
        bardic_group.setTitle("Bardic Abilities")
        bardic_group.setFont(box_title_font)
        bardic_group.setLayout(bardic_layout)

        # Create long rest button
        long_rest_button = QtWidgets.QPushButton()
        long_rest_button.setText("Long Rest")
        long_rest_button.setFont(box_title_font)
        long_rest_button.clicked.connect(self.long_rest)

        # Create central layout to house all sublayouts
        self._central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self._central_widget)

        top_layout = QtWidgets.QVBoxLayout(self._central_widget)
        top_layout.addWidget(health_group)
        top_layout.addWidget(spells_group)
        top_layout.addWidget(bardic_group)
        top_layout.addWidget(long_rest_button)

    def long_rest(self):
        # Reset HP
        self._stat_tracker_list[0].setSpinBoxValue(
            self._stat_tracker_list[0].getSpinBoxMax()
        )

        # Add half of Hit Dice
        self._stat_tracker_list[2].setSpinBoxValue(
            self._stat_tracker_list[2].getSpinBoxValue() + 
            self._stat_tracker_list[2].getSpinBoxMax()/2
        )

        # Reset Spell Slots
        self._stat_tracker_list[3].setSpinBoxValue(
            self._stat_tracker_list[3].getSpinBoxMax()
        )

        self._stat_tracker_list[4].setSpinBoxValue(
            self._stat_tracker_list[4].getSpinBoxMax()
        )

        # Reset Bardic Inspiration
        self._stat_tracker_list[5].setSpinBoxValue(
            self._stat_tracker_list[5].getSpinBoxMax()
        )

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle('Fusion')

    window = SethTracker()
    window.show()

    app.exec_()
