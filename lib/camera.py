import numpy as np
'''
   In OpenGL (right hand coordinate, camera z direction should be negative
'''

class Camera(object):
    def __init__(self, **kwargs):
        '''
        set default properties
        '''
        self.position = kwargs.get('position', np.array([0, 0, 1]))
        self.lookAt = kwargs.get('lookAt', np.array([0, 0, 0]))
        self.fov = kwargs.get('fov', 90)
        self.near = kwargs.get('near', 0.1)
        self.far = kwargs.get('far', 1000)
        self.up = kwargs.get('up', np.array([0, 1, 0]))

    def viewMatrix(self):
        n =  self.position - self.lookAt
        u = np.cross(self.up, n)
        v = np.cross(n, u)
        rotMatrix = np.matrix([[*u, 0], [*v, 0], [*n, 0], [0, 0, 0, 1]])
        

        transMatrix = np.identity(4)
        transMatrix[0, 3] =  - n[0]
        transMatrix[1, 3] =  - n[1]
        transMatrix[2, 3] =  - n[2] 
        # R * T * Vec == R * (T * Vec)
        # translate first, then rotate
        return rotMatrix * transMatrix 