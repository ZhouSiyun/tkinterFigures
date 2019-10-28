from tkinter import *
import turtleFigures 

import turtle

root = Tk()
root.geometry("800x600+300+300")
root.title("Euro to Dollar Converter")

# BUTTONS HANDLER

# CLEAR FUNCTION
def onClearF():
    entryOrder.delete(0, END)
    entryLength.delete(0, END)
    turtleStr.set("")
    canvas.delete("all")
    textInfo.delete(1.0, END)
    mainloop() == False
# END CLEAR

def onDrawF():
    pen = turtle.RawTurtle(canvas)
    pen.color("black")
    pen.speed(0)
    pen.width(3)
    print("Drawing start")
    textInfo.insert(INSERT, 'Drawing Started!\n')
    # read length and order and figure type
    n = int(orderStr.get())
    l = int(lengthStr.get())
    textInfo.insert(INSERT, 'NAME:' + turtleStr.get() + '\n')
    textInfo.insert(INSERT, 'ORDER:' + str(n) + '\n')
    textInfo.insert(INSERT, 'LENGTH:' + str(l) + '\n')
    print(n)
    print(l)
    turtleIndex = turtleList.index(turtleStr.get())
    if turtleIndex == 0:
        turtleFigures.tree(n,l,pen)
    if turtleIndex == 1:
        turtleFigures.dandelion(n,l,pen)
    if turtleIndex == 2:
        turtleFigures.fern(n,l,pen)
    if turtleIndex == 3:
        turtleFigures.flake(n,l,pen)
    if turtleIndex == 4:
        turtleFigures.antiflake(n,l,pen)
    if turtleIndex == 5:
        turtleFigures.sperpinskyGasket(n,l,pen)
    if turtleIndex == 6:
        turtleFigures.squreGasket(n,l,pen)
    if turtleIndex == 7:
        turtleFigures.circleGasket(n,l,pen)
    #------------NOT DEFINE-----------    
    if turtleIndex == 8:
        turtleFigures.new1(n,l,pen)
    if turtleIndex == 9:
        turtleFigures.mixGasket(n,l,pen)


    print(turtleIndex)
          
     # check what figure u draw

     # if figure 0 then 1) set the initial position and direction 2) draw 3) write the info in text

     # call the function as turtleFigures.tree(order, length, pen)
    print("Drawing Finished")
    textInfo.insert(INSERT, 'Drawing Finished!\n')

#end drawF


    

''' the interface components '''
             
root.title("Julia Fractal")

label = Label(root, text = "Turtle Fractal Generator")
label.grid(row = 0, column = 1, columnspan = 2)


canvasFrame = LabelFrame(root, text = "Canvas Space", width = 510, height = 510) # LableFrame is a kind of contener         
canvas = Canvas(canvasFrame, width = 500, height = 500) # Put the canvas inside the lableframe
canvas.pack() #pack means follow the order of element behind canvas
canvasFrame.grid(row = 1,column = 0, ipadx = 2, ipady = 2, padx =5, pady =5, columnspan = 4, rowspan = 4)

controlFrame = LabelFrame(root, text = "Control Panel")
controlFrame.grid(row = 1, column = 5, columnspan = 2, rowspan = 4, ipadx = 2, ipady = 2, padx =5, pady =5)

labelOrder = Label(controlFrame, width = 10,text = "Order")
labelOrder.grid(row = 1, column =0)

orderStr = StringVar()
entryOrder = Entry(controlFrame, width = 10,textvariable = orderStr)
entryOrder.grid(row = 1, column = 1) 

labelLength = Label(controlFrame, width = 10,text = "Length")
labelLength.grid(row = 2, column =0)

lengthStr = StringVar()
entryLength = Entry(controlFrame, width = 10,textvariable = lengthStr)
entryLength.grid(row = 2, column = 1)

labelFigure = Label(controlFrame,width = 10, text = "Figure")
labelFigure.grid(row = 3, column =0)

textInfo = Text(controlFrame,width = 30, height = 20)
textInfo.grid(row = 5, column = 0,columnspan = 2)


#drop down list
turtleList = ["Binary Tree","Dandelion","Fern Tree","Snow Flack","Anty- SnowFlack","Sierpinsky Gaskit","Squar Gaskit","Circle Fractal","Circle Gasket2","Mix Gasket"]
turtleStr = StringVar()
turtleOptionMenu = OptionMenu(controlFrame,turtleStr, *turtleList)
turtleOptionMenu.grid(row = 3 ,column = 1)
turtleOptionMenu["width"] = 10
clearButton = Button(controlFrame, text = "Clear", width = 10, command = onClearF)
clearButton.grid(row = 4, column = 0)
drawButton = Button(controlFrame, text = "Draw", width = 10,command = onDrawF)
drawButton.grid(row = 4, column = 1)



''' -------------------turtle controls-----------------'''




         
mainloop()
