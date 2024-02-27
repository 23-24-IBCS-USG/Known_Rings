import turtle
from turtle import *
from graphics import *
from Button import *
from playsound import playsound

    #——————————————————————————————————————————— ♥︎

def main():

    win = GraphWin("Molly's Mazes", 1442, 846)
    win.setBackground(color_rgb(255, 255, 255))

    #——————————————————————————————————————————— ♥︎ KEYS

    def upEasy():
        t.setheading(90)
        playsound("footstepSound.mp3", block=False)
        t.forward(25)
        
        easyList.append(1)
        easyListText.setText((sum(easyList)))
        easyCoords[:] = str(t.position())
        if easyCoords == ['(', '2', '5', '0', '.', '0', '0', ',', '2', '3', '0', '.', '0', '0', ')']:
            winListEasy.append(1)
        
    def downEasy():
        t.setheading(270)
        playsound("footstepSound.mp3", block=False)
        t.forward(25)

        easyList.append(1)
        easyListText.setText((sum(easyList)))
        easyCoords[:] = str(t.position())
        if easyCoords == ['(', '2', '5', '0', '.', '0', '0', ',', '2', '3', '0', '.', '0', '0', ')']:
            winListEasy.append(1)

    def leftEasy():
        t.setheading(180)
        playsound("footstepSound.mp3", block=False)
        t.forward(25)

        easyList.append(1)
        easyListText.setText((sum(easyList)))
        easyCoords[:] = str(t.position())
        if easyCoords == ['(', '2', '5', '0', '.', '0', '0', ',', '2', '3', '0', '.', '0', '0', ')']:
            winListEasy.append(1)

    def rightEasy():
        t.setheading(0)
        playsound("footstepSound.mp3", block=False)
        t.forward(25)

        easyList.append(1)
        easyListText.setText((sum(easyList)))
        easyCoords[:] = str(t.position())
        if easyCoords == ['(', '2', '5', '0', '.', '0', '0', ',', '2', '3', '0', '.', '0', '0', ')']:
            winListEasy.append(1)


    def upMedium():
        t.setheading(90)
        playsound("footstepSound.mp3", block=False)
        t.forward(20)
        mediumList.append(1)
        mediumListText.setText((sum(mediumList)))
        playsound("footstepSound.mp3", block=False)
        mediumCoords[:] = str(t.position())
        if mediumCoords == ['(', '2', '8', '0', '.', '0', '0', ',', '-', '1', '8', '0', '.', '0', '0', ')']:
            winListMedium.append(1)
         
    def downMedium():
        t.setheading(270)
        playsound("footstepSound.mp3", block=False)
        t.forward(20)
        mediumList.append(1)
        mediumListText.setText((sum(mediumList)))
        playsound("footstepSound.mp3", block=False)
        mediumCoords[:] = str(t.position())
        if mediumCoords == ['(', '2', '8', '0', '.', '0', '0', ',', '-', '1', '8', '0', '.', '0', '0', ')']:
            winListMedium.append(1)

    def leftMedium():
        t.setheading(180)
        playsound("footstepSound.mp3", block=False)
        t.forward(20)
        mediumList.append(1)
        mediumListText.setText((sum(mediumList)))
        playsound("footstepSound.mp3", block=False)
        mediumCoords[:] = str(t.position())
        if mediumCoords == ['(', '2', '8', '0', '.', '0', '0', ',', '-', '1', '8', '0', '.', '0', '0', ')']:
            winListMedium.append(1)

    def rightMedium():
        t.setheading(0)
        playsound("footstepSound.mp3", block=False)
        t.forward(20)
        mediumList.append(1)
        mediumListText.setText((sum(mediumList)))
        playsound("footstepSound.mp3", block=False)
        mediumCoords[:] = str(t.position())
        if mediumCoords == ['(', '2', '8', '0', '.', '0', '0', ',', '-', '1', '8', '0', '.', '0', '0', ')']:
            winListMedium.append(1)


    def upHard():
        t.setheading(90)
        playsound("footstepSound.mp3", block=False)
        t.forward(10)
        hardList.append(1)
        hardListText.setText((sum(hardList)))
        hardCoords[:] = str(t.position())
        if hardCoords == ['(', '2', '9', '5', '.', '0', '0', ',', '1', '5', '.', '0', '0', ')']:
            winListHard.append(1)
         
    def downHard():
        t.setheading(270)
        playsound("footstepSound.mp3", block=False)
        t.forward(10)
        hardList.append(1)
        hardListText.setText((sum(hardList)))
        hardCoords[:] = str(t.position())
        if hardCoords == ['(', '2', '9', '5', '.', '0', '0', ',', '1', '5', '.', '0', '0', ')']:
            winListHard.append(1)

    def leftHard():
        t.setheading(180)
        playsound("footstepSound.mp3", block=False)
        t.forward(10)
        hardList.append(1)
        hardListText.setText((sum(hardList)))
        hardCoords[:] = str(t.position())
        if hardCoords == ['(', '2', '9', '5', '.', '0', '0', ',', '1', '5', '.', '0', '0', ')']:
            winListHard.append(1)

    def rightHard():
        t.setheading(0)
        playsound("footstepSound.mp3", block=False)
        t.forward(10)
        hardList.append(1)
        hardListText.setText((sum(hardList)))
        hardCoords[:] = str(t.position())
        if hardCoords == ['(', '2', '9', '5', '.', '0', '0', ',', '1', '5', '.', '0', '0', ')']:
            winListHard.append(1)


    #——————————————————————————————————————————— ♥︎ LISTS

    easyList = []
    mediumList = []
    hardList = []

    easyCoords = []
    mediumCoords = []
    hardCoords = []

    winListEasy = []
    winListMedium = []
    winListHard = []
    
    #——————————————————————————————————————————— ♥︎ TEXT

    #"welcome" above Welcome Text
    txtWelcomeAbove = Text(Point(710, 90), ("Welcome To"))
    txtWelcomeAbove.setSize(22)
    txtWelcomeAbove.setStyle("bold")
    
    #Welcome Text
    txtWelcome = Text(Point(710, 120), ("Molly's Mazes!"))
    txtWelcome.setSize(36)
    txtWelcome.setStyle("bold")

    #Description
    txtDescription = Text(Point(710, 180), ("Choose a maze to complete:"))
    txtDescription.setSize(22)
    txtDescription.setStyle("bold")

    #Buttons
    txtOk = Text(Point(705, 660), ("OK"))
    txtOk.setSize(18)
    
    txtEasyMaze = Text(Point(270, 425), ("EASY\nMaze"))
    txtEasyMaze.setSize(36)
    txtEasyMaze.setStyle("bold")
    
    txtMediumMaze = Text(Point(710, 425), ("MEDIUM\nMaze"))
    txtMediumMaze.setSize(36)
    txtMediumMaze.setStyle("bold")
    
    txtHardMaze = Text(Point(1150, 425), ("HARD\nMaze"))
    txtHardMaze.setSize(36)
    txtHardMaze.setStyle("bold")

    txtQ = Text(Point(710, 740), ("QUIT"))
    txtQ.setSize(18)
    txtQ.setStyle("bold")

    #Intro
    introBorderUp = Text(Point(720, 10), ("————————————————————————————————————————————"))
    introBorderUp.setSize(32)
    introBorderUp.setTextColor(color_rgb(255, 250, 140))

    introBorderDown = Text(Point(720, 830), ("————————————————————————————————————————————"))
    introBorderDown.setSize(32)
    introBorderDown.setTextColor(color_rgb(255, 250, 140))

    introBorderLeft = Text(Point(15, 424), ("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|"))
    introBorderLeft.setSize(32)
    introBorderLeft.setTextColor(color_rgb(255, 250, 140))

    introBorderRight = Text(Point(1425, 424), ("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|"))
    introBorderRight.setSize(32)
    introBorderRight.setTextColor(color_rgb(255, 250, 140))
    
    txtIntro = Text(Point(710, 400), ("Welcome to MOLLY'S MAZES!"))
    txtIntro.setSize(32)
    txtIntro.setTextColor(color_rgb(255, 250, 140))
    txtIntro.setStyle("bold")

    txtRules = Text(Point(710, 400), ("𝟏\nDue to this program being coded in IDLE,\n some of the buttons take several tries\n to click. Move your mouse to different\npositions on the button and keep clicking.\n\n𝟐\nYou may use the buttons or the arrow\nkeys to move your line.\n\n𝟑.\nDue to the aforementioned limits, the\nmaze cannot be ''won'' unless a button is\npressed after you pass ''finish line.''"))
    txtRules.setSize(22)
    txtRules.setTextColor(color_rgb(255, 250, 140))

    #Reload
    txtMessageImage = Text(Point(710, 340), ("☀"))
    txtMessageImage.setSize(36)
    txtMessageImage.setTextColor(color_rgb(215, 120, 0))
    txtMessageImage.setStyle("bold")
    
    txtMessage = Text(Point(710, 380), ("Please reload the program to start another maze."))
    txtMessage.setSize(32)
    txtMessage.setTextColor(color_rgb(215, 120, 0))
    txtMessage.setStyle("bold")

    #——————————————————————————————————————————— ♥︎ SHAPES

    btnWelcome = Rectangle(Point(570, 70), Point(850, 150))
    
    #——————————————————————————————————————————— ♥︎ BUTTONS
    
    ok = Button(win, Point(655, 640), Point(755, 680), color_rgb(255, 180, 0), " ")
    easyMaze = Button(win, Point(120, 350), Point(420, 500), color_rgb(250, 250, 250), " ") #mid = (270,425)
    mediumMaze = Button(win, Point(560, 350), Point(860, 500), color_rgb(250, 250, 250), " ") # = (710,425)
    hardMaze = Button(win, Point(1000, 350), Point(1300, 500), color_rgb(250, 250, 250), " ") # = (1150,425)
    Q = QuitButton(win, Point(660, 710), Point(760, 770), color_rgb(230, 150, 150), " ") # = (710,740)

    #——————————————————————————————————————————— ♥︎ PREPARATORY UNDRAWS

    ok.undraw()
    txtOk.undraw()
    easyMaze.undraw()
    txtEasyMaze.undraw()
    mediumMaze.undraw()
    txtMediumMaze.undraw()
    hardMaze.undraw()
    txtHardMaze.undraw()
    txtWelcomeAbove.undraw()
    txtWelcome.undraw()
    txtDescription.undraw()
    btnWelcome.undraw()
    Q.undraw()

