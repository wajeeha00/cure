from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog,
    QVBoxLayout, QLineEdit, QComboBox, QPushButton, QToolBar, QStatusBar,
    QMessageBox, QLabel, QGridLayout,QTextEdit
)
import sys
from threading import Thread
from backend import ChatBot
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Chatbot = ChatBot()
        self.setWindowTitle("Chatbot")
        self.setMinimumSize(700,500)
 
        self.chat_area = QTextEdit(self)
        #left,top,width,height
        self.chat_area.setGeometry(10,10,480,320)
        self.input_field = QLineEdit(self)
        self.chat_area.setReadOnly(True)
        self.input_field.returnPressed.connect(self.send_message)
 
 
        self.input_field.setGeometry(10,340,480,30)
        self.button = QPushButton("Send", self)
 
        self.button.setGeometry(500,340,80,30)
        self.button.clicked.connect(self.send_message)
        self.show()
 
    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'> Me: {user_input}</p>")
        thread = Thread(target=self.get_bot_response,args=(user_input,))
        thread.start()
    def get_bot_response(self,user_input):
        response = self.Chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color:#e9e9e9'>Bot: {response}</p>")
        self.input_field.clear()
 
 
app = QApplication(sys.argv)
window = ChatbotWindow()
sys.exit(app.exec())