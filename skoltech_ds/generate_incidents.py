import numpy as np
import pandas as pd
M = 100
N = 1000000
df = pd.DataFrame({'feature1': np.random.randint(M, size=(N,)),
                   'feature2': np.random.randint(M, size=(N,)),
                   'time': np.random.rand(N)
                  })
df.to_csv('incidents.csv', index_label='id')
