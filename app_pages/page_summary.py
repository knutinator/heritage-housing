import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    st.write(
        f" A machine learning app for house pricing visualization and\n"
        f" preciction in Ames, Iowa."
        f" The app helps the client to do the following:\n\n"
        f" * View which house attributes correlate to sale prices.\n"
        f" * Predict sale prices for houses in Ames, Iowa.")

    # text based on README file - "Dataset Content" section
    st.info(
        f"The dataset has almost 1.5 thousand rows and represents housing "
        f"records from Ames, Iowa, indicating house attributes (Floor Area, "
        f"Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) "
        f"and its respective sale price for houses built between 1872 and "
        f"2010.")

    # copied from README file - "Business Requirements" section
    st.success(
        f"** The project has 2 business requirements:** \n \n "
        f"**1.** The client is interested in discovering how the house attributes "
        f"correlate with the sale price. Therefore, the client expects data "
        f"visualisations of the correlated variables against the sale price "
        f"to show that. \n\n "
        f"**2.** The client is interested in predicting the house sale price from "
        f"her four inherited houses and any other house in Ames, Iowa. ")

    # Link to README file, so the users can have access to
    # full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/knutinator/heritage-housing).")
