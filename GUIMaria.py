from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


from new_SpaceApps import Illuminated


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
    filename = filedialog.askopenfilename(initialdir = "C:/Users/antonia/Desktop/python/2.stl",
                                          title = "Select a File",
                                          filetypes = (("stl files",
                                                        "*.stl*"),
                                                       ("all files",
                                                        "*.*"),
                                                        ("Text files",
                                                        "*.txt*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)

def popup_window_1():
    pop_1 = Toplevel()

    label = Label(pop_1, text="Angle between Earth and the asteroid")
    label.pack(fill='x', padx=50, pady=5)

    button_close = Button(pop_1, text="Close", command=pop_1.destroy)
    button_close.pack(fill='x')

    canvas3 = Canvas(pop_1, width = 273, height = 100)
    imgp = ImageTk.PhotoImage(Image.open("3.png"))
    canvas3.create_image(0, 0, anchor=NW, image=imgp)
    canvas3.pack()

# Create the root window
window = Tk()

# Set window title
window.title('ILLUMINAT3D')

# Set window size
window.geometry("1000x720")

#window.eval('tk::PlaceWindow . center')

#Set window background color
window.config(background = "white")

#images
canvas1 = Canvas(window, width = 273, height = 100)
img1 = ImageTk.PhotoImage(Image.open("1.png"))
canvas1.create_image(0, 0, anchor=NW, image=img1)

canvas2 = Canvas(window, width = 273, height = 100)
img2 = ImageTk.PhotoImage(Image.open("2.png"))
canvas2.create_image(0, 0, anchor=NW, image=img2)

#Create logo label
logo2 = ImageTk.PhotoImage(Image.open("logo2.png"))
logo_img = Label(window, image = logo2)

# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "Open your 3D model file",
                            width = 100, height = 4,
                            fg = "blue")


info =  PhotoImage(file = r"info.png")
info_button_1 = Button(window,
                     image = info,
                     command = popup_window_1)


button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)

button_exit = Button(window,
                     text = "Exit",
                     command = exit)

button_run = Button(window,
                    text = "Run Program",
                    command = checkInputs)


label_input1 = Label(window,
                    text = "Source-Earth Angle (e.g. 90):",
                    width = 40, height = 3,
                    fg = "blue")
label_input2 = Label(window,
                    text = "Initial Rotation (e.g. 0, 90, 90, 20):",
                    width = 40, height = 3,
                    fg = "blue")
label_input3 = Label(window,
                    text = "Rotation Axis (e.g. 90, 90, 0):",
                    width = 40, height = 3,
                    fg = "blue")
label_input4 = Label(window,
                    text = "Frames:",
                    width = 40, height = 3,
                    fg = "blue")
label_input5 = Label(window,
                    text = "Albedo (from 0 to 1):",
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




logo_img.grid(row=0)

label_file_explorer.grid(row = 1, column=0, columnspan=3)

button_explore.grid(column = 1, row = 2)

info_button_1.grid(column=4, row=4)


label_input1.grid(column = 0, row = 4, sticky = W, pady = 2)
label_input2.grid(column = 0, row = 5, sticky = W, pady = 2)
label_input3.grid(column = 0, row = 6, sticky = W, pady = 2)
canvas1.grid(column = 2, row = 5, sticky = W, pady = 2)
canvas2.grid(column = 2, row = 6, sticky = W, pady = 2)
label_input4.grid(column = 0, row = 7, sticky = W, pady = 2)
label_input5.grid(column = 0, row = 8, sticky = W, pady = 2)

firstVariableEntry.grid(row = 4, column = 1, pady = 2)
secondVariableEntry.grid(row = 5, column = 1, pady = 2)
thirdVariableEntry.grid(row = 6, column = 1, pady = 2)
fourthVariableEntry.grid(row = 7, column = 1, pady = 2)
albedoEntry.grid(row = 8, column = 1, pady = 2)



button_run.grid(column = 1,row = 9)
button_exit.grid(column = 1,row = 10)




window.mainloop()
