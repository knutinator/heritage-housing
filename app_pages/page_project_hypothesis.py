import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis")

    st.info(
        f"**Hypothesis 1:**\n\n"
        f"It's believed that the attributes most people naturally consider "
        f"important, like the size of the house and its overall quality, "
        f"will turn out to be the key factors affecting house prices "
        f"when we analyze the data and apply machine learning techniques.\n "
    )
    st.info(
        f"**Hypothesis 2:**\n\n"
        f"It's also expected that predicting the prices of houses "
        f"with lower values will be easier compared to houses with higher "
        f"values. The idea here is that as house prices go up, things get "
        f"trickier because the relationships between different factors and "
        f"the final price become more complex and uncertain. "
    )
