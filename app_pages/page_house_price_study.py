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

    # copied from house_price_study notebook
    vars_to_study = ['1stFlrSF',
                     '2ndFlrSF',
                     'GarageArea',
                     'GrLivArea',
                     'KitchenQual',
                     'OverallQual',
                     'TotalBsmtSF']

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

    )
    st.info(
        f"The correlation plots below indicate that the following are the "
        f"most important attributes that affect house sale prices: \n\n"

        f"* **OverallQual** -  Overall quality of the house \n"
        f"* **GrLivArea**   -  Size of ground floor, in square feet \n"
        f"* **KitchenQual** -  Quality of kitchen \n"
        f"* **GarageArea**  -  Size of garage in square feet \n"
        f"* **1stFlrSF**    -  Size of First Floor in square feet \n"
        f"* **2ndFlrSF**    -  Size of Second Floor in square feet \n"
        f"* **TotalBsmtSF** -  Total Basement size in square feet \n"
    )

    # Correlation Heatmap
    if st.checkbox("Correlation Heatmap"):
        st.write(
            f"The heatmap shows how the top seven attributes correlate "
            f"to each other and the target, 'SalePrice'. "
            f"The higher the number, the stronger the correlation.")
        corr_heatmap(df, vars_to_study)

    # Correlation Scatterplots
    if st.checkbox("Correlation Scatterplots"):
        st.write(
            f"The scatterplots shows how the datapoints of each individual "
            f"attribute correlates to SalePrice")
        corr_scatterplot(df, vars_to_study)


def corr_heatmap(df, vars_to_study):
    df_copy = df.copy()
    kitchenqual_mapping = {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1}
    df_copy['KitchenQual'] = df_copy['KitchenQual'].map(kitchenqual_mapping)

    # Create a separate list for plotting
    plot_vars = vars_to_study.copy()
    plot_vars.append('SalePrice')

    # Plot the heat map
    sns.heatmap(df_copy[plot_vars].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation of features to SalePrice")
    st.pyplot()


def corr_scatterplot(df, vars_to_study):
    df_copy = df.copy()
    kitchenqual_mapping = {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1}
    df_copy['KitchenQual'] = df_copy['KitchenQual'].map(kitchenqual_mapping)

    # Create a separate list for plotting
    plot_vars = vars_to_study.copy()
    plot_vars.append('SalePrice')

    # create scatterplots showing the relationship between each variable and SalePrice
    for var in plot_vars:
        plt.figure()
        plt.scatter(df_copy[var], df_copy['SalePrice'], alpha=0.5)
        plt.xlabel(var)
        plt.ylabel('SalePrice')
        plt.title(f'{var} vs. SalePrice')
        st.pyplot()
