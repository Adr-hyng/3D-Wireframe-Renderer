import pygame
from math import cos, sin
from Plot.text import Text
from Plot.inputbox import InputBox
from sys import exit

PROJECTION_MATRIX = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]

def drawFaces():
    pass
    # Draw Faces
        # pygame.draw.polygon(self.screen, pygame.color.THECOLORS["red"], [self.cube_edges[0], self.cube_edges[1], self.cube_edges[2], self.cube_edges[3]])
        # pygame.draw.polygon(self.screen, pygame.color.THECOLORS["yellow"], [self.cube_edges[0], self.cube_edges[4], self.cube_edges[5], self.cube_edges[1]])
        # pygame.draw.polygon(self.screen, pygame.color.THECOLORS["orange"], [self.cube_edges[2], self.cube_edges[3], self.cube_edges[7], self.cube_edges[6]])
        # pygame.draw.polygon(self.screen, pygame.color.THECOLORS["pink"], [self.cube_edges[0], self.cube_edges[4], self.cube_edges[7], self.cube_edges[3]])
        # pygame.draw.polygon(self.screen, pygame.color.THECOLORS["blue"], [self.cube_edges[1], self.cube_edges[5], self.cube_edges[6], self.cube_edges[2]])
        # pygame.draw.polygon(self.screen, pygame.color.THECOLORS["green"], [self.cube_edges[4], self.cube_edges[5], self.cube_edges[6], self.cube_edges[7]])

def dotProduct(matrix_a, matrix_b):
    # Inefficient, only implemented for educational purposes.
    # Use Numpy matrix and dot product or matrix multiplication
    a_rows = len(matrix_a)
    a_columns = len(matrix_a[0])
    
    b_rows = len(matrix_b)
    b_columns = len(matrix_b[0])
    
    product = [[0 for _ in range(b_columns)] for _ in range(a_rows)]
    
    if a_columns == b_rows:
        for i in range(a_rows):
            for j in range(b_columns):
                for k in range(b_rows):
                    product[i][j] += matrix_a[i][k] * matrix_b[k][j]
    else:
        print("Invalid Matrix Size")
    return product

def addOffset(index, points, offset) -> list[list[list[int]]]:
    for i, point in enumerate(points):
        points[i][index][0] = point[index][0] + offset
    return points

def connect_edges(screen, i: int, j: int, edges, thickness: int = 1):
    pygame.draw.line(screen, pygame.color.THECOLORS["black"], (edges[i][0], edges[i][1]), (edges[j][0], edges[j][1]), thickness)
        
def get_xrot_matrix(theta: int = 0):
    return [[1, 0, 0],
            [0, cos(theta), -sin(theta)],
            [0, sin(theta), cos(theta)]]

def get_yrot_matrix(theta: int = 0):
    return [[cos(theta), 0, sin(theta)],
            [0, 1, 0],
            [-sin(theta), 0, cos(theta)]]

def get_zrot_matrix(theta: int = 0):
    return [[cos(theta), -sin(theta), 0],
            [sin(theta), cos(theta), 0],
            [0, 0, 1]]

