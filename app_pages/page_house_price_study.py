from src.data_management import load_house_data
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
st.set_option('deprecation.showPyplotGlobalUse', False)


def page_house_price_study_body():
    # load data
    df = load_house_data()

    vars_to_study = ['GarageArea', 'GrLivArea',
                     'KitchenQual', 'OverallQual', 'YearBuilt']

    st.write("### House Price Study")

    st.info(
        f"* The client is interested in discovering how the house "
        f"attributes correlate with the sale price. Therefore, the "
        f"client expects data visualizations of the correlated "
        f"variables against the sale price to show that."
    )

    # inspect data
    if st.checkbox("Inspect House Attributes"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")
        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook "
        f"to better understand how "
        f"the house attributes are correlated to sale prices. \n"
        f"The most correlated attributes are: **{vars_to_study}**"
    )
    st.info(
        f"The correlation plots below indicate that the following are the "
        f"most important attributes that affect house sale prices: \n"
        f"* Overall quality of the house \n"
        f"* Size of ground floor \n"
        f"* Quality of kitchen \n"
        f"* Size of garage \n"
        f"* Newness of house (year built)\n"
    )


def corr_heatmap(df, vars_to_study):
    vars_to_study.append('SalePrice')

    # Plot the heat map
    sns.heatmap(df[vars_to_study].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation of features to SalePrice")
    st.pyplot()

    # Remove SalePrice from vars_to_study
    vars_to_study.remove('SalePrice')


def corr_scatterplot(df, vars_to_study):
    # create scatterplots showing the relationship between each variable and SalePrice
    for var in vars_to_study:
        plt.figure()
        plt.scatter(df[var], df['SalePrice'], alpha=0.5)
        plt.xlabel(var)
        plt.ylabel('SalePrice')
        plt.title(f'{var} vs. SalePrice')
        st.pyplot()