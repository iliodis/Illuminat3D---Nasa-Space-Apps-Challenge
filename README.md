# Illuminat3D---Nasa-Space-Apps-Challenge
This project participates in the Nasa Space Apps Challenge 2021.
# Documentation of the Illuminat3d App
# Version 1.0

The main scope of this application is to plot the light curve of an asteroid for a certain values of the input variables. The project consists of two .py files (<name_of_the_gui_file>.py and <name_of_the_illuminated_class>.py).

## <name_of_the_gui_file>.py file
This is the file that we create the **User Interface** (**UI**) of our application. It have a space that the user load his 3D model (*.stl* file format). Then the user must fill in every enrty of the variables in the right form and finally hit the **Run Program** button to see the light curve plot in the window. The User Interface except all the widgets (***Button***, ***Label***, ***Entry***, ***Images***) has and 3(?? Αυτό πιθανότατα να είναι μεγαλύερο ανάλογα το τελικό πρόγραμμα) functions:
* **browseFiles()**: in this function we set the directory that the application can search to find the user his file with the 3D model. When a file is selected then the label of the file explorer change text to psecify the path of the file.
* **popup_window_1()**: function that triggered when the info button is pressed and pop up a information message.
* **checkInputs()**: in this function we check the validity of the input variables and then create a **Illuminated** object to start running the main program.