class Shapes:
    def getCustomPoints(self, offset: pygame.Vector3):
        #? To-Do (No Promise): Get points from file or temporary database and then return, instead of copying
        return [[[-8 + offset.x], [0 + offset.z], [6 + offset.y]], [[-1 + offset.x], [0 + offset.z], [13 + offset.y]], [[2 + offset.x], [0 + offset.z], [13 + offset.y]], [[9 + offset.x], [0 + offset.z], [6 + offset.y]], [[4 + offset.x], [0 + offset.z], [6 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]], [[-2 + offset.x], [0 + offset.z], [3 + offset.y]], [[-2 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[-4 + offset.x], [0 + offset.z], [0 + offset.y]], [[-4 + offset.x], [0 + offset.z], [6 + offset.y]], [[9 + offset.x], [0 + offset.z], [6 + offset.y]], [[-7 + offset.x], [0 + offset.z], [6 + offset.y]]]
    
    def getPyramid(self, offset: pygame.Vector3):
        """
        Edges:
        connect_edges(self.screen, 0, 1, self.column_cubes[-1].edges)
        connect_edges(self.screen, 1, 2, self.column_cubes[-1].edges)
        connect_edges(self.screen, 2, 3, self.column_cubes[-1].edges)
        connect_edges(self.screen, 3, 4, self.column_cubes[-1].edges)
        connect_edges(self.screen, 0, 3, self.column_cubes[-1].edges)
        connect_edges(self.screen, 1, 4, self.column_cubes[-1].edges)
        connect_edges(self.screen, 2, 4, self.column_cubes[-1].edges)
        connect_edges(self.screen, 0, 4, self.column_cubes[-1].edges)
        """
        return [
            [[-1 + offset.x], [-1 + offset.z], [1 + offset.y]], 
            [[1 + offset.x], [-1 + offset.z], [1 + offset.y]], 
            [[1 + offset.x], [1 + offset.z], [1 + offset.y]], 
            [[-1 + offset.x], [1 + offset.z], [1 + offset.y]], 
            [[0 + offset.x], [0 + offset.z], [3 + offset.y]]
            ]
    def getCube(self, offset: pygame.Vector3):
        """
        Edges:
        for point in range(4):
            connect_edges(self.screen, point, (point + 1) % 4, self.cube_edges)
            connect_edges(self.screen, point + 4, ((point + 1) % 4) + 4, self.cube_edges)
            connect_edges(self.screen, point, (point + 4), self.cube_edges)
            
        Note: At the Draw method of Solid class
        """
        return [
            [[-1 + offset.x], [-1], [1 + offset.y]], 
            [[1 + offset.x], [-1], [1 + offset.y]], 
            [[1 + offset.x], [1], [1 + offset.y]], 
            [[-1 + offset.x], [1], [1 + offset.y]], 
            [[-1 + offset.x], [-1], [-1 + offset.y]], 
            [[1 + offset.x], [-1], [-1 + offset.y]], 
            [[1 + offset.x], [1], [-1 + offset.y]], 
            [[-1 + offset.x], [1], [-1 + offset.y]]
            ]
    
    def getRocket(self, offset: pygame.Vector3):
        return [
            [[0 + offset.x], [0 + offset.z], [2 + offset.y]],
            [[2 + offset.x], [-2 + offset.z], [0 + offset.y]],
            [[-2 + offset.x], [-2 + offset.z], [0 + offset.y]],
            [[-2 + offset.x], [2 + offset.z], [0 + offset.y]],
            [[2 + offset.x], [2 + offset.z], [0 + offset.y]],
            
            [[-1 + offset.x], [-1 + offset.z], [0 + offset.y]],
            [[-1 + offset.x], [1 + offset.z], [0 + offset.y]],
            [[1 + offset.x], [1 + offset.z], [0 + offset.y]],
            [[1 + offset.x], [-1 + offset.z], [0 + offset.y]],
            
            [[-1 + offset.x], [-1 + offset.z], [-4 + offset.y]],
            [[-1 + offset.x], [1 + offset.z], [-4 + offset.y]],
            [[1 + offset.x], [1 + offset.z], [-4 + offset.y]],
            [[1 + offset.x], [-1 + offset.z], [-4 + offset.y]]
        ]
    
    def getDPyramid(self, offset: pygame.Vector3):
        return [
            [[0 + offset.x], [0 + offset.z], [2 + offset.y]],
            [[2 + offset.x], [-2 + offset.z], [0 + offset.y]],
            [[-2 + offset.x], [-2 + offset.z], [0 + offset.y]],
            [[-2 + offset.x], [2 + offset.z], [0 + offset.y]],
            [[2 + offset.x], [2 + offset.z], [0 + offset.y]],
            [[0 + offset.x], [0 + offset.z], [-2 + offset.y]]
        ]
    
    def getWord(self, letter: str, offset: pygame.Vector3):
        # format: X: Right, Z-Forward, Y-Above
        alphabets = {
            "A": [[[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[3 + offset.x], [0 + offset.z], [2 + offset.y]], [[1 + offset.x], [0 + offset.z], [2 + offset.y]], [[2 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "B": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [3 + offset.y]], [[3 + offset.x], [0 + offset.z], [2 + offset.y]], [[0 + offset.x], [0 + offset.z], [2 + offset.y]], [[3 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "C": [[[3 + offset.x], [0 + offset.z], [4 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]], [[0 + offset.x], [0 + offset.z], [1 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [1 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [3 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "D": [[[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [3 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "E": [[[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[1 + offset.x], [0 + offset.z], [2 + offset.y]], [[3 + offset.x], [0 + offset.z], [2 + offset.y]], [[1 + offset.x], [0 + offset.z], [2 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "F": [[[3 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [2 + offset.y]], [[3 + offset.x], [0 + offset.z], [2 + offset.y]], [[0 + offset.x], [0 + offset.z], [2 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "G": [[[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]], [[0 + offset.x], [0 + offset.z], [1 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[4 + offset.x], [0 + offset.z], [2 + offset.y]], [[3 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [1 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "H": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [2 + offset.y]], [[0 + offset.x], [0 + offset.z], [2 + offset.y]]],
            "I": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "J": [[[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [1 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]]],
            "K": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [2 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]], [[1 + offset.x], [0 + offset.z], [2 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "L": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "M": [[[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "N": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]]],
            "O": [[[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[4 + offset.x], [0 + offset.z], [3 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]], [[0 + offset.x], [0 + offset.z], [1 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]]],
            "P": [[[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [3 + offset.y]], [[3 + offset.x], [0 + offset.z], [2 + offset.y]], [[1 + offset.x], [0 + offset.z], [2 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "Q": [[[0 + offset.x], [0 + offset.z], [1 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [3 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [0 + offset.y]], [[3 + offset.x], [0 + offset.z], [1 + offset.y]], [[2 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [1 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]]], 
            "R": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [3 + offset.y]], [[3 + offset.x], [0 + offset.z], [2 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]], [[1 + offset.x], [0 + offset.z], [2 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "S": [[[1 + offset.x], [0 + offset.z], [2 + offset.y]], [[3 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[3 + offset.x], [0 + offset.z], [2 + offset.y]], [[1 + offset.x], [0 + offset.z], [2 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[1 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]]],
            "T": [[[2 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [3 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [4 + offset.y]]],
            "U": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [3 + offset.y]]],
            "V": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [0 + offset.y]]],
            "W": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [1 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[3 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [1 + offset.y]], [[1 + offset.x], [0 + offset.z], [0 + offset.y]]],
            "X": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]]],
            "Y": [[[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]], [[2 + offset.x], [0 + offset.z], [0 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[2 + offset.x], [0 + offset.z], [2 + offset.y]]],
            "Z": [[[0 + offset.x], [0 + offset.z], [3 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [1 + offset.y]], [[4 + offset.x], [0 + offset.z], [0 + offset.y]], [[0 + offset.x], [0 + offset.z], [0 + offset.y]], [[4 + offset.x], [0 + offset.z], [4 + offset.y]], [[0 + offset.x], [0 + offset.z], [4 + offset.y]]]
        }
        return alphabets.get(letter)
        
class Rotation:
    def __init__(self):
        self.x, self.y, self.z = None, None, None
        
class Solid:
    def __init__(self, screen, size, _cube_vertices, _cube_edges):
        self.screen = screen
        self.size = size
        self.vertices = _cube_vertices
        self.edges = _cube_edges
        self.rotation = Rotation()
        self.text = Text(self.screen, "red")
    
    def draw(self, angle, position, size, debug = False):
        self.size = size
        
        for index, vertex in enumerate(self.vertices):
            self.rotation.x = dotProduct(get_xrot_matrix(angle.x), vertex)
            self.rotation.y = dotProduct(get_yrot_matrix(angle.y), self.rotation.x)
            
            transformed_vertex = dotProduct(PROJECTION_MATRIX, self.rotation.y)
            
            x = (transformed_vertex[0][0] * self.size) + (self.screen.get_size()[0] / 2) + position.x
            y = (transformed_vertex[1][0] * self.size) + (self.screen.get_size()[0] / 2) + position.y
            self.edges[index] = (x, y)
            pygame.draw.circle(self.screen, pygame.color.THECOLORS["black"], (x, y), 1)
            if debug: self.text.Insert(20, index, x, y - 10, False, True)
        

class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.font.init()
        pygame.init()

        self.initialize_screen("Setup", 600, 600)

    def initialize_screen(self, title: str, width: int, height: int):
        self.window_size = (width, height)
        self.screen = pygame.display.set_mode(self.window_size, 0, 32)
        self.display = pygame.Surface((width // 2, height // 2))
        pygame.display.set_caption(title)

    def screen_background(self, color: str):
        self.screen.fill(pygame.color.THECOLORS[color])

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
                
            self.input_box.handle_event(event)
                
    def key_input(self):
        keys = pygame.key.get_pressed()
        
        # Rotation
        if keys[pygame.K_PAGEDOWN]:
            self.angle.x += 5 * self.dt
        if keys[pygame.K_PAGEUP]:
            self.angle.x -= 5 * self.dt
        if keys[pygame.K_HOME]:
            self.angle.y += 5 * self.dt
        if keys[pygame.K_END]:
            self.angle.y -= 5 * self.dt
            
        # Rotation of Cube
        if keys[pygame.K_s]:
            self.box_angle.x += 5 * self.dt
        if keys[pygame.K_w]:
            self.box_angle.x -= 5 * self.dt
        if keys[pygame.K_a]:
            self.box_angle.y += 5 * self.dt
        if keys[pygame.K_d]:
            self.box_angle.y -= 5 * self.dt
        
        # Zoom Main
        if keys[pygame.K_z]:
            self.focal_length += 25 * self.dt
        if keys[pygame.K_x]:
            self.focal_length -= 25 * self.dt
            
        # Moving
        if keys[pygame.K_RIGHT]:
            self.position.x += 200 * self.dt
        if keys[pygame.K_LEFT]:
            self.position.x -= 200 * self.dt
        if keys[pygame.K_DOWN]:
            self.position.y += 200 * self.dt
        if keys[pygame.K_UP]:
            self.position.y -= 200 * self.dt
    
    def initialize_code(self):
        self.text = Text(self.screen, "black")
        self.input_box = InputBox(200, 500, 140, 30, "")
        self.focal_length = 20
        
        self.angle = pygame.Vector3(0, 0, 0)
        self.position = pygame.Vector2(0, 0)
        self.offset = pygame.Vector3(0, 0, 0)
        
        self.solid_objects: list[Solid] = []
        self.shape = Shapes()
        cube = self.shape.getRocket(pygame.Vector3(0, 0, 0))
        # cube = self.shape.getCube(pygame.Vector2(0, 0))
        self.box_angle = pygame.Vector3(0, 0, 0)
        self.box_multiplier = 5
        self.box = Solid(self.screen, self.focal_length * self.box_multiplier, cube, [0 for _ in range(len(cube))])
            
        
    def loop_block(self):
        self.input_box.update()

    def rendering_screen(self):
        for _object in self.solid_objects:
            _object.draw(self.angle, self.position, self.focal_length)
            
        for cube in self.solid_objects:
            for i in range(len(cube.vertices)):
                connect_edges(self.screen, i, (i+1) % len(cube.edges), cube.edges, 3)
        
        self.box.draw(self.box_angle, pygame.Vector2(0, 0), self.focal_length * self.box_multiplier, False)
        
        connect_edges(self.screen, 0, 1, self.box.edges)
        connect_edges(self.screen, 1, 2, self.box.edges)
        connect_edges(self.screen, 2, 3, self.box.edges)
        connect_edges(self.screen, 3, 4, self.box.edges)
        connect_edges(self.screen, 0, 2, self.box.edges)
        connect_edges(self.screen, 0, 3, self.box.edges)
        connect_edges(self.screen, 0, 4, self.box.edges)
        connect_edges(self.screen, 1, 4, self.box.edges)
        connect_edges(self.screen, 6, 10, self.box.edges)
        connect_edges(self.screen, 5, 9, self.box.edges)
        connect_edges(self.screen, 8, 12, self.box.edges)
        connect_edges(self.screen, 7, 11, self.box.edges)
        connect_edges(self.screen, 9, 10, self.box.edges)
        connect_edges(self.screen, 10, 11, self.box.edges)
        connect_edges(self.screen, 11, 12, self.box.edges)
        connect_edges(self.screen, 12, 9, self.box.edges)
        connect_edges(self.screen, 1, 8, self.box.edges)
        connect_edges(self.screen, 2, 5, self.box.edges)
        connect_edges(self.screen, 7, 4, self.box.edges)
        connect_edges(self.screen, 6, 3, self.box.edges)
        
        # for i in range(len(self.box.edges)):
            # connect_edges(self.screen, i, (i+1) % len(self.box.edges), self.box.edges, 3)
            
        # for i in range(4):
        #     connect_edges(self.screen, i, (i + 1) % 4, self.box.edges, 2)
        #     connect_edges(self.screen, i + 4, ((i + 1) % 4) + 4, self.box.edges, 2)
        #     connect_edges(self.screen, i, (i + 4), self.box.edges, 2)
            
        if self.input_box.entered:
            if self.solid_objects: self.solid_objects = []
            spacing = 6
            self.word = self.input_box.text.upper()
            self.input_box.reset()
            
            spacing = 5
            for letter in self.word:
                if letter.isspace():
                    spacing = 3
                else:
                    vertices = self.shape.getWord(letter, self.offset)
                    self.solid_objects.append(Solid(self.screen, self.focal_length, vertices, [0 for _ in range(len(vertices))]))
                    spacing = 5
                self.offset.x += spacing
        
        self.text.Insert(30, "ENTER STRING", self.input_box.rect.left, self.input_box.rect.top - self.input_box.rect.height, False, True)
        self.input_box.draw(self.screen)
        
    def update_screen(self):
        pygame.display.update()
        self.dt = self.clock.tick(self.fps) / 1000

    def Run(self):
        self.fps = 60
        self.dt = self.clock.tick(self.fps) / 1000
        self.running = True
        self.initialize_code()

        while self.running:
            self.screen_background('white')
            self.event_handling()
            self.key_input()

            self.loop_block()
            self.rendering_screen()
            self.update_screen()

        pygame.quit()

if __name__ == '__main__':
    Main().Run()
