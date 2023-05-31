import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file




def page_technical_details_body():

 # load house price pipeline files
    version = 'v1'
    pipeline = load_pkl_file(
        f"outputs/predict_house_price/{version}/best_regressor_pipeline.pkl")
    house_price_feat_importance = plt.imread(
        f"outputs/predict_house_price/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/predict_house_price/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/predict_house_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/predict_house_price/{version}/y_train.csv").squeeze()
    y_test = pd.read_csv(
        f"outputs/predict_house_price/{version}/y_test.csv").squeeze()

    st.write("### Machine Learning house price pipeline details")
    st.info(
        f"* The goal of the project was a model and a pipeline with an R2 "
        f"score of at least 0.75 on both train and test sets. \n"
        f"* The pipeline achieves XX on the train set and XX on the test set. \n"
    )
        # show pipeline steps
    st.write("---")
    st.write("* **ML pipeline steps used in this project**")
    st.write(pipeline)
    st.write("---")

        # show best features
    st.write("* The features the model was trained on and their importance.")
    st.write(X_train.columns.to_list())
    st.image(house_price_feat_importance)
    st.write("---")



    
