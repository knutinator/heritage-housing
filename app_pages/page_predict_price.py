from src.data_management import load_house_data, load_pkl_file
import streamlit as st
import numpy as np
import pandas as pd


def page_predict_price_body():
#load needed files

    version = 'v1'
    pipeline = load_pkl_file(
        f"outputs/predict_house_price/{version}/best_regressor_pipeline.pkl")
    best_features = (pd.read_csv(f"outputs/predict_house_price/{version}/X_train.csv")
                     .columns
                     .to_list()
                     )

    df = pd.read_csv("inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")

#run price prediction on inherited houses using trained ML pipeline
    st.write("### Predicted sale prices of the client's four inherited houses")
    st.write(
        f"* These are the characteristics of the clients houses (scroll to view more):"
    )
    st.write(df.head())
    df = df.filter(best_features)
    price_prediction = pipeline.predict(df).round(0)
    df['Predicted House Price'] = price_prediction
    st.write(
        f"\n"
    )
    st.write(
        f"* Here are the predicted sale prices of the clients houses, "
        f"together with the attributes that were used in our machine "
        f"learning model to produce the prediction:"

    )
    st.write(df.head())
