import streamlit as st
from src.data_management import load_house_data, load_pkl_file
import numpy as np
import pandas as pd


def page_predict_price_body():

    # load needed files
    version = 'v1'
    pipeline = load_pkl_file(
        f"outputs/predict_house_price/{version}/best_regressor_pipeline.pkl")
    best_features = (pd.read_csv(f"outputs/predict_house_price/{version}/X_train.csv")
                     .columns
                     .to_list()
                     )

    df = pd.read_csv(
        "inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")

    # run price prediction on inherited houses using trained ML pipeline
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

    # calculate sum of houses
    sum = df['Predicted House Price'].sum()
    st.write(
        f"* The predicted *total* sale price for all the four houses is: &nbsp;$ {sum}  \n"
    )

    st.write("---")

    # house price predictor in Ames, Iowa
    st.write("### Predict other house prices (in Ames, Iowa) \n")
    st.write(
        f"* The function below can be used to calculate a predicted "
        f"price for any house in Ames, Iowa. Input the square footage and "
        f"general quality of the house below, then press 'Run Prediction'. "
    )
    st.warning(
        f"Note: the prediction model is unreliable on very large houses.")

    live_pred = InputWidget()

    if st.button("Run prediction"):
        house_price_prediction = pipeline.predict(
            live_pred.filter(best_features)).round(0)
        st.write(
            f"* The predicted sale price for the house is: &nbsp;${house_price_prediction[0]}  \n"
        )


# create widget fields for input
def InputWidget():

    # load dataset
    df = load_house_data()
    percentageMin, percentageMax = 0.5, 1.0

    # make an empty DataFrame
    live_pred = pd.DataFrame([], index=[0])

    # create two separate sections for input widgets
    st.subheader("Ground floor living area (in square feet)")
    feature = 'GrLivArea'
    st_widget = st.number_input(
        label=feature,
        min_value=df[feature].min()*percentageMin,
        max_value=df[feature].max()*percentageMax,
        value=df[feature].median()
    )
    live_pred[feature] = st_widget

    st.subheader("Overall quality of the house (from 1 - 10)")
    feature = "OverallQual"
    st_widget = st.selectbox(
        label=feature,
        options=df[feature].sort_values(ascending=True).unique()
    )
    live_pred[feature] = st_widget

    return live_pred
