from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
i=Image.open(raw_input("enter the location of image"))
iar=np.asarray(i)
#getting pixels
print "PIXELS OF THE IMAGE",i,'ARE', iar
#producing images

plt.imshow(iar)
plt.show()
