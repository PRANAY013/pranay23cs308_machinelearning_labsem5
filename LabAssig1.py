# Posted Aug 7
# Assigned
# Learning Outcomes:
# * Load and explore the Iris dataset
# * Visualize features using pairplots
# * Train and test a KNN classifier
# * Connect distance-based learning to vector space
# * Relate classification results to class probabilities

# Activities:
# Setup (15 mins)
# * Launch Jupyter or Colab
# * Import required libraries

# Data Exploration (30 mins)
# * Load and inspect the Iris dataset
# * Plot class distribution, use seaborn pairplots

# Model Building (45 mins)
# * Split data into training/testing
# * Train a K-Nearest Neighbors (KNN) model
# * Test with different k values (1, 3, 5, 7)
# * Evaluate accuracy

# Wrap-up and Sharing (30 mins)
# * Document model results
# * Push notebook to GitHub with README summary


# - - -



# Lab Assignment 1: Iris Dataset Exploration and KNN Classification

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# sk learn dependencies
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


