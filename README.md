# README for DUAL DISCO: A Novel Approach to Acoustic Emission Monitoring in Multi-Laser LPBF Systems

## Project Overview

This repository contains the code and notebooks associated with the research paper **"DUAL DISCO: A Novel Approach to Acoustic Emission Monitoring in Multi-Laser LPBF Systems"**. The main goal of this project is to develop a novel signal processing technique called **DUAL DISCO (Dual Unmixing Acoustic Learning for Disentangling Interwoven Signal Complexity in Operations)**. This technique is designed to disentangle acoustic emission (AE) signals from concurrent laser-material interactions in multi-laser Laser Powder Bed Fusion (LPBF) systems, enabling accurate real-time monitoring of process quality. The data used in this project is available here: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13863838.svg)](https://doi.org/10.5281/zenodo.13863838)

## Repository Structure

The repository consists of several Jupyter notebooks and Python scripts categorized by the stages of the research pipeline. Each file has a clear naming convention to reflect its purpose. Below is a description of the key files and their roles.

### Data Preprocessing
- **0_CSV_2_parquet.ipynb**: Converts raw CSV data files into Parquet format for more efficient storage and processing.
- **0_CSV_2_parquet_TEST.ipynb**: Converts the test data from CSV to Parquet format.

### Exploratory Data Analysis (EDA)
- **1_EDA.ipynb**: Performs exploratory data analysis on the converted data, visualizing key metrics and inspecting the data quality.
- **1_EDA_TEST.ipynb**: Performs exploratory data analysis on the test data.

### Segmentation
- **2_Segmentation_test.ipynb**: Implements initial segmentation of acoustic data based on laser activity using ThreshMorph, a custom segmentation algorithm ([ThreshMorph Algorithm](https://c4science.ch/diffusion/12199/)).
- **2_Segmentation_test_TEST.ipynb**: Processes the test data for segmentation.
- **3_Segmentation_real_deal.ipynb**: Full segmentation pipeline for the training datasets.
- **3_Segmentation_real_deal_TEST.ipynb**: Full segmentation pipeline for the test datasets.

### Data Preparation for Classification
- **4_Database_preparation-Classification.ipynb**: Prepares datasets for classification tasks. Processes AE signals and assigns labels based on the ground truth (conduction or keyhole melting regimes).
- **4_Database_preparation-Classification-Short.ipynb**: Prepares a shorter version of the dataset for quicker testing.
- **4_Database_preparation-Classification-Short-Sequential.ipynb**: Prepares data specifically for sequential laser operations.
- **4_Database_preparation.ipynb**: General data preparation notebook for different tasks.
- **4_Database_preparation-Classification-Short_TEST.ipynb**: Prepares test data for the short classification task.

### Train-Test Split
- **5_Train_Test_Split-Classification.ipynb**: Splits the data into training and test sets for classification tasks.
- **5_Train_Test_Split-Classification-Short.ipynb**: Train-test split for the shorter dataset.
- **5_Train_Test_Split-Classification-Short-Sequential.ipynb**: Splits data for sequential operations.
- **5_Train_Test_Split.ipynb**: General train-test splitting for various tasks.
- **5_Train_Test_Split-Classification-Short-Sequential_TEST.ipynb**: Processes test data for train-test split in the sequential task.

### Model Training and Testing
- **6_Demixing-Classification.ipynb**: Implements the DUAL DISCO algorithm for demixing AE signals and classifying the melting regimes in simultaneous laser operations.
- **6_Demixing-Classification-Short.ipynb**: Short version for testing demixing with a smaller dataset.
- **6_Demixing-Classification-Short-Cuda0_hyperparams.ipynb**: Hyperparameter optimization for the demixing model using GPU acceleration.
- **6_Demixing-Cuda1.ipynb**: Alternative demixing model using a different GPU setting.
- **6_Demixing.ipynb**: General demixing notebook.
- **6_Demixing-Classification-Short_Cuda0_hyperparams_TEST.ipynb**: Processes the test data using demixing with optimized hyperparameters.

### Performance Evaluation
- **7_Performance_evaluation.ipynb**: Evaluates the performance of the models (accuracy, precision, recall, F1-score) on the test set.
- **7_Performance_evaluation_TEST.ipynb**: Evaluates performance using the test data.

### Interpretability
- **8_Interpretability.ipynb**: Analyzes model interpretability, such as frequency band importance in the classification of AE signals.

### Results
- **Results - Sequential mode.ipynb**: Contains the results and analysis from sequential mode LPBF operations.
- **Results - Simultaneous mode.ipynb**: Contains the results and analysis from simultaneous multi-laser operations.

### Utilities
- **utils.py**: Utility functions used across various notebooks for data loading, preprocessing, and analysis.

### Configuration Files
- **params.xlsx**: Contains the parameters used for training the model.
- **params_test.xlsx**: Testing parameters configuration file.

## Usage Instructions

### Running the Notebooks

1. **Data Preprocessing**: Start by converting raw CSV data into Parquet format using the `0_CSV_2_parquet.ipynb` notebook.
2. **Exploratory Data Analysis**: Analyze the dataset using `1_EDA.ipynb` to understand its structure and key characteristics.
3. **Segmentation**: Segment the AE signals using `2_Segmentation_test.ipynb` or `3_Segmentation_real_deal.ipynb` for the final dataset.
4. **Data Preparation**: Prepare datasets for classification using `4_Database_preparation-Classification.ipynb` or the short versions.
5. **Train-Test Split**: Split the data into training and test sets using `5_Train_Test_Split-Classification.ipynb`.
6. **Model Training**: Train the DUAL DISCO model with `6_Demixing-Classification.ipynb` or any other relevant notebooks.
7. **Performance Evaluation**: Assess model performance using `7_Performance_evaluation.ipynb`.
8. **Interpretability**: Analyze the interpretability of the model using `8_Interpretability.ipynb`.

### Contribution Guidelines

Feel free to open issues or submit pull requests for improvements. Make sure to follow proper coding conventions and include detailed comments in your code.

## License

This project is licensed under [Creative Commons].

For any questions, please contact the corresponding author:

**Giulio Masinelli** - giulio.masinelli@empa.ch

## Acknowledgments

This research was supported by the Bern Economic Development Agency and Swiss Federal Laboratories for Materials Science and Technology (Empa). Special thanks to Thomas Rytz for technical support.
