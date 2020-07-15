import json
import os

from gui_elements import StatTracker


class StatTrackerCODEC(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, StatTracker):
            # Create dictionary from o
            tracker_dict = {
                "__stat_tracker__": True,
                "label": o.getLabelText(),
                "value": o.getSpinBoxValue(),
                "min": o.getSpinBoxMin(),
                "max": o.getSpinBoxMax()
            }

            return(tracker_dict)

        else:
            return super().default(o)

class JSONBackend():
    def __init__(self, _stat_tracker_list: [StatTracker], _json_file_path):
        self.stat_tracker_list = _stat_tracker_list
        self.json_file_path = _json_file_path

        self.init_json_file()

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
        """ Used as the slot to the value changed signals of the StatTrackers
        
        Gets the new value and the label of the tracker from the StatTracker
        it is passed at when the signal-slot relationship is built.

        :param stat_tracker: The tracker that this slot is assigned to 
        """
        print("Stat Tracker: {}".format(stat_tracker.getLabelText()))
        print("Value Now:    {}".format(stat_tracker.getSpinBoxValue()))


    def init_json_file(self):
        """ Initialise the file handling functionality of the backend
        """
        # Check to see whether a file needs to be made from scratch
        if not os.path.isfile(self.json_file_path):
            self.create_json_file()
            return



    def create_json_file(self):
        """ Generate a new JSON file based on stat values given in the gui
        initialisation.
        """
            with open(self.json_file_path, "w") as json_file:
                json.dump(self.stat_tracker_list,
                          json_file,
                          cls=StatTrackerCODEC,
                          indent=4)

            