#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ INTRO
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ INTRO
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ INTRO
    #Appear

    txtIntro.draw(win)
    introBorderUp.draw(win)
    introBorderDown.draw(win)
    introBorderLeft.draw(win)
    introBorderRight.draw(win)
    time.sleep(0.2)

    txtIntro.setTextColor(color_rgb(255, 255, 200))
    introBorderUp.setTextColor(color_rgb(255, 255, 200))
    introBorderDown.setTextColor(color_rgb(255, 255, 200))
    introBorderLeft.setTextColor(color_rgb(255, 255, 200))
    introBorderRight.setTextColor(color_rgb(255, 255, 200))
    time.sleep(0.1)

    txtIntro.setTextColor(color_rgb(255, 250, 150))
    introBorderUp.setTextColor(color_rgb(255, 250, 150))
    introBorderDown.setTextColor(color_rgb(255, 250, 150))
    introBorderLeft.setTextColor(color_rgb(255, 250, 150))
    introBorderRight.setTextColor(color_rgb(255, 250, 150))
    time.sleep(0.1)
    
    
    txtIntro.setTextColor(color_rgb(255, 240, 120))
    introBorderUp.setTextColor(color_rgb(255, 240, 120))
    introBorderDown.setTextColor(color_rgb(255, 240, 120))
    introBorderLeft.setTextColor(color_rgb(255, 240, 120))
    introBorderRight.setTextColor(color_rgb(255, 240, 120))
    time.sleep(0.2)
    
    txtIntro.setTextColor(color_rgb(255, 230, 100))
    introBorderUp.setTextColor(color_rgb(255, 230, 100))
    introBorderDown.setTextColor(color_rgb(255, 230, 100))
    introBorderLeft.setTextColor(color_rgb(255, 230, 100))
    introBorderRight.setTextColor(color_rgb(255, 230, 100))
    time.sleep(0.2)
    
    txtIntro.setTextColor(color_rgb(255, 220, 80))
    introBorderUp.setTextColor(color_rgb(255, 220, 80))
    introBorderDown.setTextColor(color_rgb(255, 220, 80))
    introBorderLeft.setTextColor(color_rgb(255, 220, 80))
    introBorderRight.setTextColor(color_rgb(255, 220, 80))
    time.sleep(0.2)
    
    txtIntro.setTextColor(color_rgb(255, 210, 60))
    introBorderUp.setTextColor(color_rgb(255, 210, 60))
    introBorderDown.setTextColor(color_rgb(255, 210, 60))
    introBorderLeft.setTextColor(color_rgb(255, 210, 60))
    introBorderRight.setTextColor(color_rgb(255, 210, 60))
    time.sleep(0.2)
    
    txtIntro.setTextColor(color_rgb(255, 200, 40))
    introBorderUp.setTextColor(color_rgb(255, 200, 40))
    introBorderDown.setTextColor(color_rgb(255, 200, 40))
    introBorderLeft.setTextColor(color_rgb(255, 200, 40))
    introBorderRight.setTextColor(color_rgb(255, 200, 40))
    time.sleep(0.2)
    
    txtIntro.setTextColor(color_rgb(255, 190, 20))
    introBorderUp.setTextColor(color_rgb(255, 190, 20))
    introBorderDown.setTextColor(color_rgb(255, 190, 20))
    introBorderLeft.setTextColor(color_rgb(255, 190, 20))
    introBorderRight.setTextColor(color_rgb(255, 190, 20))
    time.sleep(0.2)

    txtIntro.setTextColor(color_rgb(255, 180, 0))
    introBorderUp.setTextColor(color_rgb(255, 180, 0))
    introBorderDown.setTextColor(color_rgb(255, 180, 0))
    introBorderLeft.setTextColor(color_rgb(255, 180, 0))
    introBorderRight.setTextColor(color_rgb(255, 180, 0))
    
    playsound("yippeeee.mp3")
    
    #Disappear

    txtIntro.setTextColor(color_rgb(255, 190, 20))
    time.sleep(0.05)

    txtIntro.setTextColor(color_rgb(255, 200, 50))
    time.sleep(0.05)

    txtIntro.setTextColor(color_rgb(255, 210, 80))
    time.sleep(0.05)

    txtIntro.setTextColor(color_rgb(255, 220, 110))
    time.sleep(0.05)

    txtIntro.setTextColor(color_rgb(255, 230, 140))
    time.sleep(0.05)

    txtIntro.setTextColor(color_rgb(255, 240, 170))
    time.sleep(0.05)

    txtIntro.setTextColor(color_rgb(255, 250, 200))
    txtIntro.undraw()
    time.sleep(0.5)
    
    #Rules appear----------------------------------------
    
    txtRules.draw(win)

    txtRules.setTextColor(color_rgb(255, 255, 200))
    time.sleep(0.1)
    
    txtRules.setTextColor(color_rgb(255, 250, 150))
    time.sleep(0.1)

    txtRules.setTextColor(color_rgb(255, 240, 120))
    time.sleep(0.2)
    
    txtRules.setTextColor(color_rgb(255, 230, 100))
    time.sleep(0.2)
    
    txtRules.setTextColor(color_rgb(255, 220, 80))
    time.sleep(0.2)
    
    txtRules.setTextColor(color_rgb(255, 210, 60))
    time.sleep(0.2)
    
    txtRules.setTextColor(color_rgb(255, 200, 40))
    time.sleep(0.2)
    
    txtRules.setTextColor(color_rgb(255, 190, 20))
    time.sleep(0.2)

    txtRules.setTextColor(color_rgb(255, 180, 0))
    ok.draw(win)
    txtOk.draw(win)


