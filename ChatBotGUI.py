from pyexpat.errors import messages
from speechFunct import analyzeResponse
from basicImportInfo import *
#from openai import api_key, ChatCompletion
import openai 

openai.api_key = "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"
modelEngine = "gpt-3.5-turbo"

CHATHISTORY = [{"role": "system", 
                "content": 
                "You are a Personal Fitness Trainer assisting your client by heliping them \
                based on your previous conversation, or by answering any general questions"}]

class ChatBotWindow(QWidget):
    global modelEngine

    switchToMenuWindow = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('ChatBot')
        self.setStyleSheet("background-color: gray")

        layout = QGridLayout()

        self.title = QLabel("Personal Trainer ChatBot")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
        QLabel {
            text-align: center;
            font-size: 45px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 1100px;
            
            border: 3px solid;
            border-radius: 25%;

            margin-top: 1px;
            
            background-color: lightgray;
        }
        
        """)

        self.userMessageHistory1 = ScrollableLabel(self)
        self.userMessageHistory1.setText("_____")
        self.userMessageHistory1.setAlignment(Qt.AlignCenter)
        self.userMessageHistory1.setStyleSheet("""
        QLabel {
            text-align: center;
            font-size: 20px;
            font: bold italic "Times New Roman";
            
            min-height: 150px;
            min-width: 300px;
            max-width: 300px;

            border: 3px solid;
            border-radius: 15%;

            padding: 10px 5px;
            background-color: lightgray;
        }
        """)
        #    #min-width: 1100px;

        self.userMessageHistory2 = ScrollableLabel(self)
        self.userMessageHistory2.setText("_____")
        self.userMessageHistory2.setAlignment(Qt.AlignCenter)
        self.userMessageHistory2.setStyleSheet("""
        QLabel {
            text-align: center;
            font-size: 20px;
            font: bold italic "Times New Roman";
            
            min-height: 150px;
            min-width: 300px;
            max-width: 300px;
            
            border: 3px solid;
            border-radius: 15%;

            padding: 3%;
            background-color: lightgray;
        }
        """)
        
        
        self.userMessageHistory3 = ScrollableLabel(self)
        self.userMessageHistory3.setText("_____")
        self.userMessageHistory3.setAlignment(Qt.AlignCenter)
        self.userMessageHistory3.setStyleSheet("""
        QLabel {
            text-align: center;
            font-size: 20px;
            font: bold italic "Times New Roman";
            
            min-height: 150px;
            min-width: 300px;
            max-width: 300px;
            
            border: 3px solid;
            border-radius: 15%;

            padding: 3%;
            background-color: lightgray;
        }
        """)

        self.chatBotMessageHistory1 = ScrollableLabel(self)  #QLabel("_____")
        self.chatBotMessageHistory1.setText("_____")
        self.chatBotMessageHistory1.setAlignment(Qt.AlignCenter)
        self.chatBotMessageHistory1.setStyleSheet("""
        QLabel {
            background-color: lightgray;
            text-align: center;
            font-size: 20px;
            font: bold italic "Times New Roman";
            
            min-height: 150px;
            min-width: 300px;
            max-width: 300px;
            
            border: 3px solid;
            border-radius: 15%;

        }
        """)

        self.chatBotMessageHistory2 = ScrollableLabel(self)
        self.chatBotMessageHistory2.setText("_____")
        self.chatBotMessageHistory2.setAlignment(Qt.AlignCenter)
        self.chatBotMessageHistory2.setStyleSheet("""
        QLabel {
            text-align: center;
            font-size: 20px;
            font: bold italic "Times New Roman";
            
            min-height: 150px;
            min-width: 300px;
            max-width: 300px;
            
            border: 3px solid;
            border-radius: 15%;

            padding: 10px 5px;
            background-color: lightgray;
        }
        """)

        self.chatBotMessageHistory3 = ScrollableLabel(self)
        self.chatBotMessageHistory3.setText("_____")
        self.chatBotMessageHistory3.setAlignment(Qt.AlignCenter)
        self.chatBotMessageHistory3.setStyleSheet("""
        QLabel {
            text-align: center;
            font-size: 20px;
            font: bold italic "Times New Roman";

            min-height: 150px;
            min-width: 300px;
            max-width: 300px;
            
            border: 3px solid;
            border-radius: 15%;

            padding: 10px 5px;
            background-color: lightgray;
        }
        """)

        self.userInput = QLineEdit()
        self.userInput.returnPressed.connect(self.goToAskChatBot)
        self.userInput.setStyleSheet("""
        QLineEdit {
            font-size: 30px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 800px;
            max-width: 800px;
            
            border: 3px solid;
            border-radius: 25%;
            
            background-color: lightgray;
        }
        QLineEdit:hover {
            background-color: white;
        }
        """)

        self.backButton = QPushButton('Back To Menu')
        self.backButton.clicked.connect(self.goToMenuWindow)
        self.backButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 250px;
            max-width: 250px;

            border: 1px solid;
            border-radius: 8%;
         
            background-color: lightgray;
        }
        QPushButton:hover {
            font-size: 25px;
            font: bold italic "Times New Roman";

            background-color: white;
        }
        """)

        self.enterButton = QPushButton('Enter')
        self.enterButton.clicked.connect(self.goToAskChatBot)
        self.enterButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 250px;
            max-width: 250px;

            border: 1px solid;
            border-radius: 8%;
         
            background-color: lightgray;
        }
        QPushButton:hover {
            font-size: 25px;
            font: bold italic "Times New Roman";

            background-color: white;
        }
        """)

        self.borderLeft = QLabel("")
        #self.borderLeft.setAlignment(Qt.AlignCenter)
        #self.borderLeft.setStyleSheet("""
        #QLabel {
        #    text-align: center;
        #    font-size: 20px;
        #    font: bold italic "Times New Roman";
            
        #    min-width: 250px;
        #    max-width: 250px;
            
        #    border: 3px solid;
        #    border-radius: 15%;

        #    padding: 3%;
        #    background-color: lightgray;
        #}
        #""")

            
            
        self.borderRight = QLabel("")
        #self.borderRight.setAlignment(Qt.AlignCenter)
        #self.borderRight.setStyleSheet("""
        #QLabel {
        #    text-align: center;
        #    font-size: 20px;
        #    font: bold italic "Times New Roman";
            
        #    min-width: 250px;
        #    max-width: 250px;
            
        #    border: 3px solid;
        #    border-radius: 15%;

        #    padding: 3%;
        #    background-color: lightgray;
        #}
        #""")

        self.addToLayout = [(self.borderLeft, 1, 0, 3, 1), (self.title, 0, 0, 1, 4), (self.borderRight, 1, 3, 3, 1), 
                            (self.userMessageHistory3, 1, 1, 1, 1), (self.chatBotMessageHistory3, 1, 2, 1, 1),
                            (self.userMessageHistory2, 2, 1, 1, 1), (self.chatBotMessageHistory2, 2, 2, 1, 1),
                            (self.userMessageHistory1, 3, 1, 1, 1), (self.chatBotMessageHistory1, 3, 2, 1, 1),
                            (self.backButton, 4, 0, 1, 1), (self.userInput, 4, 1, 1, 2), (self.enterButton, 4, 3, 1, 1)]

        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
        


        self.setLayout(layout)
    
    def goToMenuWindow(self):
        self.switchToMenuWindow.emit()

    def goToAskChatBot(self):
        try: 
            mess = self.chatGPTAPI(self.userInput.text())
            
            self.userMessageHistory3.setText(self.userMessageHistory2.text())
            self.userMessageHistory2.setText(self.userMessageHistory1.text())
        
            self.chatBotMessageHistory3.setText(self.chatBotMessageHistory2.text())
            self.chatBotMessageHistory2.setText(self.chatBotMessageHistory1.text())
        
            self.userMessageHistory1.setText(self.userInput.text())
            self.chatBotMessageHistory1.setText(mess)

        except openai.error.RateLimitError:
            print("Crashed")
        finally:
            self.userInput.clear()

    def chatGPTAPI(self, userInput):
        global CHATHISTORY
        
        CHATHISTORY.append({"role": "user", "content": userInput}) 

        response = openai.ChatCompletion.create(
            model=modelEngine,
            messages=CHATHISTORY,
            temperature=1)
        
        message = response.choices[0]['message']
        print('\n', len(message["content"]),
              '\n', message["content"])

        role, mess = message["role"], message["content"]
        CHATHISTORY.append({"role": role, "content": mess}) 

        return mess

# class for scrollable label
class ScrollableLabel(QScrollArea):
 
    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
 
        # making widget resizable
        self.setWidgetResizable(True)
 
        # making qwidget object
        textToDisplay = QWidget(self)
        self.setWidget(textToDisplay)
 
        # vertical box layout
        layout = QVBoxLayout(textToDisplay)
 
        self.label = QLabel(textToDisplay)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
        QLabel {
            font-size: 20px;
            font: bold italic "Times New Roman";
            
            min-height: 150px;
            min-width: 300px;
            max-width: 300px;
            
            border: 3px solid;
            border-radius: 15%;

            padding: 3%;
            background-color: lightgray;
        }
        """)
 
        layout.addWidget(self.label)

 
    # the setText method
    def setText(self, text):
        # setting text to the label
        #padding = (" " * 300) + "."S
        #print(text + padding)
        self.label.setText(text)

    def text(self):
        # getting text to the label
        return self.label.text()

    def setStyleSheet(self, str):
        self.label.setStyleSheet(str)
