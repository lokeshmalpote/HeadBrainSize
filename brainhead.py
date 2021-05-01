import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def MeanData(arr):
    size= len(arr)
    sum = 0
    
    for i in range(size):
        sum = sum + arr[i]
    return(sum/size)    


def MarvellousHeadBrain(name):
    dataset = pd.read_csv(name)
    print("size of dataset is ",dataset.shape)
    
    X = dataset["Head Size(cm^3)"].values
    Y = dataset["Brain Weight(grams)"].values
    
    print("length of X:",len(X))
    print("lenght of Y :",len(Y))
    
    Mean_X = MeanData(X)
    Mean_Y = MeanData(Y)

    print("Mean of Independent variable is",Mean_X)
    print("mean of independen variable is ",Mean_Y)
   
   
    # m =(Sum(X-Xb)*(Y-Yb))/sum(X-Xb)^2
    numerator = 0
    denomenator = 0
    
    for i in range(len(X)):
        numerator = numerator + (X[i] - Mean_X)*(Y[i] -Mean_Y )
        denomenator = denomenator + (X[i] - Mean_X)**2
        
    m = numerator/denomenator
    print(" value of slope is :",m)
    
    # Y = mX + C
    # C = Y -mX
    c = Mean_Y - (m * Mean_X)
    print("value of Y intercept is :",c)  
    
    X_start = np.min(X) - 200
    X_End = np.max(X) + 200
    
    x = np.linspace(X_start,X_End)
    y = m*x + c
    
    plt.plot(x,y,color = 'r',label = " Line of Regrreassion")
    plt.scatter(X,Y,color = 'b',label = "Data plots")
    
    plt.xlabel("Head size")
    plt.ylabel("Brain Weight")
    
    plt.legend()
    plt.show()
    
    
    
def main():
    print("Enter file name of  the dataset ")
    name = input()
    
    MarvellousHeadBrain(name)
    
if __name__=="__main__":
    main()