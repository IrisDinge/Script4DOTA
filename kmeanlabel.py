


import pandas as pd
import numpy as np
'''

from data format:
<image path1> <box1> <box2>
<image path2> 
<image path3> <box1>
<image path4> <box1> <box2> <box3>

into
<box1> <box2>
<box1>
<box1> <box2> <box3>

so u can use kmeans.py
'''



pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_table('/home/dingjin/no0/tra_val_416.txt', header=None, delimiter='\n')


df1 = df[0].str.split(' ', expand=True)
df2 = df1.drop([0], axis=1)
df3 = df2.dropna(axis=0, how='any', thresh=3)

df3.replace(to_replace=r'^\s*$', value=np.nan, inplace=True, regex=True)
df3.replace(to_replace=[None], value=np.nan, inplace=True, regex=True)
df3.replace(to_replace=np.nan, value='', inplace=True, regex=True)
#df4 = pd.concat(df3.iloc[:, i] for i in range(df3.shape[1]))
#df4.index = np.arange(len(df4))

#df4.to_csv('/home/dingjin/no0/test.csv', index=False, header=None, sep=' ', encoding='UTF-8')
#df5 = pd.read_table('/home/dingjin/no0/test.txt', header=None, delimiter='\n')

#print(df3)

np.savetxt(r'/home/dingjin/no0/test.txt', df3.values, fmt='%s', delimiter=' ')
#df3.to_csv('/home/dingjin/no0/test.csv', index=False, header=None, sep=' ', line_terminator='\n')

