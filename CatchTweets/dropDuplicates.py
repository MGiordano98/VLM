import pandas as pd
import getMethods


hashtags = getMethods.getHashtags()

for i,val in enumerate(hashtags):
        df = pd.read_csv('CSV/'+val+'.csv')
        df.drop_duplicates(inplace=True)
        df.to_csv('CSV1/'+val+'.csv', index=False)
