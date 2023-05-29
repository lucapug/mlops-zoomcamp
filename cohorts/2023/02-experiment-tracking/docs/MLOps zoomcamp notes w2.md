# MLOps Zoomcamp Notes Week2

## A resume of the experiments conducted throughout the week

### First experiment (not tracked)

In the first week, Alexey has built the `duration-prediction` notebook, as an example of the typical data scientist way of work, mainly done of free execution of notebook cells, with weak structure for storing the sequence odf trials (examples of rudimentary tracking tools are descibed both by Alexey in the first week and Cristin in the second week: Markdown cells with list of experiments executed, or the same list archived as an Excel file. As for the models, they can be archived each one in a separate folder whose name should be the way to recognize it)

### Experiment `nyc-taxi-experiment`, trackad by MLflow

Runs conducted in `duration-predictio.ipynb` (revised by Cristian)

* First and second run (tracked) are Linear regression with regularization (Lasso), manual hyperparameters setting (alfa = 0.1 in second run, alfa = 0.01 in third run)
* Xgboost with hyperparameters optimization (Hyperopt tool): serveral runs created with an xgboost model and set of paramters generated for each run by hyperopt. 
* Follow human analysis on the MLflow dashboard to determine the run with the `best parameters` (in view of the deployment to production, there are multiple criteria to select the best solution: best metric value, lowest execution time, smallest model storage volume,..)
* for the selected best params, executed a run with use of autolog() [in the specific case xgboost.autolog()], to capture (log) a great number of execution parameters, without having to write many lines of code. 
* Model management: executed a new run for best params, without autolog(), and logged artifacts and model (log\_artifacts, log\_model). log\_artifact allows to store the preprocessor, to be recovered for future inferences. log\_model is a first solution to save the model (the second one is better and is described below). Follow example of load the model to do inferences.
* Execution of a sequence of runs, each one with a different sklearn estimator (RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor, LinearSVR), with use of autolog()


activities conducted in model-registry.ipynb

* after deletion of all previous runs from nyc-taxi-experiment (from UI), execept best\_params xgboost and the 4 sklearn estimators, use of MLflow client to mange modles (register a model, save versions, prmoting the different versions to staging, production, archived stages). The promotion is simply adding a tag. To effectivly send to deployment a model, some CICD logic must be done, triggered by the tagging operation. it is a task of the ML engineer, analyze and test the tagged models provisioned by the Data Scientist, to decide which one to productionize.