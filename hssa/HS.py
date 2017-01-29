# -*- coding: utf-8 -*-
import scipy.io
import numpy as np
import weles

"""
A class to store and to use hypersectral image.
"""
class HS:
    """
    ## Initialization
    """
    def __init__(self, dictionary):
        # Loading image, ground truth and establishing informations.
        self.image = self.loadMatFromTuple(dictionary['image'])
        self.gt = self.loadMatFromTuple(dictionary['gt'])
        self.name = dictionary['name']
        self.classes = dictionary['classes']

        # Getting in shape.
        shape = np.shape(self.image)
        self.rows = shape[0]
        self.cols = shape[1]
        self.bands = shape[2]

        # Searching for maximum value
        self.max = np.amax(self.image)

    ## Operators

    """
    ### Getting sample
    """
    def sample(self, location, learning = True):
        cvLocation = location
        return weles.Sample(self.signature(cvLocation), self.label(cvLocation))

    """
    ### Getting signature
    """
    def signature(self, location):
        return np.copy(self.image[location])

    """
    ### Getting label
    """
    def label(self, location):
        return int(np.copy(self.gt[location]))

    """
    ### Getting slice
    """
    def slice(self, band):
        return np.copy(self.image[:, :, band])

    ## Helper functions
    """
    ## Loading from .mat file
    """
    def loadMatFromTuple(self, entry):
        return scipy.io.loadmat(entry[0])[entry[1]]

    """
    ## Be verbose, man
    """
    def __str__(self):
        return '%s image, %i classes, %i samples of %i bands' % (
            self.name,
            len(self.classes),
            self.rows * self.cols,
            self.bands)
