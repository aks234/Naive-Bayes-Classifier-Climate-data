# Naive-Bayes-Classifier-Climate-data
This dataset contains records of simulation crashes encountered during climate model uncertainty quantification (UQ) ensembles
The goal is to use classification to predict simulation outcomes (fail or succeed) from input parameter values, and to use sensitivity analysis and feature selection to determine the causes of simulation crashes. 
Attribute Information:

The goal is to predict climate model simulation outcomes (column 21, fail or succeed) given scaled values of climate model input parameters (columns 3-20). 

Column 1: Latin hypercube study ID (study 1 to study 3) 

Column 2: simulation ID (run 1 to run 180) 

Columns 3-20: values of 18 climate model parameters scaled in the interval [0, 1] 

Column 21: simulation outcome (0 = failure, 1 = success)
