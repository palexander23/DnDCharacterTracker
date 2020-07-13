import sys
sys.path.insert(0, "./SethTracker")

from gui_elements import StatTracker


def test_stat_tracker(qtbot):
    # Create stat tracker instance and add it to qbot
    stat_tracker_widget = StatTracker("Test", 5, 10, 3)

    qtbot.addWidget(stat_tracker_widget)

    # Test constructor set values
    assert stat_tracker_widget.getLabelText() == "Test"
    assert stat_tracker_widget.getSpinBoxMax() == 10
    assert stat_tracker_widget.getSpinBoxMin() == 3
    assert stat_tracker_widget.getSpinBoxValue() == 5

    # Test get/set interface
    stat_tracker_widget.setLabelText("Label")
    stat_tracker_widget.setSpinBoxMax(20)
    stat_tracker_widget.setSpinBoxMin(1)
    stat_tracker_widget.setSpinBoxValue(8)

    assert stat_tracker_widget.getLabelText() == "Label"
    assert stat_tracker_widget.getSpinBoxMax() == 20
    assert stat_tracker_widget.getSpinBoxMin() == 1
    assert stat_tracker_widget.getSpinBoxValue() == 8

    # Test value changed signal
    # Create an integer in a list container that a slot function can mutate
    test_value = [0]

    # Define slot function
    def saveValue(test_list):
        test_list[0] = stat_tracker_widget.getSpinBoxValue()

    stat_tracker_widget.spinBoxSignal()[int].connect(lambda: saveValue(test_value))

    stat_tracker_widget.setSpinBoxValue(4)
    assert test_value[0] == 4

    stat_tracker_widget.setSpinBoxValue(8)
    assert test_value[0] == 8

    stat_tracker_widget.setSpinBoxValue(999)
    assert test_value[0] == stat_tracker_widget.getSpinBoxMax()
    
    stat_tracker_widget.setSpinBoxValue(-999)
    assert test_value[0] == stat_tracker_widget.getSpinBoxMin()
