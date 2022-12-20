import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QTextEdit, QVBoxLayout, QWidget)


class PickerWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.setWindowTitle("Christmas Friend Picker")
        self.friends_picked = 0
        self.input_edit = QTextEdit()
        self.pick_button = QPushButton("Pick a Friend")
        self.result_label = QLabel("Your selected friend is: ")
        self.selected_friend_label = QLabel()
        self.clear_button = QPushButton("Clear")

        self.pick_button.setEnabled(False)
        self.clear_button.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.input_edit)
        layout.addWidget(self.pick_button)
        result_layout = QHBoxLayout()
        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.selected_friend_label)
        layout.addLayout(result_layout)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

        # Connect signals and slots
        self.pick_button.clicked.connect(self.pick_friend)
        self.clear_button.clicked.connect(self.clear)
        self.input_edit.textChanged.connect(self.input_changed)

    def pick_friend(self):
        names = self.input_edit.toPlainText().strip().split(",")
        names = [name.strip() for name in names]
        if not names:
            self.selected_friend_label.setText("No names left to choose from!")
            return

        chosen_name = random.choice(names)
        self.selected_friend_label.setText(chosen_name)
        names.remove(chosen_name)

        self.input_edit.clear()
        self.input_edit.insertPlainText(", ".join(names))
        self.pick_button.setEnabled(bool(names))
        self.clear_button.setEnabled(True)
        self.input_edit.setVisible(False)
        self.friends_picked += 1
        self.setWindowTitle(f"Christmas Friend Picker ({self.friends_picked} friends picked)")

    def clear(self):
        self.input_edit.clear()
        self.selected_friend_label.clear()
        self.pick_button.setEnabled(False)
        self.clear_button.setEnabled(False)

    def input_changed(self):
        self.pick_button.setEnabled(bool(self.input_edit.toPlainText().strip()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = PickerWidget()
    window.show()
    sys.exit(app.exec_())
