import numpy as np

import cv2

n=int (50)
b = np.ones([400,400],dtype = 'uint8')*255
for i in range(n,400,n*2):
        for j in range (n,400,n*2):

           b[j-n:j,i-n:i] = 0
           b[j:j+n,i:i+n] = 0 

cv2.imshow('checker board 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()  
