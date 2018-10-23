# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 01:02:47 2018

Exercise 1

In this case study, we will analyze a dataset consisting of an assortment of 
wines classified as "high quality" and "low quality" and will use the k-Nearest 
Neighbors classifier to determine whether or not other information about the
wine helps us correctly predict whether a new wine will be of high quality.

Our first step is to import the dataset.

@author: Dimitris
"""

import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/mitselec/PyWine/master/wine.csv")