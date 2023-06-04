# MLOps Zoomcamp Notes for Weeks 2 (MLflow) and 3 (Wandb)

## week2 - MLFlow for experiment tracking and model management (model registry)

### First experiment (not tracked)

In the first week, Alexey has built the `duration-prediction` notebook, as an example of the typical data scientist way of work, mainly done of free execution of notebook cells, with weak structure for storing the sequence odf trials. Examples of rudimentary tracking tools are descibed both by Alexey in the first week and Cristian in the second week: markdown cells inside the notebook, with a list of experiments executed, or the same list archived as an Excel file. As for the models, they can be archived each one in a separate folder, whose name should be the way to recognize them!

### Experiment `nyc-taxi-experiment`, trackad by MLflow

Runs conducted in `duration-predictio.ipynb` (revised by Cristian)

* First and second run (tracked) are Linear regression with regularization (<strong>Lasso</strong>), manual hyperparameters setting (alfa = 0.1 in first run, alfa = 0.01 in second run)
* **Xgboost** with **hyperparameters optimization** (`hyperopt tool`): several runs created with an xgboost model and set of paramters generated for each run by hyperopt.
* Follow human analysis on the MLflow dashboard (UI) to determine the run with the `best parameters`; in view of the <strong>deployment to production</strong>, there are **multiple criteria** to select the best solution: best metric value, lowest execution time, smallest model storage volume,..
* for the selected best params, executed a run with use of `autolog()` [in the specific case xgboost.autolog()], to capture (log) a great number of execution parameters, without having to write many lines of code.
* Model management: executed a new run for best params, without autolog(), and logged artifacts and model (`log_artifacts`, `log_model`). log\_artifact allows to store the preprocessor, to be recovered for future inferences. log\_model is a first solution to save the model (the second one is better and is described below). Follow an example of load the model to do inferences.
* Execution of a sequence of runs, each one with a different sklearn estimator (<strong>RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor, LinearSVR</strong>), with use of autolog()

### Activities conducted in the model registry (`model-registry.ipynb notebook)`

* after deletion of all previous runs from `nyc-taxi-experiment` (from the UI), execept best\_params xgboost and the 4 sklearn estimators, use of MLflow client to **manage models** (register a model, save versions, **promoting** the different model versions to <strong>staging, production, archived stages</strong>). The promotion is simply adding a tag. To effectivly send to deployment a model, some CI/CD logic must be added, with deployment triggered by the tagging operation. It is a task of the ML engineer: analyze and test the tagged models provisioned by the Data Scientist, in order to decide which one to productionize.

## week 3 - Notes on Webinar and on the side by side hw2 execution with wandb and mlflow

### webinar

intro to use of tables to better make analysis of tabular data in the dashboard. Any kind of media easily logged (also inside table if you want). Very easy to create html rich reports (with interactive show of the wandb charts and plots): semms similar to a Notion page. Among the integrations, if some Tensorboar visualization can't be reproduced, there is the possibility to host tensorboard logs directly inside wandb project (1 line of code needed, `wandb.init(project='my-project', sync_tensorboard=True)`). Wandb is very well suited for Deep learning projects. With the Prompt service wandb can even track LLMs tuning with prompts..

### side by side execution of homework 2

* **q1** install library in local and say which version
* **q2** preprocess data, save dictvetorizer, and say saved file dimension
* **q3** train data with RandomForestRegressor, and say max\_depth value
* **q4** hyperparameters tuning against val\_data, and say best val\_RMSE (mlflow) or analyze features\_importance (wandb) to decide best\_params model
* **q5** (mlflow) select top 5 runs that minimize val\_rmse, execute them on test\_data, promote the best one (min test\_rmse) to model registry, (wandb) link best\_params model to model registry

**notes on the homework:** slightly different homework tasks, and apparently in wandb\_hw no use of test\_data to select the model to promote to model registry..hyperparameter optimization in local with hyperopt or optuna in mlflow, server side control in wandb with sweep that makes use of a particular Bayesian Optimization algorithm named BOHB. Client side there are agents to make connection to the centralized sweep controller.

<strong>peculiarities (</strong>these are my **first notes and impressions** as a <strong>fresh learner</strong>!<strong>):</strong> better data tracking in wandb (in mlflow only get track of data file names). wandb lacks of the local UI that is present in mlflow, but it's possible to work offline and sync later to dashboard. nice DAG lineage for artifacts in wandb. In mlflow useful autolog(), not present in wandb, to log a bunch of parameters without manual coding. Richer documentation in wandb and curated free courses. Both are considering LLMs tracking, but in wandb there are greater advancements (Prompt service)!