#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ MAIN
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ MAIN
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ MAIN
        
    
    while True:
        m = win.getMouse()

        if ok.isClicked(m):

            ok.setFill(color_rgb(225, 150, 0))
            time.sleep(0.09)
            ok.setFill(color_rgb(255, 180, 0))

            time.sleep(0.1)

            ok.undraw()
            txtOk.undraw()
                
            txtRules.setTextColor(color_rgb(255, 190, 20))

            time.sleep(0.05)

            txtRules.setTextColor(color_rgb(255, 200, 50))

            time.sleep(0.05)

            txtRules.setTextColor(color_rgb(255, 210, 80))

            time.sleep(0.05)

            txtRules.setTextColor(color_rgb(255, 220, 110))
            
            time.sleep(0.05)

            txtRules.setTextColor(color_rgb(255, 230, 140))
            
            time.sleep(0.05)

            txtRules.setTextColor(color_rgb(255, 240, 170))

            time.sleep(0.05)

            txtRules.setTextColor(color_rgb(255, 250, 200))

            txtRules.undraw()
            
            win.setBackground(color_rgb(255, 200, 0))
            win.setBackground(color_rgb(255, 180, 0))
            introBorderUp.setTextColor(color_rgb(0, 0, 0))
            introBorderDown.setTextColor(color_rgb(0, 0, 0))
            introBorderLeft.setTextColor(color_rgb(0, 0, 0))
            introBorderRight.setTextColor(color_rgb(0, 0, 0))
            time.sleep(0.2)
            
            txtWelcomeAbove.draw(win)
            txtWelcome.draw(win)
            
            txtDescription.draw(win)
            
            btnWelcome.draw(win)

            easyMaze.draw(win)
            mediumMaze.draw(win)
            hardMaze.draw(win)
            
            txtEasyMaze.draw(win)
            txtMediumMaze.draw(win)
            txtHardMaze.draw(win)

            Q.draw(win)
            txtQ.draw(win)

