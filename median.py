import numpy as np
import math
import matplotlib.pyplot as plt
import cv2
import sys

def median(S,img):
    
    img = np.asarray(img)
    S = int(S)
    z = S*S
    location = (z + 1)/ 2
    location = int(location)
    
    result_rows = img.shape[0] - S + 1
    result_columns = img.shape[1] - S + 1
    resultR = []
    resultG = []
    resultB = []

    result = np.zeros((result_rows,result_columns,3))
    
    for i in range (result_rows):     # 2 for loops for sweep and result
        result_rowsR = []
        result_rowsG = []
        result_rowsB = []
        for j in range (result_columns):
            ii = i
            u = 0
            Rarray1d = np.zeros((z))
            Garray1d = np.zeros((z))
            Barray1d = np.zeros((z))
            for x in range(S):     #2 for getting 2 d array for sorting 
                jj = j 
                for y in range(S):
                    Rarray1d[u] = (img[ii][jj][0])
                    Garray1d[u] = (img[ii][jj][1])
                    Barray1d[u] = (img[ii][jj][2])
                    jj = jj + 1
                    u=u+1
                ii = ii + 1    
            Rarray1d = np.sort(Rarray1d)
            Garray1d = np.sort(Garray1d)
            Barray1d = np.sort(Barray1d)
            result_rowsR.append(Rarray1d[location])        
            result_rowsG.append(Garray1d[location])        
            result_rowsB.append(Barray1d[location])      
        resultR.append(result_rowsR)        
        resultG.append(result_rowsG)        
        resultB.append(result_rowsB)
            
    
    result[...,0] = resultR 
    result[...,1] = resultG 
    result[...,2] = resultB
    for i in range (result_rows):     # 2 for float approximation
        for j in range (result_columns):
            result[i][j][0] = result[i][j][0] /256
            result[i][j][1] = result[i][j][1] /256
            result[i][j][2] = result[i][j][2] /256
    
    return result
    
target_file = input("type in your target file name with extension: ")
img1 = cv2.imread(target_file)
plt.subplot(1,2,1)
plt.imshow(img1)
img1.shape    

S = input("input median filter size : ")
result = median(S,img1)
plt.subplot(1,2,2)
plt.imshow(result)

    