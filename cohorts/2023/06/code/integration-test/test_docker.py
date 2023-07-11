import json

import requests
from deepdiff import DeepDiff

event = {
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49642333528152160045161343175597482755845342796282068994",
                "data": "ewogICAgICAgICJyaWRlIjogewogICAgICAgICAgICAiUFVMb2NhdGlvbklEIjogMTMwLAogICAgICAgICAgICAiRE9Mb2NhdGlvbklEIjogMjA1LAogICAgICAgICAgICAidHJpcF9kaXN0YW5jZSI6IDMuNjYKICAgICAgICB9LCAKICAgICAgICAicmlkZV9pZCI6IDE1NgogICAgfQ==",
                "approximateArrivalTimestamp": 1688499216.333
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000000:49642333528152160045161343175597482755845342796282068994",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::188124115410:role/lambda-kinesis-role",
            "awsRegion": "eu-south-1",
            "eventSourceARN": "arn:aws:kinesis:eu-south-1:188124115410:stream/ride_events"
        }
    ]
}


url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
actual_response = requests.post(url, json=event).json()

print('actual response:')

print(json.dumps(actual_response, indent=2))

expected_response = {
    "predictions": [{
        'model': 'ride_duration_prediction_model',
        'version': 'Test123',
        'prediction': {
            'ride_duration': 18.2,
            'ride_id': 156   
        }
    }]
}




diff = DeepDiff(actual_response, expected_response, significant_digits=1)
print(f'diff={diff}')

assert 'type_changes' not in diff
assert 'values_changed' not in diff