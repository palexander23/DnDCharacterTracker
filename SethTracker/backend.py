import json
import os

from gui_elements import StatTracker


class StatTrackerCODEC(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, StatTracker):
            # Create dictionary from o
            tracker_dict = self.tracker_to_dict(o)
            return(tracker_dict)

        else:
            return super().default(o)

    def tracker_to_dict(self, tracker: StatTracker):
        tracker_dict = {
                "__stat_tracker__": True,
                "label": tracker.getLabelText(),
                "value": tracker.getSpinBoxValue(),
                "min": tracker.getSpinBoxMin(),
                "max": tracker.getSpinBoxMax()
            }
        return(tracker_dict)

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
        
        # Find the dict in the dict list with the right label
        dict_index = self.get_dict_index(stat_tracker.getLabelText())

        # Set dict list value and write to disk
        self._json_dicts[dict_index]["value"] = stat_tracker.getSpinBoxValue()
        self.save_json_changes()

    def init_json_file(self):
        """ Initialise the file handling functionality of the backend
        """
        # Check to see whether a file needs to be made from scratch
        if not os.path.isfile(self.json_file_path):
            with open(self.json_file_path, "w") as json_file:
                json_file.write("[]")

        # If a file exists, read its contents
        with open(self.json_file_path, "r") as json_file:
            self._json_dicts = json.load(json_file)

        # Extract a list of labels from the json file 
        json_labels = [tracker["label"] for tracker in self._json_dicts]

        # Copy the stat tracker list
        # Remove those that are represented in the JSON
        unrepresented_trackers = [tracker 
                                  for tracker in self.stat_tracker_list
                                  if tracker.getLabelText() not in json_labels]

        if unrepresented_trackers:
            self.add_unrepresented_trackers(unrepresented_trackers)

        # Finally, set the parameters of the StatTrackers from the JSON file
        for tracker in self.stat_tracker_list:
            dict_index = self.get_dict_index(tracker.getLabelText())

            tracker.setSpinBoxValue(self._json_dicts[dict_index]["value"])
            tracker.setSpinBoxMin(self._json_dicts[dict_index]["min"])
            tracker.setSpinBoxMax(self._json_dicts[dict_index]["max"])

    def save_json_changes(self):
        """ Save changes to the json_dict member to disk """
        with open(self.json_file_path, "w") as json_file:
            json.dump(self.stat_tracker_list,
                        json_file,
                        cls=StatTrackerCODEC,
                        indent=4)

    def add_unrepresented_trackers(self, trackers):
        """Add unrepresented trackers to the JSON file
        :param trackers: List of unrepresented trackers
        """

        # Parse trackers into dict
        unrepresented_dict = [StatTrackerCODEC().tracker_to_dict(tracker) 
                              for tracker in trackers]

        # Add unrepresented trackers to central dictionary
        self._json_dicts = self._json_dicts + unrepresented_dict

        # Copy central dictionary to disk
        self.save_json_changes()

    def get_dict_index(self, label: str):
        """ Get the index of the json_dicts entry with the given label

        :param label: The label of the required dict
        """

        return(next(i for i, item in enumerate(self._json_dicts) 
                    if item["label"] == label))