#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ EASY MAZE
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ EASY MAZE
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ EASY MAZE

        elif easyMaze.isClicked(m):
                playsound("yippee.mp3", block=False)
                
                easyMaze.setFill(color_rgb(230, 230, 250)) #new color
                time.sleep(0.09)
                easyMaze.setFill(color_rgb(250, 250, 250)) #old color

                time.sleep(0.3)

                winEasy = GraphWin("Easy Controls", 200, 220)
                winEasy.setBackground(color_rgb(255, 180, 0))

                canvasEasy = turtle.Screen()
                canvasEasy.title("Easy Maze")

                t = turtle.Turtle()
                t.pencolor("orange")
                t.color("orange")
                t.speed(1000)
                t.width(7)

                #Steps
                easyListStepsText = Text(Point(30, 10), ("Steps taken:"))
                easyListStepsText.setSize(10)

                easyListText = Text(Point(70, 10), ("0"))
                easyListText.setSize(10)
                
                easyListStepsText.draw(winEasy)
                easyListText.draw(winEasy)

                #Undraw
                easyMaze.undraw()
                txtEasyMaze.undraw()
                mediumMaze.undraw()
                txtMediumMaze.undraw()
                hardMaze.undraw()
                txtHardMaze.undraw()
                txtWelcomeAbove.undraw()
                txtWelcome.undraw()
                txtDescription.undraw()
                btnWelcome.undraw()

                txtMessageImage.draw(win)
                txtMessage.draw(win)

                #——————————————————————————————————————————— ♥︎ BUTTONS

                upButtonEasy = Button(winEasy, Point(70,25), Point(130, 85), color_rgb(250, 250, 250), "↑")
                downButtonEasy = Button(winEasy, Point(70, 155), Point(130, 215), color_rgb(250, 250, 250), "↓")
                leftButtonEasy = Button(winEasy, Point(5, 90), Point(65, 150), color_rgb(250, 250, 250), "←")
                rightButtonEasy = Button(winEasy, Point(135, 90), Point(195, 150), color_rgb(250, 250, 250), "→")

                undoEasy = Button(winEasy, Point(70, 90), Point(130, 150), color_rgb(250, 200, 150), " ")
                QEasy = Button(winEasy, Point(175, 5), Point(195, 25), color_rgb(230, 150, 150), "X")

                #——————————————————————————————————————————— ♥︎ TEXT

                txtUndoEasy = Text(Point(100, 120), ("⟲"))
                txtUndoEasy.setSize(20)
                txtUndoEasy.setStyle("bold")

                #——————————————————————————————————————————— ♥︎ ACTIONS

                txtUndoEasy.draw(winEasy)

                #——————————————————————————————————————————— ♥︎ LOOP
                
                while True:
                    mEasy = winEasy.getMouse()
                    
                    canvasEasy.onkey(upEasy,"Up")
                    canvasEasy.onkey(downEasy,"Down")
                    canvasEasy.onkey(leftEasy,"Left")
                    canvasEasy.onkey(rightEasy,"Right")

                    canvasEasy.listen()
    
                    if undoEasy.isClicked(mEasy):
                        t.clear()
                        undoEasy.setFill(color_rgb(230, 180, 150))
                        time.sleep(0.09)
                        undoEasy.setFill(color_rgb(250, 200, 150))
                        turtle.bgpic("easyMaze.png")
                        t.penup()
                        t.goto(-250, -220)
                        t.pendown()
                        t.speed(100)
                        playsound("yippee.mp3")
                        playsound("easyMaze.mp3", block=False)
                        easyCoords[:] = str(t.position())
                        if easyCoords == ['(', '2', '5', '0', '.', '0', '0', ',', '2', '3', '0', '.', '0', '0', ')']:
                            winListEasy.append(1)
                        
                        
                    elif upButtonEasy.isClicked(mEasy):
                        upButtonEasy.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        upButtonEasy.setFill(color_rgb(250, 250, 250))
                        t.setheading(90)
                        t.forward(25)
                        easyList.append(1)
                        easyListText.setText((sum(easyList)))
                        playsound("footstepSound.mp3", block=False)
                        easyCoords[:] = str(t.position())
                        if easyCoords == ['(', '2', '5', '0', '.', '0', '0', ',', '2', '3', '0', '.', '0', '0', ')']:
                            winListEasy.append(1)

                    elif downButtonEasy.isClicked(mEasy):
                        downButtonEasy.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        downButtonEasy.setFill(color_rgb(250, 250, 250))
                        t.setheading(270)
                        t.forward(25)
                        easyList.append(1)
                        easyListText.setText((sum(easyList)))
                        playsound("footstepSound.mp3", block=False)
                        easyCoords[:] = str(t.position())
                        if easyCoords == ['(', '2', '5', '0', '.', '0', '0', ',', '2', '3', '0', '.', '0', '0', ')']:
                            winListEasy.append(1)

                    elif rightButtonEasy.isClicked(mEasy):
                        rightButtonEasy.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        rightButtonEasy.setFill(color_rgb(250, 250, 250))
                        t.setheading(0)
                        t.forward(25)
                        easyList.append(1)
                        easyListText.setText((sum(easyList)))
                        playsound("footstepSound.mp3", block=False)
                        easyCoords[:] = str(t.position())
                        if easyCoords == ['(', '2', '5', '0', '.', '0', '0', ',', '2', '3', '0', '.', '0', '0', ')']:
                            winListEasy.append(1)

                    elif leftButtonEasy.isClicked(mEasy):
                        leftButtonEasy.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        leftButtonEasy.setFill(color_rgb(250, 250, 250))
                        t.setheading(180)
                        t.forward(25)
                        easyList.append(1)
                        easyListText.setText((sum(easyList)))
                        playsound("footstepSound.mp3", block=False)
                        easyCoords[:] = str(t.position())
                        if easyCoords == ['(', '2', '5', '0', '.', '0', '0', ',', '2', '3', '0', '.', '0', '0', ')']:
                            winListEasy.append(1)

                    i = 1

                    if i in winListEasy:
                      
                        winWinListEasy = GraphWin("Yippee!", 620, 80)
                        winWinListEasy.setBackground(color_rgb(255, 255, 255))
                        txtWinEasy = Text(Point(310, 40), ("You win!!!"))
                        txtWinEasy.setSize(36)
                        txtWinEasy.setStyle("bold")
                        txtWinEasy.setTextColor(color_rgb(255, 180, 0))
                        txtWinEasy.draw(winWinListEasy)
                        winListEasy.clear()
                        playsound("victoryMusic.mp3", block=False)
                        time.sleep(0.5)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.4)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.3)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.3)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.5)
                        playsound("yippee.mp3", block=False)
    

                    elif QEasy.isClicked(mEasy):
                        QEasy.setFill(color_rgb(200, 120, 120))
                        time.sleep(0.09)
                        QEasy.setFill(color_rgb(230, 150, 150))
                        playsound("yippee.mp3")
                        break
                    
                winEasy.close()
                winWinListEasy = GraphWin(".", 1, 1)
                winWinListEasy.close()
                turtle.bye()

