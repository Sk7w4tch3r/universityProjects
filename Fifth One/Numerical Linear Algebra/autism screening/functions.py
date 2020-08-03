from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.neighbors import NearestNeighbors
from scipy.stats import pearsonr
import numpy as np
import pandas as pd
import bct


def correlation(df):
    dataf = df.corr(method='pearson')
    return dataf

# calculating nodal metrics

# returns vector
def clusteringCoefficient(network):
    return bct.clustering_coef_wu(network)

# returns vector
def betweennessCentrality(network):
    return bct.betweenness_wei(network)


# returns vector
def closenessCentrality(network):
    shortestPathMatrix = bct.distance_wei(network)
    averageShortestPath = []
    for i in range(len(shortestPathMatrix)):
        path = 0
        for j in shortestPathMatrix:
            path += j[i]
        averageShortestPath.append(path/len(shortestPathMatrix))
    return averageShortestPath


# returns vector
def localEfficiency(network):
    bct.efficiency_wei(network, local=True)


# returns vector
def degreeCentrality(network):
    dCentrality = []
    for j in network:
        dCentrality.append(sum(j))
    return dCentrality

