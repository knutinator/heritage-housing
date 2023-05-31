import streamlit as st
import numpy as np
import pandas as pd
from src.data_management import load_house_price_data, load_pkl_file


def page_predict_house_price_body():
#load needed files

    version = 'v1'
    pipeline = load_pkl_file(
        f"outputs/predict_price/{version}/best_regressor_pipeline.pkl")
    best_features = (pd.read_csv(f"outputs/predict_price/{version}/X_train.csv")
                     .columns
                     .to_list()
                     )

    df = pd.read_csv("inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
