import os
import pandas as pd
import joblib # Library for serializing and deserializing Python objects
from sklearn.model_selection import train_test_split
from pathlib import Path # Module to handle file system paths
import sys # Provides access to system-specific parameters and functions

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config # Import project-specific configuration from the config module

#load data set
def load_dataset(file_name):
    filepath = os.path.join(config.DATAPATH, file_name)
    _data = pd.read_csv(filepath)# Temporary variable for raw dataset loading
    _data.columns = [c.strip() for c in _data.columns] #remove spaces in column names
    return _data[config.FEATURES] 

#separate X and y
def separate_data(data):
    X=data.drop(config.TARGET, axis=1)
    y=data[config.TARGET]
    return X,y

#split the dataset
def split_data(X,y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

#Serialization
def save_pipleline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME) # Construct the save path for the model
    print(save_path)
    joblib.dump(pipeline_to_save, save_path) # Serialize the pipeline and save it to the specified path
    print(f"Model has been saved under the name {config.MODEL_NAME}")

#Deserialization
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH, pipeline_to_load)# Construct the load path for the model
    model_loaded = joblib.load(save_path)# Deserialize the pipeline from the specified path
    print(f"Model has been loaded")
    return model_loaded    
