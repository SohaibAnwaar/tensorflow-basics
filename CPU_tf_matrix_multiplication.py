import numpy as np
import time
from tqdm import tqdm


# Making Tensor Constant
np_arr = np.asarray([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [4.0, 5.0, 6.0]])
print("Starting cpu processing")
st = time.time()
for i in tqdm(range(0,100000000)):
    np_arr @ np_arr
    
# Took 35 sec    
print(f"Time Taken BY CPU {time.time() -st}")