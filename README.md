# Illuminat3D---Nasa-Space-Apps-Challenge
This project participates in the Nasa Space Apps Challenge 2021.
# Documentation of the Illuminat3d App
# Version 1.0

The main scope of this application is to plot the light curve of an asteroid for certain values of the input variables. The project consists of two .py files (<name_of_the_gui_file>.py and <name_of_the_illuminated_class>.py).

## <name_of_the_gui_file>.py file
This is the file that we create the **User Interface** (**UI**) of our application. It have a space that the user load his 3D model (*.stl* file format). Then the user must fill in every enrty of the variables in the right form and finally push the **Run Program** button to see the light curve plot in the corresponding window. The User Interface except all the widgets (***Button***, ***Label***, ***Entry***, ***Images***) has and 3 functions:
* **browseFiles()**: in this function we set the directory that the application can search to find the user's 3D model. When a file is selected then the label of the file explorer change text to specify the path of the file.
* **popup_window_1()**: function that triggered when the info button is pressed and pops out an information message.
* **checkInputs()**: in this function we check the validity of the input variables and then create an **Illuminated** object to start running the main program.


## <name_of_the_illuminated_class>.py file
In this file we create a **class Illuminated** to control the core of our program and to plot the **light curves** of the input 3D models. This class has several functions to produce the expected output.
* **__ init__(self, filename, initRot, rotAxis, frames, albedo, omega)**: is the contructor of the class which assigns the proper values to the class variables. It recieves as inputs the filename of the 3D model(**filename**), the initial rotation axis and angle (**initRot**), the rotational axis (**rotAxis**), the number of frames (**frames**), the albedo (**albedo**) and the omega angle(**omega**).
* **checkTheModel(self)**: this function check if the 3D model that the user inserted is valid(**close object**). Return boolean value **True** or **False**.
* **computeIntersectionsAreas(self, multi)**: recieves a **Multipolygon** object and returns its total area.
* **multColumns(self, col1, col2)**: recieves two arrays and produce a new one of the same length. Each element of this array is the multiplication of the two initial arrays' corresponding elements (i.e. new_col[5] = col1[5]*col2[5])
* **sortCoords(self, arr, ind)**: this is an extra function which sorts the rows of the 2D **arr** array under the 1D **index** array.
* **sortDist(self, arr, ind)**: this is an extra function which sorts the values of the 1D **arr** array under the 1D **index** array. 
* **desortDist(self, arr, ind)**: with this function we de-sort the **distances** array back to its initial structure.
* **computeCoefs(self, coords, dist, dots)**: compute the **coefficients** array depending on the coordinates, distances and dots arrays. By taking one triangle at a time we compute the area of each triangle that is seen by the viewer.
* **n_vec(self, tha, thb, thc)**: return a normalized vector as the cosines of the given angles **tha**, **thb**, **thc**. Each input is the angle that this vector forms with the corresponding axix (x, y, z).
* **v_surf(self, cube ,n_v)**: return the viewing surface when looking in the **n_v** direction (either as the source or as the viewer).
* **execution(self)**: in this function we calibrate the model with its rotation and the position of the light and the viewer and we plot the asteroid's light curve. The number of the plot's points is implied by the number of *frames*.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary libraries.

```bash
pip install python-math
pip install numpy-stl
pip install matplotlib
pip install tk
pip install shapely
```

## Execution

After you download the project in your computer, you must move to the directory that the python files are and run the command below.

```python
python <name_of_the_gui_file>.py
```

## Members
1. Doli Maria
2. Eleftheriadis Emmanouil
3. Komitis Dimitrios
4. Liodis Ioannis
5. Noula Konstantina
6. Rodiou Eirini

README.md
4 KB