#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ MEDIUM MAZE
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ MEDIUM MAZE
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ MEDIUM MAZE

        elif mediumMaze.isClicked(m):
                mediumMaze.setFill(color_rgb(230, 230, 250)) #new color
                time.sleep(0.09)
                mediumMaze.setFill(color_rgb(250, 250, 250)) #old color

                playsound("yippee.mp3", block=False)

                winMedium = GraphWin("Medium Controls", 200, 220)
                winMedium.setBackground(color_rgb(255, 180, 0))

                canvasMedium = turtle.Screen()
                canvasMedium.title("Medium Maze")

                t = turtle.Turtle()
                t.pencolor("orange")
                t.color("orange")
                t.speed(1000)
                t.width(5)

                #Steps
                mediumListStepsText = Text(Point(30, 10), ("Steps taken:"))
                mediumListStepsText.setSize(10)

                mediumListText = Text(Point(70, 10), ("0"))
                mediumListText.setSize(10)
                
                mediumListStepsText.draw(winMedium)
                mediumListText.draw(winMedium)

                #Undraw
                easyMaze.undraw()
                txtEasyMaze.undraw()
                mediumMaze.undraw()
                txtMediumMaze.undraw()
                hardMaze.undraw()
                txtHardMaze.undraw()
                txtWelcomeAbove.undraw()
                txtWelcome.undraw()
                txtDescription.undraw()
                btnWelcome.undraw()

                txtMessageImage.draw(win)
                txtMessage.draw(win)

                #——————————————————————————————————————————— ♥︎ BUTTONS

                upButtonMedium = Button(winMedium, Point(70,25), Point(130, 85), color_rgb(250, 250, 250), "↑")
                downButtonMedium = Button(winMedium, Point(70, 155), Point(130, 215), color_rgb(250, 250, 250), "↓")
                leftButtonMedium = Button(winMedium, Point(5, 90), Point(65, 150), color_rgb(250, 250, 250), "←")
                rightButtonMedium = Button(winMedium, Point(135, 90), Point(195, 150), color_rgb(250, 250, 250), "→")

                undoMedium = Button(winMedium, Point(70, 90), Point(130, 150), color_rgb(250, 200, 150), " ")
                QMedium = Button(winMedium, Point(175, 5), Point(195, 25), color_rgb(230, 150, 150), "X")

                #——————————————————————————————————————————— ♥︎ TEXT

                txtUndoMedium = Text(Point(100, 120), ("⟲"))
                txtUndoMedium.setSize(20)
                txtUndoMedium.setStyle("bold")

                #——————————————————————————————————————————— ♥︎ ACTIONS

                txtUndoMedium.draw(winMedium)

                #——————————————————————————————————————————— ♥︎ LOOP
                
                while True:
                    mMedium = winMedium.getMouse()

                    canvasMedium.onkey(upMedium,"Up")
                    canvasMedium.onkey(downMedium,"Down")
                    canvasMedium.onkey(leftMedium,"Left")
                    canvasMedium.onkey(rightMedium,"Right")

                    canvasMedium.listen()

                    if undoMedium.isClicked(mMedium):
                        t.clear()
                        turtle.bgpic("MediumMaze.png")
                        t.penup()
                        t.goto(-280, 180)
                        t.pendown()
                        t.speed(100)
                        playsound("yippee.mp3")
                        playsound("mediumMaze.mp3", block=False)
                        mediumCoords[:] = str(t.position())
                        if mediumCoords == ['(', '2', '8', '0', '.', '0', '0', ',', '-', '1', '8', '0', '.', '0', '0', ')']:
                            winListMedium.append(1)
                        
                    elif upButtonMedium.isClicked(mMedium):
                        upButtonMedium.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        upButtonMedium.setFill(color_rgb(250, 250, 250))
                        t.setheading(90)
                        t.forward(20)
                        mediumList.append(1)
                        mediumListText.setText((sum(mediumList)))
                        playsound("footstepSound.mp3", block=False)
                        mediumCoords[:] = str(t.position())
                        if mediumCoords == ['(', '2', '8', '0', '.', '0', '0', ',', '-', '1', '8', '0', '.', '0', '0', ')']:
                            winListMedium.append(1)
                        
                    elif downButtonMedium.isClicked(mMedium):
                        downButtonMedium.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        downButtonMedium.setFill(color_rgb(250, 250, 250))
                        t.setheading(270)
                        t.forward(20)
                        mediumList.append(1)
                        mediumListText.setText((sum(mediumList)))
                        playsound("footstepSound.mp3", block=False)
                        mediumCoords[:] = str(t.position())
                        if mediumCoords == ['(', '2', '8', '0', '.', '0', '0', ',', '-', '1', '8', '0', '.', '0', '0', ')']:
                            winListMedium.append(1)
                        
                    elif rightButtonMedium.isClicked(mMedium):
                        rightButtonMedium.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        rightButtonMedium.setFill(color_rgb(250, 250, 250))
                        t.setheading(0)
                        t.forward(20)
                        mediumList.append(1)
                        mediumListText.setText((sum(mediumList)))
                        playsound("footstepSound.mp3", block=False)
                        mediumCoords[:] = str(t.position())
                        if mediumCoords == ['(', '2', '8', '0', '.', '0', '0', ',', '-', '1', '8', '0', '.', '0', '0', ')']:
                            winListMedium.append(1)

                    elif leftButtonMedium.isClicked(mMedium):
                        leftButtonMedium.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        leftButtonMedium.setFill(color_rgb(250, 250, 250))
                        t.setheading(180)
                        t.forward(20)
                        mediumList.append(1)
                        mediumListText.setText((sum(mediumList)))
                        playsound("footstepSound.mp3", block=False)
                        mediumCoords[:] = str(t.position())
                        if mediumCoords == ['(', '2', '8', '0', '.', '0', '0', ',', '-', '1', '8', '0', '.', '0', '0', ')']:
                            winListMedium.append(1)
                        
                    i = 1

                    if i in winListMedium:
                       
                        winWinListMedium = GraphWin("Yippee!", 620, 80)
                        winWinListMedium.setBackground(color_rgb(255, 255, 255))
                        txtWinMedium = Text(Point(310, 40), ("You win!!!"))
                        txtWinMedium.setSize(36)
                        txtWinMedium.setStyle("bold")
                        txtWinMedium.setTextColor(color_rgb(255, 180, 0))
                        txtWinMedium.draw(winWinListMedium)
                        winListMedium.clear()
                        playsound("victoryMusic.mp3", block=False)
                        time.sleep(0.5)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.4)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.3)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.3)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.5)
                        playsound("yippee.mp3", block=False)

                    elif QMedium.isClicked(mMedium):
                        QMedium.setFill(color_rgb(200, 120, 120))
                        time.sleep(0.09)
                        QMedium.setFill(color_rgb(230, 150, 150))
                        #time.sleep(0.55)
                        playsound("yippee.mp3")
                        break
                    
                winMedium.close()
                winWinListMedium.close()
                winWinListMedium = GraphWin(".", 1, 1)
                turtle.bye()


