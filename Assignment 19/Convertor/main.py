import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_convert.clicked.connect(self.generate_conversion)
        self.ui.combo_list.currentIndexChanged.connect(self.update_combo_boxes)
        self.ui.combo_list.addItems(["Weight", "Length", "Temperature", "Digital Size"])

        self.conversion_functions = {
            "Weight": self.convert_weight,
            "Length": self.convert_length,
            "Temperature": self.convert_temperature,
            "Digital Size": self.convert_digital_size
        }

        self.update_combo_boxes()  

    def update_combo_boxes(self):
        self.ui.combo_from.clear()
        self.ui.combo_to.clear()
        selected_item = self.ui.combo_list.currentText()

        if selected_item in self.conversion_functions:
            units = self.get_units(selected_item)
            self.ui.combo_from.addItems(units)
            self.ui.combo_to.addItems(units)

    def get_units(self, category):
        if category == "Weight":
            return ["Gram", "Kilogram", "Ton", "Pound"]
        elif category == "Length":
            return ["Millimeter", "Centimeter", "Meter", "Kilometer", "Inch"]
        elif category == "Temperature":
            return ["Centigrade", "Fahrenheit", "Kelvin"]
        elif category == "Digital Size":
            return ["Bit", "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"]
        else:
            return []

    def generate_conversion(self):
        from_unit = self.ui.combo_from.currentText()
        to_unit = self.ui.combo_to.currentText()
        value = float(self.ui.text_get.text())
        selected_category = self.ui.combo_list.currentText()

        if selected_category in self.conversion_functions:
            conversion_function = self.conversion_functions[selected_category]
            result = conversion_function(from_unit, to_unit, value)
            if result is not None:
                self.ui.text_show.setText(str(result))
            else:
                self.ui.text_show.setText("Unsupported conversion")
        else:
            self.ui.text_show.setText("Unsupported category")


    def convert_weight(self, from_unit, to_unit, value):
        if from_unit == to_unit:
            return value
        elif from_unit == "Gram":
            if to_unit == "Kilogram":
                return value / 1000
            elif to_unit == "Ton":
                return value / 1e6
            elif to_unit == "Pound":
                return value * 0.00220462
        elif from_unit == "Kilogram":
            if to_unit == "Gram":
                return value * 1000
            elif to_unit == "Ton":
                return value / 1000
            elif to_unit == "Pound":
                return value * 2.20462
        elif from_unit == "Ton":
            if to_unit == "Gram":
                return value * 1e6
            elif to_unit == "Kilogram":
                return value * 1000
            elif to_unit == "Pound":
                return value * 2204.62
        elif from_unit == "Pound":
            if to_unit == "Gram":
                return value / 0.00220462
            elif to_unit == "Kilogram":
                return value / 2.20462
            elif to_unit == "Ton":
                return value / 2204.62
        return None


    def convert_length(self, from_unit, to_unit, value):
        if from_unit == to_unit:
            return value
        elif from_unit == "Millimeter":
            if to_unit == "Centimeter":
                return value / 10
            elif to_unit == "Meter":
                return value / 1000
            elif to_unit == "Kilometer":
                return value / 1e6
            elif to_unit == "Inch":
                return value * 0.0393701
        elif from_unit == "Centimeter":
            if to_unit == "Millimeter":
                return value * 10
            elif to_unit == "Meter":
                return value / 100
            elif to_unit == "Kilometer":
                return value / 100000
            elif to_unit == "Inch":
                return value * 0.393701
        elif from_unit == "Meter":
            if to_unit == "Millimeter":
                return value * 1000
            elif to_unit == "Centimeter":
                return value * 100
            elif to_unit == "Kilometer":
                return value / 1000
            elif to_unit == "Inch":
                return value * 39.3701
        elif from_unit == "Kilometer":
            if to_unit == "Millimeter":
                return value * 1e6
            elif to_unit == "Centimeter":
                return value * 100000
            elif to_unit == "Meter":
                return value * 1000
            elif to_unit == "Inch":
                return value * 39370.1
        elif from_unit == "Inch":
            if to_unit == "Millimeter":
                return value / 0.0393701
            elif to_unit == "Centimeter":
                return value / 0.393701
            elif to_unit == "Meter":
                return value / 39.3701
            elif to_unit == "Kilometer":
                return value / 39370.1
        return None 


    def convert_temperature(self, from_unit, to_unit, value):
        if from_unit == to_unit:
            return value
        elif from_unit == "Centigrade":
            if to_unit == "Fahrenheit":
                return value * 1.8 + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Centigrade":
                return (value - 32) / 1.8
            elif to_unit == "Kelvin":
                return (value + 459.67) * 5 / 9
        elif from_unit == "Kelvin":
            if to_unit == "Centigrade":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return value * 9 / 5 - 459.67
        return None


    def convert_digital_size(self, from_unit, to_unit, value):
        if from_unit == to_unit:
            return value
        elif from_unit == "Bit":
            if to_unit == "Byte":
                return value / 8
            elif to_unit == "Kilobyte":
                return value / 8e3
            elif to_unit == "Megabyte":
                return value / 8e6
            elif to_unit == "Gigabyte":
                return value / 8e9
            elif to_unit == "Terabyte":
                return value / 8e12
        elif from_unit == "Byte":
            if to_unit == "Bit":
                return value * 8
            elif to_unit == "Kilobyte":
                return value / 1000
            elif to_unit == "Megabyte":
                return value / 1e6
            elif to_unit == "Gigabyte":
                return value / 1e9
            elif to_unit == "Terabyte":
                return value / 1e12
        elif from_unit == "Kilobyte":
            if to_unit == "Bit":
                return value * 8e3
            elif to_unit == "Byte":
                return value * 1000
            elif to_unit == "Megabyte":
                return value / 1000
            elif to_unit == "Gigabyte":
                return value / 1e6
            elif to_unit == "Terabyte":
                return value / 1e9
        elif from_unit == "Megabyte":
            if to_unit == "Bit":
                return value * 8e6
            elif to_unit == "Byte":
                return value * 1e6
            elif to_unit == "Kilobyte":
                return value * 1000
            elif to_unit == "Gigabyte":
                return value / 1000
            elif to_unit == "Terabyte":
                return value / 1e6
        elif from_unit == "Gigabyte":
            if to_unit == "Bit":
                return value * 8e9
            elif to_unit == "Byte":
                return value * 1e9
            elif to_unit == "Kilobyte":
                return value * 1e6
            elif to_unit == "Megabyte":
                return value * 1000
            elif to_unit == "Terabyte":
                return value / 1000
        elif from_unit == "Terabyte":
            if to_unit == "Bit":
                return value * 8e12
            elif to_unit == "Byte":
                return value * 1e12
            elif to_unit == "Kilobyte":
                return value * 1e9
            elif to_unit == "Megabyte":
                return value * 1e6
            elif to_unit == "Gigabyte":
                return value * 1000
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
