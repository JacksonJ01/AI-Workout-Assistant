from basicImportInfo import *


class LoginWindow(QWidget):
    # The pyqtSignal declarations in each class allow for specified windows to be opened
    switchToSignInWindow, switchToSignUpWindow = pyqtSignal(), pyqtSignal(list)

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Login Window')
        self.setStyleSheet("background-color: gray")

        layout = QGridLayout()

        self.title = QLabel("AI Workout Assistant")
        #self.title.setFixedWidth(500)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
        QLabel {
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
        #min-width: 400px;
        #max-width: 600px;
        
        
        self.signUpButton = QPushButton('Sign Up')
        self.signUpButton.clicked.connect(self.goToSignUpWindow)
        self.signUpButton.setStyleSheet("""
        QPushButton {
            font-size: 30px;
            font-family: "Times New Roman";

            min-height: 75px;
            max-height: 100px;
            min-width: 500px;
            max-width: 500px;

            border: 1px solid;
            border-radius: 50%;
            background-color: lightgray;

            margin-left: 0;
        }
        QPushButton:hover {
            background-color: white;
            font-size: 40px;
            font: bold italic "Times New Roman";

            border: 3px solid;
        }
        """)
        self.signUpButton.enterEvent = self.changeSignUpWidth
        self.signUpButton.leaveEvent = self.changeSignUpWidthBack
    
        self.signInButton = QPushButton('Sign In')
        self.signInButton.clicked.connect(self.goToSignInWindow)
        self.signInButton.setStyleSheet("""
        QPushButton {
            font-size: 30px;
            font-family: "Times New Roman";

            min-height: 75px;
            max-height: 100px;
            min-width: 500px;
            max-width: 500px;

            border: 1px solid;
            border-radius: 50%;
            background-color: lightgray;

            margin-right: 0;
        }
        QPushButton:hover {
            background-color: white;
            font-size: 40px;
            font: bold italic "Times New Roman";

            border: 3px solid;
        }
        """)
        self.signInButton.enterEvent = self.changeSignInWidth
        self.signInButton.leaveEvent = self.changeSignInWidthBack

        self.exitButton = QPushButton('Exit Program')
        self.exitButton.clicked.connect(self.goToExit)
        self.exitButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 30px;
            min-width: 1000px;

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
         

        self.bufferZone1 = QLabel()
        self.bufferZone1.setAlignment(Qt.AlignCenter)
        self.bufferZone1.setStyleSheet("""
        QLabel {
            min-height: 50px;
            max-height: 75px;
            min-width: 700px;
        }
        
        """)

        self.bufferZone2 = QLabel()
        self.bufferZone2.setAlignment(Qt.AlignCenter)
        self.bufferZone2.setStyleSheet("""
        QLabel {
            min-height: 50px;
            max-height: 75px;
            min-width: 700px;
        }
        
        """)
            
            
            #margin-top: 1px;
            
            #background-color: lightgray;

        # List variable that hold all of the widegts that need to be added into the current window then adds them
        self.addToLayout = [(self.title, 0, 0, 1, 2),
                            (self.bufferZone1, 1, 0, 1, 2),
                            (self.signUpButton, 2, 0, 1, 1), (self.signInButton, 2, 1, 1, 1), 
                            (self.bufferZone2, 3, 0, 1, 2),
                            (self.exitButton, 4, 0, 1, 2)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)

    def changeSignInWidth(self, event):
        #print("Event Start:", event)
        self.signInWidthAnimation = QPropertyAnimation(self.signInButton, b"minimumWidth")
        self.signInWidthAnimation.setDuration(100)
        self.signInWidthAnimation.setStartValue(500) #Initial width
        self.signInWidthAnimation.setEndValue(600) #Final width
        
        #self.signUpWidthAnimation = QPropertyAnimation(self.signUpButton, b"maximumWidth")
        #self.signUpWidthAnimation.setDuration(50)
        #self.signUpWidthAnimation.setStartValue(500) #Initial width
        #self.signUpWidthAnimation.setEndValue(400) #Final width
        
        #self.signUpWidthAnimation.start()
        self.signInWidthAnimation.start()

    
    def changeSignInWidthBack(self, event=None):
        #print("Event End:", event, type(event))
        self.signInWidthAnimation = QPropertyAnimation(self.signInButton, b"minimumWidth")
        self.signInWidthAnimation.setDuration(25)
        self.signInWidthAnimation.setStartValue(600) #Initial width
        self.signInWidthAnimation.setEndValue(500) #Final width
        
        #self.signUpWidthAnimation = QPropertyAnimation(self.signUpButton, b"maximumWidth")
        #self.signUpWidthAnimation.setDuration(50)
        #self.signUpWidthAnimation.setStartValue(400) #Initial width
        #self.signUpWidthAnimation.setEndValue(500) #Final width
        
        #self.signUpWidthAnimation.start()
        self.signInWidthAnimation.start()

    def changeSignUpWidth(self, event):
        #print("Event Start:", event)
        self.widthAnimation = QPropertyAnimation(self.signUpButton, b"minimumWidth")
        self.widthAnimation.setDuration(100)
        self.widthAnimation.setStartValue(500) #Initial width
        self.widthAnimation.setEndValue(600) #Final width
        self.widthAnimation.start()
    
    def changeSignUpWidthBack(self, event):
        #print("Event End:", event)
        self.widthAnimation = QPropertyAnimation(self.signUpButton, b"minimumWidth")
        self.widthAnimation.setDuration(25)
        self.widthAnimation.setStartValue(600) #Initial width
        self.widthAnimation.setEndValue(500) #Final width
        self.widthAnimation.start()
        

    def goToSignInWindow(self):
        self.switchToSignInWindow.emit()

    def goToSignUpWindow(self):
        self.switchToSignUpWindow.emit([])

    def goToExit(self):
        exit("Thank You! \nDo Come Again")


class SignInWindow(QWidget):
    switchToMenuWindow, switchToLoginWindow = pyqtSignal(str), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Sign In Window')
        self.setStyleSheet("background-color: gray")

        layout = QGridLayout()

        self.title = QLabel("Sign In")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
        QLabel {
            font-size: 45px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 1000px;
            
            border: 3px solid;
            border-radius: 25%;

            margin-top: 1px;
            
            background-color: lightgray;
        }
        
        """)

        self.userNameLabel = QLabel("Username")
        self.userNameLabel.setAlignment(Qt.AlignCenter)
        self.userNameLabel.setStyleSheet("""
        QLabel {
            font-size: 30px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            max-width: 400px;

            border: 3px solid;
            border-radius: 25%;

            background-color: lightgray;
        }
        """)
        self.userNameInput = QLineEdit()
        self.userNameInput.setStyleSheet("""
        QLineEdit {
            font-size: 30px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            
            border: 3px solid;
            border-radius: 25%;
            
            background-color: lightgray;
        }
        QLineEdit:hover {
            background-color: white;
        }
        """)

        self.passwordLabel = QLabel("Password")
        self.passwordLabel.setAlignment(Qt.AlignCenter)
        self.passwordLabel.setStyleSheet("""
        QLabel {
            font-size: 30px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            max-width: 400px;

            border: 3px solid;
            border-radius: 25%;

            background-color: lightgray;
        }
        """)

        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setStyleSheet("""
        QLineEdit {
            font-size: 30px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            
            border: 3px solid;
            border-radius: 25%;
            
            background-color: lightgray;
        }
        QLineEdit:hover {
            background-color: white;
        }
        """)

        self.backButton = QPushButton('Back To Login Page')
        self.backButton.clicked.connect(self.goToLoginWindow)
        self.backButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 400px;
            max-width: 400px;

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

        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.goToMenuWindow)
        self.submitButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 400px;

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

        self.bufferZone1 = QLabel()
        self.bufferZone1.setStyleSheet("""
        QLabel {
            min-height: 50px;
            max-height: 75px;
            min-width: 700px;
        }
        """)

        self.bufferZone2 = QLabel()
        self.bufferZone2.setAlignment(Qt.AlignCenter)
        self.bufferZone2.setStyleSheet("""
        QLabel {
            min-height: 50px;
            max-height: 75px;
            min-width: 700px;
        }
        """)

        self.addToLayout = [(self.title, 0, 0, 1, 2),
                            (self.bufferZone1, 1, 0, 1, 2),
                            (self.userNameLabel, 2, 0, 1, 1), (self.userNameInput, 2, 1, 1, 1), 
                            (self.passwordLabel, 3, 0, 1, 1), (self.passwordInput, 3, 1, 1, 1), 
                            (self.bufferZone2, 4, 0, 1, 2),
                            (self.backButton, 5, 0, 1, 1), (self.submitButton, 5, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])        
        self.setLayout(layout)

    def goToMenuWindow(self):
        uName = self.userNameInput.text()
        passW = self.passwordInput.text()

        uPassW: list = selectFromTable(conn, dataBases[0][1], columns=["password"], fromWhere={"userName": uName})

        uPassW = uPassW[0][0]
        print(passW, uPassW)

        if uPassW is False:
            self.userNameLabel.setText("UserName Not Found")
            self.userNameLabel.setStyleSheet("""
            QLabel {
                font-size: 30px;
                font: bold italic "Times New Roman";
                text-align: center;

                min-height: 50px;
                max-height: 75px;
                min-width: 400px;
                max-width: 400px;

                border: 3px solid;
                border-radius: 25%;

                background-color: white;
            }
            """)
            return
        else:
            self.userNameLabel.setText("UserName*")
            self.userNameLabel.setStyleSheet("""
            QLabel {
                font-size: 30px;
                font: bold italic "Times New Roman";
                text-align: center;

                min-height: 50px;
                max-height: 75px;
                min-width: 400px;
                max-width: 400px;

                border: 3px solid;
                border-radius: 25%;

                background-color: lightgray;
            }
            """)
            if passW == uPassW:
                dataBaseUsernames = []
                self.passwordLabel.setText("Password*")
                self.switchToMenuWindow.emit(uName)
            else:
                dataBaseUsernames = []
                self.passwordLabel.setText("Incorrect Password")
                self.passwordLabel.setStyleSheet("""
                QLabel {
                    font-size: 30px;
                    font: bold italic "Times New Roman";
                    text-align: center;

                    min-height: 50px;
                    max-height: 75px;
                    min-width: 400px;
                    max-width: 400px;

                    border: 3px solid;
                    border-radius: 25%;

                    background-color: white;
                }
                """)
                return

    def goToLoginWindow(self):
        self.switchToLoginWindow.emit()

class SignUpWindow(QWidget):
    switchToAccountCreationWindow, switchToLoginWindow = pyqtSignal(list), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Sign Up Window')
        self.setStyleSheet("background-color: gray")



        layout = QGridLayout()             
        
        self.title = QLabel("Sign Up")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
        QLabel {
            font-size: 45px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 1000px;
            
            border: 3px solid;
            border-radius: 25%;

            margin-top: 1px;
            
            background-color: lightgray;
        }
        
        """)


        self.firstNameLabel = QLabel("First Name*")
        self.firstNameLabel.setAlignment(Qt.AlignCenter)
        self.firstNameLabel.setStyleSheet("""
        QLabel {
            font-size: 30px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            max-width: 400px;

            border: 3px solid;
            border-radius: 25%;

            background-color: lightgray;
        }
        """)

        self.firstNameInput = QLineEdit()
        self.firstNameInput.setStyleSheet("""
        QLineEdit {
            font-size: 30px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            
            border: 3px solid;
            border-radius: 25%;
            
            background-color: lightgray;
        }
        QLineEdit:hover {
            background-color: white;
        }
        """)


        self.lastNameLabel = QLabel("Last Name*")
        self.lastNameLabel.setAlignment(Qt.AlignCenter)
        self.lastNameLabel.setStyleSheet("""
        QLabel {
            font-size: 30px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            max-width: 400px;

            border: 3px solid;
            border-radius: 25%;

            background-color: lightgray;
        }
        """)

        self.lastNameInput = QLineEdit()
        self.lastNameInput.setStyleSheet("""
        QLineEdit {
            font-size: 30px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            
            border: 3px solid;
            border-radius: 25%;
            
            background-color: lightgray;
        }
        QLineEdit:hover {
            background-color: white;
        }
        """)

        self.backButton = QPushButton('Back To Login Page')
        self.backButton.clicked.connect(self.goToLoginWindow)
        self.backButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 400px;
            max-width: 400px;

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

        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.goToAccountCreationWindow)      
        self.submitButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 400px;

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

        self.bufferZone1 = QLabel()
        self.bufferZone1.setStyleSheet("""
        QLabel {
            min-height: 50px;
            max-height: 75px;
            min-width: 700px;
        }
        """)

        self.bufferZone2 = QLabel()
        self.bufferZone2.setAlignment(Qt.AlignCenter)
        self.bufferZone2.setStyleSheet("""
        QLabel {
            min-height: 50px;
            max-height: 75px;
            min-width: 700px;
        }
        """)

        
        self.addToLayout = [(self.title, 0, 0, 1, 2), 
                            (self.bufferZone1, 1, 0, 1, 2),
                            (self.firstNameLabel, 2, 0, 1, 1), (self.firstNameInput, 2, 1, 1, 1), 
                            (self.lastNameLabel, 3, 0, 1, 1), (self.lastNameInput, 3, 1, 1, 1), 
                            (self.bufferZone2, 4, 0, 1, 2),
                            (self.backButton, 5, 0, 1, 1), (self.submitButton, 5, 1, 1, 1)]

        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    
    def goToAccountCreationWindow(self):
        fName = self.firstNameInput.text()
        lName = self.lastNameInput.text()
        print(fName, lName)
        if fName != "" and lName != "":
            print(fName, lName)
            self.switchToAccountCreationWindow.emit([fName, lName])

    def goToLoginWindow(self):
        self.switchToLoginWindow.emit()


