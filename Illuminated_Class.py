# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 16:45:05 2021

@author: You
"""


import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
import math
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon

class Illuminated:

    def __init__(self, filename, initRot, rotAxis, frames, albedo, omega):
        self.initialRot = initRot
        self.rotationAxis = rotAxis
        self.frames = frames
        self.albedo = albedo
        self.omegaAngle = omega
        self.cube = mesh.Mesh.from_file(filename)
        


    def checkTheModel(self):
        if self.cube.is_closed():
            return True
        else:
            return False
    


    def computeIntersectionsAreas(self, multi):
        total_area = 0
        polygons = list(multi)
        for poly in polygons:
            total_area += poly.area
        return total_area


    def multColumns(self, col1, col2):
        out = np.zeros(col1.shape[1])
        for i in range(col1.shape[1]):
            out[i] = col1[0][i] * col2[0][i]
        return np.reshape(out, (1, col1.shape[1]))


    #Sorting the matrix arr by increasing values
    def sortCoords(self, arr, ind):
        out = np.zeros((arr.shape[0], arr.shape[1]))
        for i in range(len(arr)):
            for j in range(6):
                out[i][j] = arr[ind[0][i]][j]
        return out


    #Sorting the matrix arr by increasing values
    def sortDist(self, arr, ind):
        return arr[0][ind]

    #Desorting the matrix arr
    def desortDist(self, arr,ind):
        return arr[0][np.argsort(ind)].T
        
        




    def computeCoefs(self, coords, dist, dots):
        coefs = np.zeros(len(dist))

        #We sort the distances array
        temp = np.argsort(dist.T)
        sorted_coords = self.sortCoords(coords, temp)
        sorted_dist = self.sortDist(dist.T, temp)
        sorted_dots = self.sortDist(dots.T, temp).T
        
        one = (sorted_coords[0][0], sorted_coords[0][1])
        two = (sorted_coords[0][2], sorted_coords[0][3])
        three = (sorted_coords[0][4], sorted_coords[0][5])
        big_poly = Polygon([one, two, three])
        
        
        
        coefs[0] = 1
        
        for i in range(1, sorted_dist.shape[1]):
            if sorted_dots[i][0] == 0:
                coefs[i] = 0
            else:
                #We create the three points of the traingles
                one = (sorted_coords[i][0], sorted_coords[i][1])
                two = (sorted_coords[i][2], sorted_coords[i][3])
                three = (sorted_coords[i][4], sorted_coords[i][5])
                poly = Polygon([one, two, three]) # Trinagle creation
                




                if poly.area > 0.0000000001 and big_poly.overlaps(poly):
                    if big_poly.geom_type == 'Polygon' and big_poly.intersection(poly).geom_type == 'Polygon':
                        coefs[i] = 1 - (big_poly.intersection(poly).area/poly.area) #The percentage of area
                    elif big_poly.geom_type == 'MultiPolygon' and big_poly.intersection(poly).geom_type =='MultiPolygon':
                        coefs[i] = 1 - (self.computeIntersectionsAreas(big_poly.intersection(poly))/poly.area)
                    elif big_poly.geom_type == 'MultiPolygon' and big_poly.intersection(poly).geom_type =='Polygon':
                        coefs[i] = 1 - (big_poly.intersection(poly).area/poly.area) #The percentage of area
                elif poly.area > 0.0000000001:
                    coefs[i] = 1
                else:
                    coefs[i] = 0



                if poly.area > 0.0000000001:
                    big_poly = big_poly.union(poly) #The union of the two areas
        
                
        
        

        
            
        return self.desortDist(np.reshape(coefs, (1, coefs.shape[0])), temp)


    #Normal function from given angles
    def n_vec(self, tha,thb,thc):
        a = math.radians(tha)
        b = math.radians(thb)
        c = math.radians(thc)
        n_vec = (math.cos(a),math.cos(b),math.cos(c))
        n_unit = n_vec/np.linalg.norm(n_vec)
        return n_unit



    #Viewing surfaces function (either from source or from viewer)
    def v_surf(self, cube,n_v): 
        #Initial arrays
        unit_normals = cube.get_unit_normals()
        centroids = np.zeros((len(cube.points),3))
        dot_products = np.zeros((len(cube.points),1))
        distances = np.zeros((len(cube.points),1))
        coord_2d = np.zeros((len(cube.points),6))
        coef = np.ones((len(cube.points),1))              #This will be the return
        
        
        #2D plane basis vectors
        e_1 = np.array((0,0,1))
        e_2 = np.cross(n_v,e_1)
        
        
        
        for j in range(len(cube.points)):
            
            
            #Dot products n_v * unit_normals and KEEP THE VIEWING
            dot = -np.dot(n_v,unit_normals[j])
            if dot > 0.000000001:
                dot_products[j] = dot
            else:
                dot_products[j] = 0

            
        
            #Finding the centroid of each triangle
            centroids[j,0] = (cube.points[j,0] + cube.points[j,3] + cube.points[j,6])/3
            centroids[j,1] = (cube.points[j,1] + cube.points[j,4] + cube.points[j,7])/3
            centroids[j,2] = (cube.points[j,2] + cube.points[j,5] + cube.points[j,8])/3



            #Finding the distances from the viewing plane(coordinate n_v)
            distances[j] = np.dot(n_v,centroids[j])
            
        
        
        
        
            #Finding the projected coordinates of the cube's points (equivalently the other two coordinates)
            coord_2d[j,0] = np.dot(e_1,cube.points[j,0:3])
            coord_2d[j,1] = np.dot(e_2,cube.points[j,0:3])
            
            coord_2d[j,2] = np.dot(e_1,cube.points[j,3:6])
            coord_2d[j,3] = np.dot(e_2,cube.points[j,3:6])
            
            
            coord_2d[j,4] = np.dot(e_1,cube.points[j,6:9])
            coord_2d[j,5] = np.dot(e_2,cube.points[j,6:9])

        
        
        #Manolis programming stuff
        coef = self.computeCoefs(coord_2d,distances, dot_products)
        return coef,dot_products

    
    def execution(self):
        #Irrelevant stuff/properties
        #scale = 2*self.cube.points.flatten()
        volume, cog, inertia = self.cube.get_mass_properties()
        albedo = self.albedo * np.ones((1,len(self.cube.points)))
        I=1.0


        #Light and viewing direction (Always on the xy plane)
        tha_light = self.omegaAngle
        thb_light = 90 - tha_light


        n_light = self.n_vec(tha_light,thb_light,90)



        """DEBUGED"""
        n_view = np.array((-1,0,0))        #Fixed by principle 



        #Rotating axis direction n_rot
        tha_rot = self.rotationAxis[0]
        thb_rot = self.rotationAxis[1]
        thc_rot = self.rotationAxis[2]

        n_rot = self.n_vec(tha_rot,thb_rot,thc_rot)



        #Initial Rotation??
        tha_in_rot = self.initialRot[0]
        thb_in_rot = self.initialRot[1]
        thc_in_rot = self.initialRot[2]
        in_rot_angle = self.initialRot[3]

        n_in_rot = self.n_vec(tha_in_rot,thb_in_rot,thc_in_rot)
        self.cube.rotate(n_in_rot,theta=math.radians(in_rot_angle),point=cog)


        f = self.frames





        x_axis = []
        y_axis = []
        print('The brightness: ')
        #Rotating around arbitrary n_rot (Angular momentum)
        for i in range(f):
            self.cube.rotate(n_rot,theta=math.radians(360.0/f),point=cog)
            """
            figure = plt.figure()
            axes = mplot3d.Axes3D(figure)
            axes.add_collection3d(mplot3d.art3d.Poly3DCollection(cube.vectors))
            axes.auto_scale_xyz(scale, scale, scale)
            plt.show()
            """
            

            
            
            #Getting the coef matrix and the dot_products for the viewer
            viewer_mat,view_dots = self.v_surf(self.cube,n_view)
            
            
            #Getting the coef matrix and the dot_products for the source
            source_mat,source_dots = self.v_surf(self.cube,n_light)
            
            #Combining the two matrices
            final_mat = self.multColumns(np.reshape(viewer_mat, (1, len(viewer_mat))),np.reshape(source_mat, (1, len(source_mat))))
            
            
            #Finding the TOTAL RADIANCE!!!
            L = (I / math.pi) * self.multColumns(self.multColumns(view_dots.T,source_dots.T),albedo)
            I_final = self.multColumns(self.multColumns(L,self.cube.areas.T),final_mat)
            y_axis.append(np.sum(I_final[0]))
            print(np.sum(I_final[0]))
            x_axis.append((i+1)/f)            
            


        plt.style.use('seaborn')
        plt.scatter(x_axis, y_axis,
                        marker= '.', label = 'No initial rotation')
        plt.legend(loc = 1)
        plt.xlabel('Rotational Phase')
        plt.ylabel('Light (Geometric Units)')
        plt.title('Light Curve: Cube')
        plt.show()
        



obj = Illuminated("cube.stl", [0, 90, 90, 45], [90, 90, 0], 10, 1, 270)
obj.execution()