from os import listdir
import networkx as nx
import os
import csv
import pandas as pd
import functions
import numpy as np


def init():

    directory = "C:\\Users\\Sk7w4tch3r\\Desktop\\Fifth One\\Numerical Linear Algebra\\Project\\NYU Dataset"

    outDirectory = directory + "\\csv\\"
    connectionMatrix = directory + "\\connection\\"
    degreeCentralityDirectory = directory + "\\degree\\"
    betweennessCentralityDirectory = directory + "\\betweenness\\"
    closenessCentralityDirectory = directory + "\\closeness\\"
    localEfficiencyDirectory = directory + "\\localeff\\"
    clusteringCoefficientDirectory = directory + "\\clusteringcoeff\\"
    allFeatures = directory + "\\allfeatures\\"

    fileTitles = [f for f in listdir(directory) if f.endswith(".1D")]
    print(len(fileTitles))
    csvFileTitles = [f[:len(f) - 3] + ".csv" for f in fileTitles]
    print(len(csvFileTitles))

    data = [directory,
            outDirectory,
            fileTitles,
            csvFileTitles,
            degreeCentralityDirectory,
            betweennessCentralityDirectory,
            closenessCentralityDirectory,
            localEfficiencyDirectory,
            clusteringCoefficientDirectory,
            connectionMatrix]

    # changing 1d format to csv and saving them into the desired path
    # for i in range(len(fileTitles)):
    #     dataToConnection(data, fileTitles[i], csvFileTitles[i])


    # creating degree centrality database
    # for i in range(len(fileTitles)):
    #     network = loadCsvToList(data[9] + csvFileTitles[i])
    #     degreeCenter = functions.degreeCentrality(network)
    #     saveListToCsv(data[4] + csvFileTitles[i], degreeCenter)


    # creating betweenness centrality database
    # for i in range(len(fileTitles)):
    #     network = loadCsvToList(data[9] + csvFileTitles[i])
    #     G = nx.from_numpy_matrix(network)
    #     betweenCenter = list(nx.betweenness_centrality(G, weight='weight').values())
    #     saveListToCsv(data[5] + csvFileTitles[i], betweenCenter)

    # creating closeness centrality database
    # for i in range(len(fileTitles)):
    #     network = loadCsvToList(data[9] + csvFileTitles[i])
    #     G = nx.from_numpy_matrix(network)
    #     closenessCenter = list(nx.closeness_centrality(G, distance='weight').values())
    #     saveListToCsv(data[6] + csvFileTitles[i], closenessCenter)


    # creating clustering coefficient database
    # for i in range(len(fileTitles)):
    #     network = loadCsvToList(data[9] + csvFileTitles[i])
    #     clusteringCoeff = functions.clusteringCoefficient(network)
    #     saveListToCsv(data[8] + csvFileTitles[i], clusteringCoeff)


    # concating all features vectors to one vector 
    # so now each person will have a 1*(116*4) vector
    # for i in range(len(fileTitles)):
    #     between = loadCsvToList(betweennessCentralityDirectory+csvFileTitles[0])
    #     closeness = loadCsvToList(closenessCentralityDirectory+csvFileTitles[0])
    #     cluster = loadCsvToList(clusteringCoefficientDirectory+csvFileTitles[0])
    #     degree = loadCsvToList(degreeCentralityDirectory+csvFileTitles[0])
    #     temp = np.concatenate([between, closeness, cluster, degree])
    #     np.savetxt(allFeatures+csvFileTitles[i], temp, delimiter=",")


    return data


def dataToConnection(data, inputFormat, outputFormat):
    inputFile = open(data[0] + "\\" + inputFormat, "r")
    outputFile = open(data[9] + outputFormat, "w+")
    for i in inputFile:
        csv.writer(outputFile).writerow(i.split())
    df = pd.read_csv(data[1] + outputFormat)
    df.corr(method='pearson').apply(absol).apply(inverser).to_csv(data[9] + outputFormat, header = True)


# returns list
def loadCsvToList(path):
    df = pd.read_csv(path)
    # array = df.drop(df.columns[0], axis = 1).to_numpy()
    return df.to_numpy()


# takes an np array as input and saves it as a csv file
# into the given path
def saveListToCsv(path, array):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w+") as entry:
        np.savetxt(entry, array, delimiter=',')


def inverser(x):
    return 1 / x


def absol(x):
    return abs(x)

# init()