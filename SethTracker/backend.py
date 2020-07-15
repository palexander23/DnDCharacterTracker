import json

from gui_elements import StatTracker


class JSONBackend():
    def __init__(self, _stat_tracker_list: [StatTracker]):
        self.stat_tracker_list = _stat_tracker_list

        # Function for generating the slot functions
        # Each lambda function is tied to a tracker variable
        # Encapsulating the lambda in a lower scope ensures each lamda has a
        # different tracker variable
        def generate_value_change_slot(tracker):
            return lambda: self.process_value_change(tracker)

        # Set up slots for stat trackers:
        for i, stat_tracker in enumerate(self.stat_tracker_list):
            stat_tracker.spinBoxSignal()[str].connect(
                generate_value_change_slot(stat_tracker)
            )

    def process_value_change(self, stat_tracker: StatTracker):
        print("Stat Tracker: {}".format(stat_tracker.getLabelText()))
        print("Value Now:    {}".format(stat_tracker.getSpinBoxValue()))
