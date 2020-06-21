import numpy as np
import cv2

b = np.ones([400,400],dtype = 'uint8')*255
n=50
j=n
while(j<=400):
     for i in range(n,400,n*2):
          
            b[j-n:j,i-n:i] = 0
            b[j:j+n,i:i+n] = 0

     j+=n*2    
cv2.imshow('checker board 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
