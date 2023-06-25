#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip freeze | grep scikit-learn')


# In[27]:


import os
import pickle
import pandas as pd


# In[3]:


year = 2022
month = 2


# In[20]:


get_ipython().system("mkdir './output'")


# In[11]:


input_file=f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
output_file=f'./output/preds_{year:04d}-{month:02d}.parquet'


# In[4]:


with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


# In[12]:


categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


# In[13]:


#df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet')
df = read_data(input_file)
#df = read_data(f's3://lucap-nyc-taxi-data/data/yellow/yellow_tripdata_{year:04d}-{month:02d}.parquet')
#df = read_data ('s3://lucap-nyc-taxi-data/data/yellow/yellow_tripdata_2022-02.parquet')


# In[14]:


dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)


# In[15]:


y_pred.std()


# In[16]:


df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')


# In[23]:


df_result = pd.DataFrame()


# In[24]:


df_result['ride_id'] = df['ride_id']
df_result['prediction'] = y_pred


# In[25]:


df_result.head()


# In[26]:


df_result.to_parquet(
    output_file,
    engine='pyarrow',
    compression=None,
    index=False
)


# In[28]:


os.stat(output_file)

