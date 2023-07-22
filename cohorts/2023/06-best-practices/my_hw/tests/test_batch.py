from datetime import datetime
import pandas as pd

import batch

def test_prepare_data():
    def dt(hour, minute, second=0):
        return datetime(2022, 1, 1, hour, minute, second)
    
    categorical = ['PULocationID', 'DOLocationID']
    
    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2), dt(1, 10)),
        (1, 2, dt(2, 2), dt(2, 3)),
        (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),     
    ]

    columns = ['PULocationID', 'DOLocationID', 
               'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    
    df = pd.DataFrame(data, columns=columns)
    
    actual_result = batch.prepare_data(df, categorical)
    
    prep_data = [('-1','-1', dt(1, 2), dt(1, 10), 8.0),
                 ('1','-1', dt(1, 2), dt(1, 10), 8.0),
                 ('1','2', dt(2, 2), dt(2, 3), 1.0)
                 ]
    
    exp_cols = ['PULocationID', 'DOLocationID', 
               'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'duration']
    expected_result = pd.DataFrame(prep_data, columns=exp_cols)
    
    list1 = actual_result.to_dict(orient='list')
    list2 = expected_result.to_dict(orient='list')
    
    for (d1, d2) in zip(list1, list2):
        assert d1 == d2
