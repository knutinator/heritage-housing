import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"The dataset is sourced from Kaggle. We then created a fictitious "
        f"user story where predictive analytics can be applied in a real "
        f"project in the workplace. "
        f"The dataset has almost 1.5 thousand rows and represents housing "
        f"records from Ames, Iowa, indicating house profile(Floor Area, "
        f"Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) "
        f"and its respective sale price for houses built between 1872 and "
        f"2010.")

    # Link to README file, so the users can have access to 
        # #full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/knutinator/heritage-housing).")

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"1 - The client is interested in discovering how the house attributes "
        f"correlate with the sale price. Therefore, the client expects data "
        f"visualisations of the correlated variables against the sale price "
        f"to show that. "
        f"2 - The client is interested in predicting the house sale price from "
        f"her four inherited houses and any other house in Ames, Iowa. "
     
    )
