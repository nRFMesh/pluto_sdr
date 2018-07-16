import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dt = np.dtype([('i', 'i2'), ('q', 'i2')])

datai = np.fromfile("../../urh/capture_fast.dat", dtype=dt)
dte = np.dtype([('i', 'f'), ('q', 'f')])
#dataf = np.frombuffer(datai,dtype=dte)

#df = pd.DataFrame(data)
#df = pd.DataFrame(data, columns=data.dtype.names)

new_recarray = df.to_records()
new_recarray.tofile("../../urh/capture_fast.complex")

#df.to_csv("../../urh/capture_fast.csv",index=False)

#np.save(open("../../urh/capture_fast.bin",'w'),dataf)

#df.plot()
#plt.show()
