import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class calculations:
    def flame_name(self, name1, name2):
        name1 = name1.lower()
        name2 = name2.lower()
        for i in name1:
            if i in name2:
                name1 = name1.replace(i, '', 1)
                name2 = name2.replace(i, '', 1)
        count = len(name1) + len(name2)
        flames = ['F', 'L', 'A', 'M', 'E', 'S']
        remove_index = (count % len(flames)) - 1
        while len(flames) > 1:
            flames.pop(remove_index)
            remove_index = (remove_index + count - 1) % len(flames)
        match(flames[0]):
            case 'F':
                return "Friends"
            case 'L':
                return "Love"
            case 'A':
                return "Affection"
            case 'M':
                return "Marriage"
            case 'E':
                return "Enemy"
            case 'S':
                return "Siblings"

    def percent(self, name1, name2):
        full_name = name1 + name2
        list_of_chars = []
        i = 0
        while i < len(full_name):
            count_char = (full_name).count(full_name[i])
            list_of_chars.append(count_char)
            full_name = full_name.replace(full_name[i], '')
        return list_of_chars

    def percentage(self, list_of_number):
        while len(list_of_number) > 2:
            new_list = []
            j = len(list_of_number) - 1
            if (j + 1) % 2:
                for i in range((j + 1) // 2):
                    list1 = []
                    sum_num = list_of_number[i] + list_of_number[j - i]
                    sum_num = int(sum_num)
                    while sum_num > 9:
                        list1.append(sum_num % 10)
                        sum_num = sum_num // 10
                    list1.append(sum_num)
                    list1.reverse()
                    new_list.extend(list1)
                new_list.append(list_of_number[len(list_of_number) // 2])
            else:
                for i in range(len(list_of_number) // 2):
                    list1 = []
                    sum_num = list_of_number[i] + list_of_number[j - i]
                    sum_num = int(sum_num)
                    while sum_num > 9:
                        list1.append(sum_num % 10)
                        sum_num = sum_num // 10
                    list1.append(sum_num)
                    list1.reverse()
                    new_list.extend(list1)

            list_of_number = []
            list_of_number.extend(new_list)
        return str(list_of_number[0]) + str(list_of_number[1])


class FlamesApp(QWidget, calculations):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setGeometry(400, 350, 500, 450)
        self.setFixedSize(500, 450)
        
        # Store widgets to manage them better
        self.widgets = {}

    def init_ui(self):
        """Initialize the main UI"""
        self.setWindowTitle("💖 FLAMES Calculator")
        self.set_background_color("#FFB6C1")  # Light pink
        
        # Main layout
        vbox = QVBoxLayout()
        vbox.setContentsMargins(50, 80, 50, 80)
        vbox.setSpacing(20)

        # Welcome label
        self.welcome_label = QLabel("💕 Welcome to FLAMES 💕", self)
        self.welcome_label.setStyleSheet(
            "color: #8B0000; font-size: 28px; font-weight: bold; font-family: Arial;"
        )
        self.welcome_label.setAlignment(Qt.AlignCenter)
        
        # Subtitle
        self.subtitle_label = QLabel("Discover your relationship destiny!", self)
        self.subtitle_label.setStyleSheet(
            "color: #C71585; font-size: 16px; font-style: italic; font-family: Arial;"
        )
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        
        # Start button
        self.start_button = QPushButton("🔥 Start FLAMES 🔥", self)
        self.start_button.setStyleSheet(
            """
            QPushButton {
                background-color: #FF1493;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 15px;
                border-radius: 10px;
                border: 2px solid #C71585;
            }
            QPushButton:hover {
                background-color: #FF69B4;
            }
            QPushButton:pressed {
                background-color: #C71585;
            }
            """
        )
        self.start_button.clicked.connect(self.show_input_screen)
        
        vbox.addWidget(self.welcome_label)
        vbox.addWidget(self.subtitle_label)
        vbox.addWidget(self.start_button)
        self.setLayout(vbox)

    def set_background_color(self, color):
        """Set background color of the window"""
        self.setStyleSheet(f"background-color: {color};")

    def clear_layout(self):
        """Clear all widgets from the layout"""
        if self.layout() is not None:
            while self.layout().count():
                child = self.layout().takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            # Delete the layout itself
            QWidget().setLayout(self.layout())

    def show_input_screen(self):
        """Display the input screen for entering names"""
        self.clear_layout()
        self.set_background_color("#FFE4E1")  # Misty rose
        
        vbox = QVBoxLayout()
        vbox.setContentsMargins(50, 40, 50, 40)
        vbox.setSpacing(15)

        # Title
        title = QLabel("Enter Names", self)
        title.setStyleSheet(
            "color: #8B0000; font-size: 24px; font-weight: bold; font-family: Arial;"
        )
        title.setAlignment(Qt.AlignCenter)
        
        # First name label
        label1 = QLabel("First Name:", self)
        label1.setStyleSheet("color: #8B0000; font-size: 16px; font-weight: bold;")
        
        # First name input
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setPlaceholderText("Enter first name...")
        self.lineedit1.setStyleSheet(
            """
            QLineEdit {
                background-color: white;
                color: #000;
                font-size: 16px;
                padding: 10px;
                border: 2px solid #FF69B4;
                border-radius: 8px;
            }
            QLineEdit:focus {
                border: 2px solid #FF1493;
            }
            """
        )
        
        # Second name label
        label2 = QLabel("Second Name:", self)
        label2.setStyleSheet("color: #8B0000; font-size: 16px; font-weight: bold;")
        
        # Second name input
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setPlaceholderText("Enter second name...")
        self.lineedit2.setStyleSheet(
            """
            QLineEdit {
                background-color: white;
                color: #000;
                font-size: 16px;
                padding: 10px;
                border: 2px solid #FF69B4;
                border-radius: 8px;
            }
            QLineEdit:focus {
                border: 2px solid #FF1493;
            }
            """
        )
        
        # Error label - shows placeholder by default
        self.error_label = QLabel("✏️ Write correct input", self)
        self.error_label.setStyleSheet(
            """
            color: #C71585;
            font-size: 14px;
            font-style: italic;
            """
        )
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setWordWrap(True)
        
        # Submit button
        self.submit_button = QPushButton("Calculate 💕", self)
        self.submit_button.setStyleSheet(
            """
            QPushButton {
                background-color: #FF1493;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 12px;
                border-radius: 10px;
                border: 2px solid #C71585;
            }
            QPushButton:hover {
                background-color: #FF69B4;
            }
            QPushButton:pressed {
                background-color: #C71585;
            }
            """
        )
        self.submit_button.clicked.connect(self.calculate_flames)
        
        # Add widgets to layout
        vbox.addWidget(title)
        vbox.addSpacing(10)
        vbox.addWidget(label1)
        vbox.addWidget(self.lineedit1)
        vbox.addWidget(label2)
        vbox.addWidget(self.lineedit2)
        vbox.addWidget(self.error_label)
        vbox.addWidget(self.submit_button)
        vbox.addStretch()
        
        self.setLayout(vbox)

    def calculate_flames(self):
        """Calculate and display FLAMES result"""
        name1 = self.lineedit1.text().strip().lower()
        name2 = self.lineedit2.text().strip().lower()
        
        # Validation
        if not name1 or not name2:
            self.show_error("⚠️ Both names are required!")
            return
        
        if not (name1.isalpha() and name2.isalpha()):
            self.show_error("⚠️ Invalid Input!\nPlease enter names containing only alphabets.")
            return
        
        if name1 == name2:
            self.show_error("⚠️ Names cannot be the same!")
            return
        
        # Store names as instance variables (before clearing layout)
        self.name1_lower = name1
        self.name2_lower = name2
        self.name1_display = self.lineedit1.text().strip().title()
        self.name2_display = self.lineedit2.text().strip().title()
        
        # Calculate result
        result = self.flame_name(name1, name2)
        
        # Display result
        self.show_result_screen(result)

    def show_error(self, message):
        """Display error message then reset to placeholder"""
        self.error_label.setText(message)
        self.error_label.setStyleSheet(
            """
            color: #DC143C;
            font-size: 14px;
            font-weight: bold;
            background-color: #FFE4E4;
            padding: 10px;
            border: 2px solid #DC143C;
            border-radius: 5px;
            """
        )
        self.error_label.show()
        self.lineedit1.clear()
        self.lineedit2.clear()
        self.lineedit1.setFocus()
        
        # Reset back to placeholder after 3 seconds
        from PyQt5.QtCore import QTimer
        def reset_label():
            self.error_label.setText("✏️ Write correct input")
            self.error_label.setStyleSheet(
                "color: #C71585; font-size: 14px; font-style: italic;"
            )
        QTimer.singleShot(3000, reset_label)

    def show_result_screen(self, result):
        """Display FLAMES result screen"""
        self.clear_layout()
        self.set_background_color("#FFE4E1")

        vbox = QVBoxLayout()
        vbox.setContentsMargins(30, 30, 30, 30)
        vbox.setSpacing(12)

        # Title
        title = QLabel("💖 FLAMES Result 💖", self)
        title.setStyleSheet(
            "color: #8B0000; font-size: 24px; font-weight: bold; font-family: Arial;"
        )
        title.setAlignment(Qt.AlignCenter)

        # Names label - smaller font so long names don't overflow
        names_label = QLabel(f"{self.name1_display}  &  {self.name2_display}", self)
        names_label.setStyleSheet(
            """
            color: #8B0000;
            font-size: 15px;
            font-weight: bold;
            background-color: white;
            padding: 10px;
            border: 2px solid #FF69B4;
            border-radius: 10px;
            """
        )
        names_label.setAlignment(Qt.AlignCenter)
        names_label.setWordWrap(True)

        # "are" label
        are_label = QLabel("are", self)
        are_label.setStyleSheet("color: #8B0000; font-size: 16px; font-style: italic;")
        are_label.setAlignment(Qt.AlignCenter)

        # Result label - large and prominent
        result_label = QLabel(f"💕 {result} 💕", self)
        result_label.setStyleSheet(
            """
            color: #C71585;
            font-size: 28px;
            font-weight: bold;
            background-color: white;
            padding: 20px;
            border: 3px solid #FF69B4;
            border-radius: 15px;
            """
        )
        result_label.setAlignment(Qt.AlignCenter)
        result_label.setWordWrap(True)

        # Percentage button
        percentage_button = QPushButton("🔍 See Percentage Match", self)
        percentage_button.setStyleSheet(
            """
            QPushButton {
                background-color: #FF1493;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 12px;
                border-radius: 10px;
                border: 2px solid #C71585;
            }
            QPushButton:hover {
                background-color: #FF69B4;
            }
            """
        )
        percentage_button.clicked.connect(self.show_percentage_screen)

        vbox.addWidget(title)
        vbox.addWidget(names_label)
        vbox.addWidget(are_label)
        vbox.addWidget(result_label)
        vbox.addWidget(percentage_button)
        vbox.addStretch()

        self.setLayout(vbox)

    def show_percentage_screen(self):
        """Display percentage result screen"""
        # Use stored names instead of accessing deleted widgets
        name1 = self.name1_lower
        name2 = self.name2_lower
        
        # Calculate percentage
        result_percentage = self.percentage(self.percent(name1, name2))
        
        self.clear_layout()
        self.set_background_color("#FFE4E1")
        
        vbox = QVBoxLayout()
        vbox.setContentsMargins(40, 40, 40, 40)
        vbox.setSpacing(20)
        
        # Title
        title = QLabel("💯 Compatibility Score 💯", self)
        title.setStyleSheet(
            "color: #8B0000; font-size: 26px; font-weight: bold; font-family: Arial;"
        )
        title.setAlignment(Qt.AlignCenter)
        
        # Percentage display
        percentage_text = f"{self.name1_display} & {self.name2_display}\n\n{result_percentage}%\n\nCompatible!"
        percentage_label = QLabel(percentage_text, self)
        percentage_label.setStyleSheet(
            """
            color: #C71585;
            font-size: 22px;
            font-weight: bold;
            background-color: white;
            padding: 30px;
            border: 3px solid #FF69B4;
            border-radius: 15px;
            """
        )
        percentage_label.setAlignment(Qt.AlignCenter)
        percentage_label.setWordWrap(True)
        
        # Restart button
        restart_button = QPushButton("🔄 Try Again", self)
        restart_button.setStyleSheet(
            """
            QPushButton {
                background-color: #FF69B4;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 12px;
                border-radius: 10px;
                border: 2px solid #FF1493;
            }
            QPushButton:hover {
                background-color: #FF1493;
            }
            """
        )
        restart_button.clicked.connect(self.show_input_screen)
        
        # Exit button
        exit_button = QPushButton("❌ Exit", self)
        exit_button.setStyleSheet(
            """
            QPushButton {
                background-color: #8B0000;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 12px;
                border-radius: 10px;
                border: 2px solid #600000;
            }
            QPushButton:hover {
                background-color: #600000;
            }
            """
        )
        exit_button.clicked.connect(QApplication.quit)
        
        vbox.addWidget(title)
        vbox.addWidget(percentage_label)
        vbox.addWidget(restart_button)
        vbox.addWidget(exit_button)
        vbox.addStretch()
        
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    flames_app = FlamesApp()
    flames_app.show()
    sys.exit(app.exec_())