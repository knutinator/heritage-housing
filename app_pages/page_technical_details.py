import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file
from src.evaluate import regression_performance, regression_evaluation, regression_evaluation_plots


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
        f"* The pipeline achieves **0.86** on the train set and **0.79** on the test set. \n"
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

    # evaluate performance on train and test sets
    regression_performance(X_train=X_train, y_train=y_train,
                           X_test=X_test, y_test=y_test, pipeline=pipeline)

    st.write("---")

    # Plots predicted sale price against the actual sale price
    st.write(
        "* **Scatterplots of the predicted price versus actual price (Train and test sets)**")
    st.info("* As we can see on the plots below, the prediction (red line) stops following "
            "the the actual price data (blue points) when reaching values higher than around 400000."

            )

    # inspect data
    if st.checkbox("Show Scatterplots"):
        st.write(
            "*(Note: plots may take a while to load)*"
        )
        regression_evaluation_plots(X_train=X_train, y_train=y_train,
                                X_test=X_test, y_test=y_test, pipeline=pipeline, alpha_scatter=0.5)
