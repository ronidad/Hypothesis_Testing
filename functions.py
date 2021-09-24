import numpy as np
def systematic_sampling(df,r,n):
    step=df.shape[0]//n
    indexes = np.arange(start=r, stop= len(df), step=step)
    systematic_sample = df[indexes]
    return systematic_sample#, indexes
    