#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ HARD MAZE
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ HARD MAZE
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ HARD MAZE

        elif hardMaze.isClicked(m):
                hardMaze.setFill(color_rgb(230, 230, 250)) #new color
                time.sleep(0.09)
                hardMaze.setFill(color_rgb(250, 250, 250)) #old color

                playsound("yippee.mp3", block=False)

                winHard = GraphWin("Hard Controls", 200, 220)
                winHard.setBackground(color_rgb(255, 180, 0))

                canvasHard = turtle.Screen()
                canvasHard.title("Hard Maze")

                t = turtle.Turtle()
                t.pencolor("orange")
                t.color("orange")
                t.speed(1000)
                t.width(3)

                #Steps
                hardListStepsText = Text(Point(30, 10), ("Steps taken:"))
                hardListStepsText.setSize(10)

                hardListText = Text(Point(70, 10), ("0"))
                hardListText.setSize(10)
                
                hardListStepsText.draw(winHard)
                hardListText.draw(winHard)

                #Undraw
                easyMaze.undraw()
                txtEasyMaze.undraw()
                mediumMaze.undraw()
                txtMediumMaze.undraw()
                hardMaze.undraw()
                txtHardMaze.undraw()
                txtWelcomeAbove.undraw()
                txtWelcome.undraw()
                txtDescription.undraw()
                btnWelcome.undraw()

                txtMessageImage.draw(win)
                txtMessage.draw(win)

                #——————————————————————————————————————————— ♥︎ BUTTONS

                upButtonHard = Button(winHard, Point(70,25), Point(130, 85), color_rgb(250, 250, 250), "↑")
                downButtonHard = Button(winHard, Point(70, 155), Point(130, 215), color_rgb(250, 250, 250), "↓")
                leftButtonHard = Button(winHard, Point(5, 90), Point(65, 150), color_rgb(250, 250, 250), "←")
                rightButtonHard = Button(winHard, Point(135, 90), Point(195, 150), color_rgb(250, 250, 250), "→")

                undoHard = Button(winHard, Point(70, 90), Point(130, 150), color_rgb(250, 200, 150), " ")
                QHard = Button(winHard, Point(175, 5), Point(195, 25), color_rgb(230, 150, 150), "X")

                #——————————————————————————————————————————— ♥︎ TEXT

                txtUndoHard = Text(Point(100, 120), ("⟲"))
                txtUndoHard.setSize(20)
                txtUndoHard.setStyle("bold")

                #——————————————————————————————————————————— ♥︎ ACTIONS

                txtUndoHard.draw(winHard)

                #——————————————————————————————————————————— ♥︎ LOOP
                
                while True:
                    mHard = winHard.getMouse()

                    canvasHard.onkey(upHard,"Up")
                    canvasHard.onkey(downHard,"Down")
                    canvasHard.onkey(leftHard,"Left")
                    canvasHard.onkey(rightHard,"Right")

                    canvasHard.listen()

                    if undoHard.isClicked(mHard):
                        t.clear()
                        turtle.bgpic("HardMaze.png")
                        t.penup()
                        t.goto(-295, -15)
                        t.pendown()
                        t.speed(100)
                        playsound("yippee.mp3")
                        playsound("hardMaze.mp3", block=False)
                        hardCoords[:] = str(t.position())
                        if hardCoords == ['(', '2', '9', '5', '.', '0', '0', ',', '1', '5', '.', '0', '0', ')']:
                            winListHard.append(1)
                        
                    elif upButtonHard.isClicked(mHard):
                        upButtonHard.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        upButtonHard.setFill(color_rgb(250, 250, 250))
                        t.setheading(90)
                        t.forward(10)
                        playsound("footstepSound.mp3", block=False)
                        hardList.append(1)
                        hardListText.setText((sum(hardList)))
                        hardCoords[:] = str(t.position())
                        if hardCoords == ['(', '2', '9', '5', '.', '0', '0', ',', '1', '5', '.', '0', '0', ')']:
                            winListHard.append(1)

                    elif downButtonHard.isClicked(mHard):
                        downButtonHard.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        downButtonHard.setFill(color_rgb(250, 250, 250))
                        t.setheading(270)
                        t.forward(10)
                        hardList.append(1)
                        hardListText.setText((sum(hardList)))
                        playsound("footstepSound.mp3", block=False)
                        hardCoords[:] = str(t.position())
                    
                        if hardCoords == ['(', '2', '9', '5', '.', '0', '0', ',', '1', '5', '.', '0', '0', ')']:
                            winListHard.append(1)

                    elif rightButtonHard.isClicked(mHard):
                        rightButtonHard.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        rightButtonHard.setFill(color_rgb(250, 250, 250))
                        t.setheading(0)
                        t.forward(10)
                        hardList.append(1)
                        hardListText.setText((sum(hardList)))
                        playsound("footstepSound.mp3", block=False)
                        hardCoords[:] = str(t.position())
              
                        if hardCoords == ['(', '2', '9', '5', '.', '0', '0', ',', '1', '5', '.', '0', '0', ')']:
                            winListHard.append(1)

                    elif leftButtonHard.isClicked(mHard):
                        leftButtonHard.setFill(color_rgb(230, 230, 250))
                        time.sleep(0.09)
                        leftButtonHard.setFill(color_rgb(250, 250, 250))
                        t.setheading(180)
                        t.forward(10)
                        hardList.append(1)
                        hardListText.setText((sum(hardList)))
                        playsound("footstepSound.mp3", block=False)
                        hardCoords[:] = str(t.position())
                        if hardCoords == ['(', '2', '9', '5', '.', '0', '0', ',', '1', '5', '.', '0', '0', ')']:
                            winListHard.append(1)
                        
                    i = 1

                    if i in winListHard:
                        
                        winWinListHard = GraphWin("Yippee!", 620, 80)
                        winWinListHard.setBackground(color_rgb(255, 255, 255))
                        txtWinHard = Text(Point(310, 40), ("You win!!!"))
                        txtWinHard.setSize(36)
                        txtWinHard.setStyle("bold")
                        txtWinHard.setTextColor(color_rgb(255, 180, 0))
                        txtWinHard.draw(winWinListHard)
                        winListHard.clear()
                        playsound("victoryMusic.mp3", block=False)
                        time.sleep(0.5)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.4)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.3)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.3)
                        playsound("yippee.mp3", block=False)
                        time.sleep(0.5)
                        playsound("yippee.mp3", block=False)

                    elif QHard.isClicked(mHard):
                        QHard.setFill(color_rgb(200, 120, 120))
                        time.sleep(0.09)
                        QHard.setFill(color_rgb(230, 150, 150))
                        playsound("yippee.mp3")
                        break
                    
                winHard.close()
                winWinListHard = GraphWin(".", 1, 1)
                winWinListHard.close()
                turtle.bye()

#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ QUIT
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ QUIT 
#—————————————————————————————————————————————————————————————————————————————————————————— ♥︎ QUIT 

                
        elif Q.isClicked(m):
            Q.setFill(color_rgb(200, 120, 120)) #new color
            time.sleep(0.09)
            Q.setFill(color_rgb(230, 150, 150)) #old color
            playsound("yippee.mp3")
            break

    win.close()
    winEasy.close()
    winMedium.close()
    winHard.close()
    turtle.bye()
    winWinListEasy = GraphWin(".", 1, 1)
    winWinListEasy.close()
    winWinListMedium = GraphWin(".", 1, 1)
    winWinListMedium.close()
    winWinListHard = GraphWin(".", 1, 1)
    winWinListHard.close()
    

if __name__ == "__main__":
    main()
