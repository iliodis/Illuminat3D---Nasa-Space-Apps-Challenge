from tkinter import *
from tkinter import filedialog
import sys
#from tkinter import Tk, Label, Button, StringVar, Entry



from Illuminated_Class import Illuminated


#In this function we check if the variables are valid
def checkInputs():
    rotationAxis = rotAxis.get().split(", ")
    inititalRotation = initRot.get().split(", ")
    try:
        float(omega.get())
        inititalRotation = [float(i) for i in inititalRotation]
        rotationAxis = [float(i) for i in rotationAxis]
        int(frames.get())
        float(albedo.get())
    except ValueError:
        return False
    if not (float(albedo.get()) >= 0 and float(albedo.get()) <= 1):
        return False
   

    obj = Illuminated(label_file_explorer.cget("text").split("/")[-1], inititalRotation, rotationAxis, int(frames.get()), float(albedo.get()), float(omega.get()))
    obj.execution()



# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = r"C:\Users\You\Desktop\SPACEAPPS",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*"),
                                                        ("stl files",
                                                        "*.stl*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)
      
      
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('Illuminat3D')
  
# Set window size
window.geometry("1000x720")

#window.eval('tk::PlaceWindow . center')
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "Open your 3D model file",
                            width = 150, height = 4,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)
  
button_exit = Button(window,
                     text = "Exit",
                     command = sys.exit())

button_run = Button(window,
                    text = "Run Program",
                    command = checkInputs)


label_input1 = Label(window,
                    text = "Source-Earth Angle (e.g. ):",
                    width = 40, height = 3,
                    fg = "blue")
label_input2 = Label(window,
                    text = "Initial Rotation (e.g. ):",
                    width = 40, height = 3,
                    fg = "blue")
label_input3 = Label(window,
                    text = "Third variable:",
                    width = 40, height = 3,
                    fg = "blue") 
label_input4 = Label(window,
                    text = "Fourth variable:",
                    width = 40, height = 3,
                    fg = "blue") 
label_input5 = Label(window,
                    text = "Albedo:",
                    width = 40, height = 3,
                    fg = "blue") 

omega = StringVar()
initRot = StringVar()
rotAxis = StringVar()
frames = StringVar()
albedo = StringVar()

firstVariableEntry = Entry(window, textvariable = omega)
secondVariableEntry = Entry(window, textvariable = initRot)
thirdVariableEntry = Entry(window, textvariable = rotAxis)
fourthVariableEntry = Entry(window, textvariable = frames)
albedoEntry = Entry(window, textvariable = albedo)





label_file_explorer.grid(row = 1)
  
button_explore.grid(column = 0, row = 2)
  


label_input1.grid(column = 0, row = 4, sticky = W, pady = 2)
label_input2.grid(column = 0, row = 5, sticky = W, pady = 2)
label_input3.grid(column = 0, row = 6, sticky = W, pady = 2)
label_input4.grid(column = 0, row = 7, sticky = W, pady = 2)
label_input5.grid(column = 0, row = 8, sticky = W, pady = 2)

firstVariableEntry.grid(row = 4, column = 0, pady = 2)
secondVariableEntry.grid(row = 5, column = 0, pady = 2)
thirdVariableEntry.grid(row = 6, column = 0, pady = 2)
fourthVariableEntry.grid(row = 7, column = 0, pady = 2)
albedoEntry.grid(row = 8, column = 0, pady = 2)



button_run.grid(column = 0,row = 9)
button_exit.grid(column = 0,row = 10)


  

window.mainloop()
