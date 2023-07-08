import model


def test_base64_decode():
    base64_input = "ewogICAgICAgICJyaWRlIjogewogICAgICAgICAgICAiUFVMb2NhdGlvbklEIjogMTMwLAogICAgICAgICAgICAiRE9Mb2NhdGlvbklEIjogMjA1LAogICAgICAgICAgICAidHJpcF9kaXN0YW5jZSI6IDMuNjYKICAgICAgICB9LCAKICAgICAgICAicmlkZV9pZCI6IDE1NgogICAgfQ=="
    actual_result = model.base64_decode(base64_input)
    expected_result = {
        "ride": {
            "PULocationID": 130,
            "DOLocationID": 205,
            "trip_distance": 3.66
        }, 
        "ride_id": 156
    }
    
    assert actual_result == expected_result

def test_prepare_features():

    model_service = model.ModelService(None)
    
    ride = {
            "PULocationID": 130,
            "DOLocationID": 205,
            "trip_distance": 3.66
        }
    
    actual_features = model_service.prepare_features(ride)
    
    expected_features = {
        "PU_DO": "130_205",
        "trip_distance": 3.66
    }
    
    assert actual_features == expected_features
    
class ModelMock():
    def __init__(self, value) -> None:
        self.value = value
    
    def predict(self, X):
        n = len(X)
        return [self.value]*10


def test_predict():

    model_mock = ModelMock(10.0)
    model_service = model.ModelService(model_mock)
    
    features = {
        "PU_DO": "130_205",
        "trip_distance": 3.66
    }
    
    actual_preds = model_service.predict(features)
    expected_preds = 10.0

    
    assert actual_preds == expected_preds

def test_lambda_handler():

    model_mock = ModelMock(10.0)
    model_version = 'Test123'
    model_service = model.ModelService(model_mock, model_version)
    
    event = {
        "Records": [
            {
                "kinesis": {
                    "data": "ewogICAgICAgICJyaWRlIjogewogICAgICAgICAgICAiUFVMb2NhdGlvbklEIjogMTMwLAogICAgICAgICAgICAiRE9Mb2NhdGlvbklEIjogMjA1LAogICAgICAgICAgICAidHJpcF9kaXN0YW5jZSI6IDMuNjYKICAgICAgICB9LCAKICAgICAgICAicmlkZV9pZCI6IDE1NgogICAgfQ==",
                },
            }
        ]
    }   
    
    actual_preds = model_service.lambda_handler(event)
    expected_preds = {
        'predictions': [
            {
                'model': 'ride_duration_prediction_model',
                'version': model_version,
                'prediction': {
                    'ride_duration': 10.0,
                    'ride_id': 156,
                },
            }
        ]
    }

    
    assert actual_preds == expected_preds    