class AccountCreationWindow(QWidget):
    switchToMenuWindow, switchToSignUpWindow = pyqtSignal(str), pyqtSignal()

    def __init__(self, genUserInfo):
        QWidget.__init__(self)
        self.setWindowTitle('Account Creation Window')
        self.setStyleSheet("background-color: gray")

        layout = QGridLayout()             

        self.genUserInfo = genUserInfo
        #print(self.genUserInfo)

        self.title = QLabel("Account Creation")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
        QLabel {
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
        self.userNameLabel = QLabel("Enter A Username*")
        self.userNameLabel.setAlignment(Qt.AlignCenter)
        self.userNameLabel.setStyleSheet("""
        QLabel {
            font-size: 30px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            max-width: 400px;

            border: 3px solid;
            border-radius: 25%;

            background-color: lightgray;
        }
        """)

        self.userNameInput = QLineEdit()
        self.userNameInput.setStyleSheet("""
        QLineEdit {
            font-size: 30px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            
            border: 3px solid;
            border-radius: 25%;
            
            background-color: lightgray;
        }
        QLineEdit:hover {
            background-color: white;
        }
        """)
        
        self.passwordLabel = QLabel("Enter A Password*")
        self.passwordLabel.setAlignment(Qt.AlignCenter)
        self.passwordLabel.setStyleSheet("""
        QLabel {
            font-size: 30px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            max-width: 400px;

            border: 3px solid;
            border-radius: 25%;

            background-color: lightgray;
        }
        """)

        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setStyleSheet("""
        QLineEdit {
            font-size: 30px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            
            border: 3px solid;
            border-radius: 25%;
            
            background-color: lightgray;
        }
        QLineEdit:hover {
            background-color: white;
        }
        """)

        self.reEnterpasswordLabel = QLabel("Re-Enter Password*")
        self.reEnterpasswordLabel.setAlignment(Qt.AlignCenter)
        self.reEnterpasswordLabel.setStyleSheet("""
        QLabel {
            font-size: 30px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            max-width: 400px;

            border: 3px solid;
            border-radius: 25%;

            background-color: lightgray;
        }
        """)

        self.reEnterPasswordInput = QLineEdit()
        self.reEnterPasswordInput.setEchoMode(QLineEdit.Password)
        self.reEnterPasswordInput.setStyleSheet("""
        QLineEdit {
            font-size: 30px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            
            border: 3px solid;
            border-radius: 25%;
            
            background-color: lightgray;
        }
        QLineEdit:hover {
            background-color: white;
        }
        """)

        self.backButton = QPushButton('Back To Sign Up')
        self.backButton.clicked.connect(self.goToSignUpWindow)
        self.backButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 400px;
            max-width: 400px;

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

        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.goToMenuWindow)
        self.submitButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 400px;

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

        self.bufferZone1 = QLabel()
        self.bufferZone1.setStyleSheet("""
        QLabel {
            min-height: 50px;
            max-height: 75px;
            min-width: 700px;
        }
        """)

        self.bufferZone2 = QLabel()
        self.bufferZone2.setAlignment(Qt.AlignCenter)
        self.bufferZone2.setStyleSheet("""
        QLabel {
            min-height: 50px;
            max-height: 75px;
            min-width: 700px;
        }
        """)
        

        self.addToLayout = [(self.title, 0, 0, 1, 2), 
                            (self.bufferZone1, 1, 0, 1, 2),
                            (self.userNameLabel, 2, 0, 1, 1), (self.userNameInput, 2, 1, 1, 1), 
                            (self.passwordLabel, 3, 0, 1, 1), (self.passwordInput, 3, 1, 1, 1), 
                            (self.reEnterpasswordLabel, 4, 0, 1, 1), (self.reEnterPasswordInput, 4, 1, 1, 1),
                            (self.bufferZone2, 5, 0, 1, 2),
                            (self.backButton, 6, 0, 1, 1), (self.submitButton, 6, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    
    def goToMenuWindow(self):
        # The credentials that the User enters will be checked in this method
        # To do they will have to enter a username and password that has not been entered into the database
        uName = self.userNameInput.text()
        passW = self.passwordInput.text()
        rePassW = self.reEnterPasswordInput.text()

        #print(passW, rePassW, passW != rePassW)
        if passW != rePassW:
            self.reEnterpasswordLabel.setText("Passwords Do Not Match")
            self.reEnterpasswordLabel.setStyleSheet("""
            QLabel {
            font-size: 30px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            max-width: 400px;

            border: 3px solid;
            border-radius: 25%;

            background-color: white;
        }
        """)
            return
        else:
            self.reEnterpasswordLabel.setText("Re-Enter Password*")
            self.reEnterpasswordLabel.setStyleSheet("""
            QLabel {
            font-size: 30px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 50px;
            max-height: 75px;
            min-width: 400px;
            max-width: 400px;

            border: 3px solid;
            border-radius: 25%;

            background-color: lightgray;
        }
        """)

        global conn
        #print(conn)

        dataBaseUsernames: list = selectFromTable(conn, "PersonTable", columns=["userName"])
        #print(uName, dataBaseUsernames)
        taken = False
        for user in dataBaseUsernames:
            print(uName, user[0], taken)
            if uName == user[0]:
                taken = True
                print(uName, user[0], taken)
                break

        if taken is False:
            self.userNameLabel.setText("Username*")
            self.userNameLabel.setStyleSheet("""
            QLabel {
                font-size: 30px;
                font: bold italic "Times New Roman";
                text-align: center;

                min-height: 50px;
                max-height: 75px;
                min-width: 400px;
                max-width: 400px;

                border: 3px solid;
                border-radius: 25%;

                background-color: lightgray;
            }
            """)

            userData = {
                "userName": uName,
                "password": passW,
                "firstName": self.genUserInfo[0],
                "lastName": self.genUserInfo[1],
            }
            
            data = addIntoTable(conn, "PersonTable", userData)
            #print(data)
            self.switchToMenuWindow.emit(uName)
                
        else:
            dataBaseUsernames = []
            self.userNameLabel.setText("Username Taken")
            self.userNameLabel.setStyleSheet("""
            QLabel {
                font-size: 30px;
                font: bold italic "Times New Roman";
                text-align: center;

                min-height: 50px;
                max-height: 75px;
                min-width: 400px;
                max-width: 400px;

                border: 3px solid;
                border-radius: 25%;

                background-color: white;
            }
            """)
            return

    def goToSignUpWindow(self):
        self.switchToSignUpWindow.emit()