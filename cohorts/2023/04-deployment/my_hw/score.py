#!/usr/bin/env python
# coding: utf-8

import sys
import pickle
import pandas as pd


def load_model():
    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
    return dv, model

categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')   
    return df

def make_preds(dv, model, df):
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    return y_pred


def make_df_result(df:pd.DataFrame, y_pred, year, month, output_file):
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

    df_result = pd.DataFrame()

    df_result['ride_id'] = df['ride_id']
    df_result['prediction'] = y_pred

    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )
    
def run(): 
    YEAR = int(sys.argv[1])
    MONTH = int(sys.argv[2])
    input_file = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{YEAR:04d}-{MONTH:02d}.parquet'
    output_file = f'./preds_yellow_{YEAR:04d}-{MONTH:02d}.parquet'

    dv, model = load_model()
    print('reading data...')
    df = read_data(input_file)
    print(f'making predictions for yellow_{YEAR:04d}-{MONTH:02d}')
    y_pred = make_preds(dv, model, df)
    print("saving results to parquet file..")
    make_df_result(df, y_pred, YEAR, MONTH, output_file)
    print(f"mean predicted duration: {y_pred.mean():.2f}")


if  __name__  ==  "__main__":
    run()


