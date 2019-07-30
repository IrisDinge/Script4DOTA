
import pandas as pd

'''

delete the empty annotation only in txt file 

'''



pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_table('/home/dingjin/no0/tra_val_416.txt', header=None, delimiter='\n')
df1 = df[0].str.split(' ', expand=True)
df2 = df1.dropna(axis=0, how='any', thresh=3)
#print(df2)
df2.to_csv('/home/dingjin/no0/result.txt', index=False, header=None, sep=' ', line_terminator='\n')

