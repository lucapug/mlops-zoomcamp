## Model deployment

The predictor (or selected model) does the scoring job.

types of deployments:

<strong>offline or in batch mode</strong>: the predictor pull batches of data regularly (hourly, daily,..) and make the predictions in one shot for all the samples in the batch (example of churn analysis in marketing)
online: the model needs to be up running all the time

<strong>online-webservice</strong>: immediate model response (prediction) to a web request. It is a client server architecture, the backend create a stable connection during all the time of the communication client-server). (example of ride duration prediction : request from the app on the smartphone and immediate response with estimated duration..)

<strong>online-streaming</strong>: the backend (here named the producer) push an event to a <strong>streaming queue</strong>, then close this direct connection. Many services (consumers) pick events from the streaming queue and send their outcome (prediction) directly to the customer associated to the picked event (by-passing the backend server). Each consumer has its model to make predictions, always up and running to catch the event from the stream and make the prediction (examples: content moderation for events=uploaded videos on youtube; antother example is recomandation systems)

### **web-service (case of model stored locally , no model registry service)**

**first version.** test.py with a ride sample and simple call to predict.py (scoring job)
**second version.** predict.py transformed in a Flask app and test.py adopts requests python library to send prediction request to the flask server (not secure in production, only for local development..)
**third version.** flask server substituted by gunicorn for security reasons
**fourth version.** flask app with gunicorn server dockerized, to ease reproducibility

### **web-service (case of model in centralized model registry, use of MLFlow)**

Advantage of having easily shareable info of the model and its lineage. Mofification of the scoring script to log params and the trained model as an artifact. For storage, use of an AWS S3 bucket. to launch the mlflow server that will log info of the trained model:
`mlflow server --backend-store-uri=sqlite:///mlflow.db --default-artifact-root=s3://lucap-mlflow-artifacts-remote`

### offline (batch mode)

Even if the ride duration is tipically deployed as a web service, in this case we imagine that we need monthly batch predictions for analytical reasons. As an example, we want to compare the batch predictions with actual ride duration values to inform for possible traffic jams. 