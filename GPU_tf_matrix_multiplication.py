import tensorflow as tf
physical_devices = tf.config.list_physical_devices('GPU') 

# Gpu Settings for rtx3070
from tensorflow.compat.v1.keras.backend import set_session
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU
config.log_device_placement = True  # to log device placement (on which device the operation ran)
sess = tf.compat.v1.Session(config=config)
set_session(sess)

import time
from tqdm import tqdm

print("Here is the tensorflow version ",tf.__version__)

# Making Tensor Constant
tensor1 = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [4.0, 5.0, 6.0]])

# Getting the shape of the tensor
print(tensor1.get_shape())


st = time.time()
for i in tqdm(range(0,1000000)):
    # Using tensorflow function to use gpu functionality
    tf.linalg.matmul(tensor1, tensor1)

# Took 34 sec
print(f"Time Taken BY GPU {time.time() -st}")


