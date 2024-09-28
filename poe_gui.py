import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QTextBrowser, QComboBox, QLabel, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from loadPOE import PoeApi, AVAILABLE_BOTS, send_message_with_attachments
import markdown2

class PoeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.client = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('POE API GUI')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Connect button
        self.connect_button = QPushButton('Connect to Server')
        self.connect_button.clicked.connect(self.connect_to_server)
        layout.addWidget(self.connect_button)

        # Bot selection dropdown
        self.bot_dropdown = QComboBox()
        self.bot_dropdown.addItems(list(AVAILABLE_BOTS.values()))
        self.bot_dropdown.setEnabled(False)
        layout.addWidget(self.bot_dropdown)

        # Input and output panels
        input_output_layout = QHBoxLayout()

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter your message here...")
        input_output_layout.addWidget(self.input_text)

        self.output_text = QTextBrowser()
        self.output_text.setOpenExternalLinks(True)
        self.output_text.setFont(QFont("Courier", 10))
        input_output_layout.addWidget(self.output_text)

        layout.addLayout(input_output_layout)

        # Buttons
        button_layout = QHBoxLayout()

        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setEnabled(False)
        button_layout.addWidget(self.send_button)

        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(self.clear_text)
        button_layout.addWidget(self.clear_button)

        self.upload_button = QPushButton('Upload File')
        self.upload_button.clicked.connect(self.upload_file)
        self.upload_button.setEnabled(False)
        button_layout.addWidget(self.upload_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def connect_to_server(self):
        try:
            tokens = {
                'p-b': 'tf0Ffurpw5AQ7J-_ZmhY3g%3D%3D',
                'p-lat': 'x6TCO2hlZ61i7C8SYrS1f3BnE1sssANglmrhAi0R7Q%3D%3D',
            }
            self.client = PoeApi(tokens=tokens)
            QMessageBox.information(self, "Connection Status", "Successfully connected to the server!")
            self.connect_button.setEnabled(False)
            self.bot_dropdown.setEnabled(True)
            self.send_button.setEnabled(True)
            self.upload_button.setEnabled(True)
        except Exception as e:
            QMessageBox.critical(self, "Connection Error", f"Failed to connect to the server: {str(e)}")

    def send_message(self):
        if not self.client:
            QMessageBox.warning(self, "Not Connected", "Please connect to the server first.")
            return

        message = self.input_text.toPlainText()
        bot = self.bot_dropdown.currentText()
        

        try:
            if self.file_path:
                for chunk in self.client.send_message(bot, message, file_path=[self.file_path]):
                    pass
            else:
                for chunk in self.client.send_message(bot, message):
                    pass
            response = chunk["text"]
            html_content = markdown2.markdown(response)
            self.output_text.setHtml(html_content)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to send message: {str(e)}")

    def clear_text(self):
        self.input_text.clear()
        self.output_text.clear()
        self.file_path = None

    def upload_file(self):
        if not self.client:
            QMessageBox.warning(self, "Not Connected", "Please connect to the server first.")
            return

        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        print(self.file_path)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PoeGUI()
    ex.show()
    sys.exit(app.exec_())