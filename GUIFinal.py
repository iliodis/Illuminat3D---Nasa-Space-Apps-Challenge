from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os


from Illuminated_Class_Git_1 import Illuminated


#In this function we check if the variables are valid



# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),
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

    pop_1.title('Angle between Earth and the asteroid')

    h1 = Label(pop_1, text='Fun Fact!', font='Helvetica')
    h1.pack(pady=5)

    label1 = Label(pop_1,
                  text= 'Lucy is the first space mission that will study the trojan asteroids,\n o group of asteroids that leads and follows Jupiter in it’s orbit.\n The mission will launch in October 2021.\n If you want to explore the light curves of the trojans,\n make sure to enter the 3D model of a trojan asteroid,\n and to not exceed the point of 11o in this field,\n as it is not possible to observe them in greater angles,\n due to the geometry of the Earth’s and Jupiter’s orbits.')
    label1.pack(fill='x', padx=5, pady=5)

    button_close = Button(pop_1, text="Close", command=pop_1.destroy)
    button_close.pack(pady=50)

def popup_window_2():
    pop_2 = Toplevel()

    pop_2.title('But what is Albedo?')

    h2 = Label(pop_2, text='Fun Fact!', font='Helvetica')
    h2.pack(pady=5)

    label2 = Label(pop_2,
                  text= 'Albedo is the measure of the diffuse reflection of\n solar radiation out of the total solar radiation.\n It is measured on a scale from 0, corresponding to a black body\n that absorbs all incident radiation, to 1,\n corresponding to a body that reflects all incident radiation.')
    label2.pack(fill='x', padx=5, pady=5)

    button_close = Button(pop_2, text="Close", command=pop_2.destroy)
    button_close.pack(pady=50)



# Create the root window
window = Tk()

# Set window title
window.title('ILLUMINAT3D')

# Set window size
window.geometry("1280x720")

#window.eval('tk::PlaceWindow . center')

#Set window background color
window.config(background = "white")

#images
canvas1 = Canvas(window, width = 273, height = 100)
img1 = ImageTk.PhotoImage(Image.open("Initial Rotation.png"))
canvas1.create_image(0, 0, anchor=NW, image=img1)

canvas2 = Canvas(window, width = 273, height = 100)
img2 = ImageTk.PhotoImage(Image.open("Rotation Axis.png"))
canvas2.create_image(0, 0, anchor=NW, image=img2)

canvas3 = Canvas(window, width = 273, height = 100)
img3 = ImageTk.PhotoImage(Image.open("Source-Earth angle.png"))
canvas3.create_image(0, 0, anchor=NW, image=img3)


#Create logo label
logo2 = ImageTk.PhotoImage(Image.open("logo1.png"))
logo_img = Label(window, image = logo2)

# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "In this field you can enter the 3D model that you want to study. You can pick one from the NASA’s library, that can be found in this link: https://echo.jpl.nasa.gov/asteroids/shapes/shapes.html .\n You can, also, choose to enter your own 3D model of an asteroid, a basic geometric shape, or everything that you can possibly imagine, but make sure that you upload an “.stl” file.",
                            fg = "blue")


info =  PhotoImage(file = r"info.png")
info_button_1 = Button(window,
                     image = info,
                     command = popup_window_1)

info_button_2 = Button(window,
                     image = info,
                     command = popup_window_2)





button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)

button_exit = Button(window,
                     text = "Exit",
                     command = exit,
                     fg = "red")

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

    print(label_file_explorer.cget("text").split("/")[-1])
    obj = Illuminated(label_file_explorer.cget("text").split("/")[-1], inititalRotation, rotationAxis, int(frames.get()), float(albedo.get()), float(omega.get()))
    x_axis, y_axis = obj.execution()

    matplotlib.use("TkAgg")
    figure = Figure(figsize=(4, 4), dpi=100)

    # Define the points for plotting the figure
    plot = figure.add_subplot(1, 1, 1)
    plot.plot(0.5, 0.3, color="blue", marker="o", linestyle="")

    # Define Data points for x and y axis
    plot.plot(x_axis, y_axis, color="red", marker=".", linestyle="")

    # Add a canvas widget to associate the figure with canvas
    canvas = FigureCanvasTkAgg(figure, window)
    canvas.get_tk_widget().grid(row=6, column=5)

button_run = Button(window,
                    text = "Run Program",
                    command = checkInputs)


label_input1 = Label(window,
                    text = "Source-Earth Angle (e.g. 90):",
                    width = 60, height = 3,
                    fg = "blue")
label_input2 = Label(window,
                    text = "Initial Rotation (e.g. 0, 90, 90, 20):",
                    width = 60, height = 3,
                    fg = "blue")
label_input3 = Label(window,
                    text = "Rotation Axis (e.g. 90, 90, 0):",
                    width = 60, height = 3,
                    fg = "blue")
label_input4 = Label(window,
                    text = "Frames:",
                    width = 60, height = 3,
                    fg = "blue")
label_input5 = Label(window,
                    text = "Albedo (from 0 to 1):",
                    width = 60, height = 3,
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




logo_img.grid(column=1, row=0)

label_file_explorer.grid(row = 2, column=0, columnspan=4)

button_explore.grid(column = 1, row = 3)

info_button_1.grid(column=3, row=4)
info_button_2.grid(column=3, row=5)

label_input1.grid(column = 0, row = 4, sticky = W, pady = 2)
label_input2.grid(column = 0, row = 8, sticky = W, pady = 2)
label_input3.grid(column = 0, row = 6, sticky = W, pady = 2)
canvas1.grid(column = 2, row = 8, sticky = W, pady = 2)
canvas2.grid(column = 2, row = 6, sticky = W, pady = 2)
canvas3.grid(column = 2, row = 4, sticky = W, pady = 2)
label_input4.grid(column = 0, row = 7, sticky = W, pady = 2)
label_input5.grid(column = 0, row = 5, sticky = W, pady = 2)

firstVariableEntry.grid(row = 4, column = 1, pady = 2)
secondVariableEntry.grid(row = 8, column = 1, pady = 2)
thirdVariableEntry.grid(row = 6, column = 1, pady = 2)
fourthVariableEntry.grid(row = 7, column = 1, pady = 2)
albedoEntry.grid(row = 5, column = 1, pady = 2)



button_run.grid(column = 1,row = 9)
button_exit.grid(column = 1,row = 10)




window.mainloop()
