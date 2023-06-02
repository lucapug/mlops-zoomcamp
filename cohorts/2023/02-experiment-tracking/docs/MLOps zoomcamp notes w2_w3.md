# MLOps Zoomcamp Notes for Weeks 2 (MLflow) and 3 (Wandb)

## week2 - MLFlow for experiment tracking and model management (model registry)

### First experiment (not tracked)

In the first week, Alexey has built the `duration-prediction` notebook, as an example of the typical data scientist way of work, mainly done of free execution of notebook cells, with weak structure for storing the sequence odf trials. Examples of rudimentary tracking tools are descibed both by Alexey in the first week and Cristian in the second week: markdown cellsinside the notebbok, with a list of experiments executed, or the same list archived as an Excel file. As for the models, they can be archived each one in a separate folder, whose name should be the way to recognize them!

### Experiment `nyc-taxi-experiment`, trackad by MLflow

Runs conducted in `duration-predictio.ipynb` (revised by Cristian)

* First and second run (tracked) are Linear regression with regularization (<strong>Lasso</strong>), manual hyperparameters setting (alfa = 0.1 in first run, alfa = 0.01 in second run)
* **Xgboost** with **hyperparameters optimization** (`hyperopt tool`): serveral runs created with an xgboost model and set of paramters generated for each run by hyperopt.
* Follow human analysis on the MLflow dashboard (UI) to determine the run with the `best parameters`; in view of the <strong>deployment to production</strong>, there are **multiple criteria** to select the best solution: best metric value, lowest execution time, smallest model storage volume,..
* for the selected best params, executed a run with use of `autolog()` [in the specific case xgboost.autolog()], to capture (log) a great number of execution parameters, without having to write many lines of code.
* Model management: executed a new run for best params, without autolog(), and logged artifacts and model (`log_artifacts`, `log_model`). log\_artifact allows to store the preprocessor, to be recovered for future inferences. log\_model is a first solution to save the model (the second one is better and is described below). Follow an example of load the model to do inferences.
* Execution of a sequence of runs, each one with a different sklearn estimator (<strong>RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor, LinearSVR</strong>), with use of autolog()

### Activities conducted in the model registry (`model-registry.ipynb notebook)`

* after deletion of all previous runs from `nyc-taxi-experiment` (from the UI), execept best\_params xgboost and the 4 sklearn estimators, use of MLflow client to **manage models** (register a model, save versions, **promoting** the different model versions to <strong>staging, production, archived stages</strong>). The promotion is simply adding a tag. To effectivly send to deployment a model, some CI/CD logic must be added, with deployment triggered by the tagging operation. It is a task of the ML engineer: analyze and test the tagged models provisioned by the Data Scientist, in order to decide which one to productionize.