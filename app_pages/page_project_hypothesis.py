import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis")
    st.write("---")
    st.write(
        f"**Hypothesis 1:**\n\n"
        f"It's believed that the attributes most people naturally consider "
        f"important, like the size of the house and its overall quality, "
        f"will turn out to be the key factors affecting house prices "
        f"when we analyze the data and apply machine learning techniques.\n\n\n "
    )
    st.success(
        f"**Validation:**\n\n"
        f"The Feature Importance search on our selected algorithm showed us "
        f"that 'Overall Quality' and 'Ground Floor Living Area' are the two "
        f"most important attributes that influence sale price."
    )
    st.write("---")
    st.write(
        f"**Hypothesis 2:**\n\n"
        f"It's also expected that predicting the prices of houses "
        f"with lower values will be easier compared to houses with higher "
        f"values. The idea here is that as house prices go up, things get "
        f"trickier because the relationships between different factors and "
        f"the final price become more complex and uncertain. "
    )
    st.success(
        f"**Validation:**\n\n"
        f"When inspecting the scatterplots in the House Price Study, it was "
        f"clear that as price went up, the datapoints became fewer and more "
        f"spread out. This indicates a less obvious trend after a certain "
        f"level, which in turn will lead to less accurate predictions for "
        f"houses with higher value."
    )
