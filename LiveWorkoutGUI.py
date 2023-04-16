from speechFunct import analyzeResponse
from basicImportInfo import *

CurrentRepCount = None  
CurrentExercise = None
CurrentAngles = None
ShowTargetAngles = True
UserInfo = None
WorkoutEnded = None
trackedExercises = None
FinishWorkout = False

                                          
class WorkoutWindow(QWidget):
    switchToMenuWindow = pyqtSignal(str)
    
    def __init__(self, genUserInfo):
        global CurrentExercise
        global CurrentRepCount
        global CurrentAngles
        global UserInfo
        global WorkoutEnded

        UserInfo = genUserInfo
        print(UserInfo)

        QWidget.__init__(self)
        self.setWindowTitle('Workout Window')
        #self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.title = QLabel("Live Exercise View")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
        QLabel {
            font-size: 45px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 1080px;
            
            border: 3px solid;
            border-radius: 25%;

            margin-top: 1px;
            
            background-color: lightgray;
        }
        """)

        CurrentExercise = QLabel("Exercise: ____")
        CurrentExercise.setAlignment(Qt.AlignCenter)
        CurrentExercise.setStyleSheet("""
        QLabel {
            font-size: 25px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 30px;
            max-height: 50px;
            
            border: 3px solid;
            border-radius: 20%;

            background-color: lightgray;
            float:left;
        }
        """)
            #min-width: 400px;
            #max-width: 400px;
        
            #margin-top: 1px;
        CurrentRepCount = QLabel("Rep Count: ____")
        CurrentRepCount.setAlignment(Qt.AlignCenter)
        CurrentRepCount.setStyleSheet("""
        QLabel {
            font-size: 25px;
            font: bold italic "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 280px;
            
            border: 3px solid;
            border-radius: 20%;

            background-color: lightgray;
            text-align: center;
        }
        """)
        CurrentAngles = QLabel("Within Range: ____")
        CurrentAngles.setAlignment(Qt.AlignCenter)
        CurrentAngles.setStyleSheet("""
        QLabel {
            font-size: 25px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 30px;
            max-height: 50px;
            border: 3px solid;
            border-radius: 20%;

            background-color: lightgray;

            float: right;
        }
        """)
            #min-width: 400px;
            #max-width: 400px;
            
        
        self.videoLabel = QLabel(self)
        
        #try:
        #    if self.th.isRunning() is True:
        #        print("Here1", self.th.isRunning())

        #except AttributeError as e:
        #    print(e)
        #    self.th = Thread(self)
        #    self.th.start()
        #    print("Here2", self.th.isRunning())
        #    pass

        

        self.th = Thread(self)
        try:
            print("Here1")
            print(QThread.currentThread(), self.th, self.th.isRunning())
        
            self.th.changePixmap.connect(self.captureImage)
            self.th.start()
        except:
            print("Here2")
            self.th = Thread(self)
            self.th.changePixmap.connect(self.captureImage)
            self.th.start()


        WorkoutEnded = False
        self.videoLabel.setAlignment(Qt.AlignCenter)
        self.videoLabel.setStyleSheet("""
        QLabel {
            height: 480px;
            text-align: center; 
            border: 3px solid;
            background-color: lightgray;

            margin-top: 0px:
            margin-bottom: 0px:
            border-radius: 25%;
        }
        """)
            #margin-left: 200px;
            #margin-right: 200px;

        #self.videoLabel.setFixedWidth(720)
            #float: left;
            #min-width: 1080px;
            #max-width: 1080px;

        self.backButton = QPushButton('Back To Menu')
        self.backButton.clicked.connect(self.goToMenuWindow)
        self.backButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;

            border: 1px solid;
            border-radius: 15%;
         
            background-color: lightgray;
        }
        QPushButton:hover {
            font-size: 25px;
            font: bold italic "Times New Roman";

            background-color: white;
        }
        """)
            #has to match width for each cell
            #min-width: 300px;
            #max-width: 300px;

        self.finishWorkout = QPushButton("Finish Workout")
        self.finishWorkout.clicked.connect(self.goToFinishWorkout)
        self.finishWorkout.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;

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
            #min-width: 400px;
            #max-width: 400px;

        self.showingLines = QPushButton("Show Target Angles")
        self.showingLines.clicked.connect(self.goToShowLines)
        self.showingLines.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;

            border: 1px solid;
            border-radius: 15%;
         
            background-color: lightgray;
        }
        QPushButton:hover {
            font-size: 25px;
            font: bold italic "Times New Roman";

            background-color: white;
        }
        """)
            #min-width: 380px;
            #max-width: 380px;
        
        self.addToLayout = [(self.title, 0, 0, 1, 3), 
                            (CurrentRepCount, 1, 0, 1, 1), (CurrentExercise, 1, 1, 1, 1), (CurrentAngles, 1, 2, 1, 1), 
                            (self.videoLabel, 2, 0, 1, 3),
                            (self.backButton, 3, 0, 1, 1), (self.showingLines, 3, 1, 1, 1), (self.finishWorkout, 3, 2, 1, 1)]
        
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)

        self.setLayout(layout)
    
    def captureImage(self, image):
        self.videoLabel.setPixmap(QPixmap.fromImage(image))        

    def goToMenuWindow(self):

        self.switchToMenuWindow.emit(UserInfo)

    def goToFinishWorkout(self):
        print(trackedExercises)
        for exercise in trackedExercises:
            exerciseDataEntry = {
                "userName": UserInfo,
                "dateID": QDate().currentDate().toString("yyyy:MM:dd"),
                "exName": exercise,
                "setCount": trackedExercises[exercise][0],
                "repCount": trackedExercises[exercise][1]
            }
            print(exerciseDataEntry)
            try:
                data = addIntoTable(conn, dataBases[2][1], exerciseDataEntry)
                print(data)
            except:
                print("275")
                pass
        print("Saving")

    def goToShowLines(self):
        global ShowTargetAngles
        if ShowTargetAngles is True:
            ShowTargetAngles = False
        else:
            ShowTargetAngles = True


class Thread(QThread):
    changePixmap = pyqtSignal(QImage)



    def run(self):

        global CurrentExercise
        global CurrentRepCount
        global CurrentAngles
        global ShowTargetAngles
        global FinishWorkout
        #global trainingData
        global defaultCam
        global trackedExercises

        video = None


        repCount = 0
        trainingData = []
        exName = None
        Known = False

        self.defaultCam = defaultCam
        self.repCount = repCount

        mPose = mp.solutions.pose
        pose = mPose.Pose()
        drawLM = mp.solutions.drawing_utils

        detected = False
        Known = False
        
        #def saveWorkout():
        #    global UserInfo
        #    #global trainingData
        
        #    try:
        #        if 2 <= self.repCount and exName.mirrored is False:
        #            self.repCount //= 2

        #        if self.repCount > minimumRepCount:
        #            # key = [setCount, repCount]
        #            if exName.name not in exerciseDict:
        #                exerciseDict[exName.name] = [1, self.repCount]

        #            else:
        #                setCount, repCount = exerciseDict[exName.name]
        #                exerciseDict[exName.name] = [setCount + 1, (repCount + self.repCount) // 2]
                            

        #            # Format: exerciseDict[exercise] => exerciseDict[exercise.name] => [setCount, repCount]
        #            # "userName": UserInfo
        #            # "dateID": 
        #            # "exName": exercise.name
        #            # "setCount": exerciseDict[exercise.name][0]
        #            # "repCount": exerciseDict[exercise.name][1]

        #        Conn = workoutDatabase()
        #        for exercise in exerciseDict:
        #            exerciseDataEntry = {
        #                "userName": UserInfo,
        #                "dateID": QDate().currentDate().toString("yyyy:MM:dd"),
        #                "exName": exercise,
        #                "setCount": exerciseDict[exercise][0],
        #                "repCount": exerciseDict[exercise][1]
        #            }
        #            print(exerciseDataEntry)
        #            try:
        #                data = addIntoTable(Conn, dataBases[2][1], exerciseDataEntry)
        #                print(data)
        #            except:
        #                print("331")
        #                pass
        #    except:
        #        print("337")
        #        pass

        

        pTime = 0

        # Thinking of tracking the positioning of
        # tracked = {"nose": [],
        #            "leftShoulder|leftWrist": [], "rightShoulder|rightWrist": [],
        #            "leftHip|LeftAnkle": [], "rightHip|rightAnkle": []}

        


    
        xLength = 720
        yHeight = 480

        #abductorLegRaises,
        #barbellSquats,
        #bicepCurls,                                    
        #singleArmBicepCurls,
        #deltoidArmRaises,
        #singleArmDeltoidRaises,
        #frontLatRaises,          
        #singleArmFrontLatRaises,
        #gobletSquats,
        #shoulderPress,
        #singleArmShoulderPress

        if self.defaultCam == 0:
            video = VC(0)
        elif self.defaultCam == (0, 1):
            print("Okay")
            video = VC(1)
        elif self.defaultCam == 1:
            video = VC("C:\\Users\\Big Boi J\\source\\repos\\WorkoutAssistant\\WorkoutAssistant\\workoutTrainingVideos\\bicepCurls\\bicep0.mp4")
        elif self.defaultCam == 2:
            video = VC("C:\\Users\\Big Boi J\\source\\repos\\WorkoutAssistant\\WorkoutAssistant\\workoutTrainingVideos\\allExercisesVideo\\allEx.mp4")
            

        video.set(3, xLength)
        video.set(4, yHeight)

        #input('Start')
        #while True: 

        vT0 = .1
        vT1 = .2
        assumpt0 = None

        nOr = False
        vTStart = None
        dTStart = None
        exResetTime = 4

        repCount = 0
        minRepReq = 2
        trackedExercises = {}


        while True:
            try:
                returned, img, detected, \
                exName, repCompleted = readImg(video, pose, drawLM, exName,
                                       showInterest=ShowTargetAngles, showDots=ShowTargetAngles,
                                       showLines=ShowTargetAngles, showText=ShowTargetAngles, known=Known)

            except TypeError as T:
                print('Error:', T)
                continue
            except RuntimeError as R:
                print('Error:', R)
                pass 
            except error as e:
                print('Error:', e)
                pass

            if Known is True:
                if repCompleted is True:
                    if nOr is False:
                        repCount += 1
                        nOr = True
                        dTStart = None
                    
                        CurrentRepCount.setText(f"Rep Count: {repCount}")
                        CurrentAngles.setText(f"Within Range: {repCompleted}")

                else:
                    if dTStart is None:
                        nOr = False
                        dTStart = time()
                    elif int(time() - dTStart) >= exResetTime:
                        if repCount > minRepReq:
                            if exName.name in trackedExercises:
                               totalSet, avgRep = trackedExercises[exName.name]
                               trackedExercises[exName.name] = [(totalSet + 1), (avgRep + repCount) // 2]
                            else:
                               trackedExercises[exName.name] = [1, repCount]

                        print(trackedExercises)
                        repCount = 0
                        Known = False
                        dTStart = None

                        CurrentExercise.setText(f"Exercise: ____") 
                        CurrentRepCount.setText(f"Rep Count: ____")
                        CurrentAngles.setText(f"Within Range: ____")
                print(repCount)
                

            else:
                if detected is True:
                    if assumpt0 is None \
                        and vTStart is None:
                        vTStart = time()

                    elif assumpt0 is None \
                        and int(time() - vTStart) >= vT0:
                        if len(exName) != 1:
                            vTStart = None
                        elif len(exName) == 1:
                            assumpt0 = exName[0]
                            vTStart = time()

                    elif assumpt0 is not None \
                        and int(time() - vTStart) >= vT1:
                        if len(exName) != 1:
                            assumpt0 = None
                            vTStart = None

                        elif len(exName) == 1:
                            if assumpt0.name == exName[0].name:
                                exName = exName[0]
                                CurrentExercise.setText(f"Exercise: {exName.name}") # Move down
                                
                                Known = True
                                dTStart = None

                            assumpt0, vTStart = None, None
                            #elif assumpt0.name != exName[0].name:
                                #assumpt0, vTStart = None, None

                else:
                    print("Not Detected")
                    pass

            if FinishWorkout is True:
                FinishWorkout = False
                print("Saving Workout1")
                #saveWorkout()
                #break
                
            if returned:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cvtColor(img, COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(720, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)


        return("Error")