#from dataBase import database
from basicImportInfo import *
from A_Sign_InOrUpGUI import LoginWindow, SignInWindow, SignUpWindow, AccountCreationWindow
from MainMenuGUI import MainMenuWindow
from LiveWorkoutGUI import WorkoutWindow
from ChatBotGUI import ChatBotWindow


class DatabaseWindow(QWidget):
    switchToPersonDatabseWindow, switchToExerciseDatabaseWindow, switchToMenuWindow = pyqtSignal(), pyqtSignal(), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.CONTEXT = None

        self.setWindowTitle('Database Configuration')

        layout = QGridLayout()

        self.personDatabaseConfig = QPushButton("Person Database Configuration")
        self.personDatabaseConfig.clicked.connect(self.goToPersonDatabaseWindow)
        self.exerciseDatabaseConfig = QPushButton("Exercise Database Configuation")
        self.exerciseDatabaseConfig.clicked.connect(self.goToExerciseDatabaseWindow)

        self.backButton = QPushButton('Back To Menu')
        self.backButton.clicked.connect(self.goToMenuWindow)

        self.addToLayout = [(self.personDatabaseConfig, 0, 0, 1, 1),
                            (self.exerciseDatabaseConfig, 1, 0, 1, 1),
                            (self.backButton, 2, 0, 1, 1)]

        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
        
        self.setLayout(layout)
    
    def goToMenuWindow(self):
        self.switchToMenuWindow.emit()

    def goToPersonDatabaseWindow(self):
        self.switchToPersonDatabseWindow.emit()

    def goToExerciseDatabaseWindow(self):
        self.switchToExerciseDatabaseWindow.emit()

        
class Controller:

    def __init__(self):
        self.workOut = None
        pass
    
    def showLogin(self):
        try:
           self.signIn.close()
        except:
            pass
        try:
           self.signUp.close()
        except:
            pass

        self.login = LoginWindow()
        self.login.switchToSignInWindow.connect(self.showSignIn)
        self.login.switchToSignUpWindow.connect(self.showSignUp)
        
        self.login.showMaximized()

    def showSignIn(self):
        try:
           self.login.close()
        except:
            pass

        self.signIn = SignInWindow()
        self.signIn.switchToMenuWindow.connect(self.showMainMenu)
        self.signIn.switchToLoginWindow.connect(self.showLogin)
        
        self.signIn.showMaximized()


    def showSignUp(self):
        try:
           self.login.close()
        except:
            pass
        try:
           self.accountCreation.close()
        except:
            pass

        self.signUp = SignUpWindow()
        self.signUp.switchToAccountCreationWindow.connect(self.showAccCrea)
        self.signUp.switchToLoginWindow.connect(self.showLogin)
        
        self.signUp.showMaximized()

    def showAccCrea(self, genUserInfo):
        try:
           self.signUp.close()
        except:
            pass

        self.accountCreation = AccountCreationWindow(genUserInfo)
        self.accountCreation.switchToMenuWindow.connect(self.showMainMenu)
        self.accountCreation.switchToSignUpWindow.connect(self.showSignUp)
        
        self.accountCreation.showMaximized()


    def showMainMenu(self, genUserInfo):
        
        # This doesn't work??
        #windowsToClose = [self.signIn, self.signUp, self.chatBot, self.workOut]

        #for window in windowsToClose:
        #    try:
        #        window.close()
        #    except AttributeError:
        #        pass

        try:
           self.signIn.close()
        except:
            pass
        try:
           self.accountCreation.close()
        except:
            pass
        #try:
        #    self.database.close()
        #except:
        #    pass
        try:
           self.chatBot.close()
        except:
            pass
        try:
           self.workOut.close()
        except:
            pass
        
        self.mainMenuWindow = MainMenuWindow(genUserInfo)
        #self.mainMenuWindow.switchToDatabaseWindow.connect(self.showDatabaseWindow)
        self.mainMenuWindow.switchToChatBotWindow.connect(self.showChatBot)
        self.mainMenuWindow.switchToWorkoutWindow.connect(self.showWorkout)
        
        self.mainMenuWindow.showMaximized()


    #################################################
    def showChatBot(self, genUserInfo):
        try:
            self.mainMenuWindow.close()
        except AttributeError:
            pass

        self.chatBot = ChatBotWindow(genUserInfo)
        self.chatBot.switchToMenuWindow.connect(self.showMainMenu)
        self.chatBot.showMaximized()

    def showWorkout(self, genUserInfo):
        try:
            self.mainMenuWindow.close()
        except AttributeError:
            pass

        #print(self.workOut)
        if self.workOut is None:
            self.workOut = WorkoutWindow(genUserInfo)
            self.workOut.switchToMenuWindow.connect(self.showMainMenu)
            self.workOut.showMaximized()
        else:
            self.workOut.switchToMenuWindow.disconnect()
            self.workOut.switchToMenuWindow.connect(self.showMainMenu)
        
        self.workOut.showMaximized()

def main():
    app = QApplication(argv)
    controller = Controller()
  
    #controller.showLogin()
    #controller.showSignIn()
    #controller.showSignUp()
    #controller.showAccountCreation([])
    #controller.showMainMenu("JJ01")
    controller.showWorkout("JJ01")
    #controller.showChatBot("")

    #controller.showDatabaseWindow()
    #controller.showExerciseDatabaseWindow()
    #controller.showExerciseTableConfigurationWindow()
    #controller.showWorkoutDataTableConfigurationWindow()
    Exit(app.exec_())