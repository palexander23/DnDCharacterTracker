from PyQt5 import QtWidgets
import sys

from gui_elements import StatTracker as tracker

class SethTracker(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SethTracker, self).__init__(*args, **kwargs)

        self.setWindowTitle("Seth Tracker")
        
        # Construct all the stat trackers
        hp_track = tracker("HP:", 22, 22)
        temp_hp_track = tracker("Temp HP:", 0, 999)
        hit_dice_track = tracker("Hit Dice", 2, 4)
        lv1_spell_track = tracker("Lv.1 Spell Slots:", 1, 4)
        lv2_spell_track = tracker("Lv.2 Spell Slots:", 1, 3)
        bard_insp_track = tracker("Bardic Inspiration:", 2, 3)

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

        # Create set of group boxes
        health_group = QtWidgets.QGroupBox()
        health_group.setTitle("Health")
        health_group.setLayout(health_layout)

        spells_group = QtWidgets.QGroupBox()
        spells_group.setTitle("Spell Slots")
        spells_group.setLayout(spells_layout)

        bardic_group = QtWidgets.QGroupBox()
        bardic_group.setTitle("Bardic Abilities")
        bardic_group.setLayout(bardic_layout)

        # Create central layout to house all sublayouts
        self._central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self._central_widget)

        top_layout = QtWidgets.QVBoxLayout(self._central_widget)
        top_layout.addWidget(health_group)
        top_layout.addWidget(spells_group)
        top_layout.addWidget(bardic_group)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle('Fusion')

    window = SethTracker()
    window.show()

    app.exec_()
