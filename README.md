# Heritage Housing - Pricing Predictor <!-- omit in toc -->

A machine learning app for house pricing visualization and preciction in Ames, Iowa.

The app helps the client to do the following:
- View what house attributes correlate to sale prices.
- Predict future sale prices for specific houses in Ames, Iowa.

[View the app here >](https://heritage-house.herokuapp.com/)

---

## Index <!-- omit in toc -->

- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypothesis and validation](#hypothesis-and-validation)
  - [Hypothesis 1](#hypothesis-1)
  - [Hypothesis 2](#hypothesis-2)
- [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Credits](#credits)

---

# Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

[Back to Index](#index)

---


# Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

[Back to Index](#index)

---

# Hypothesis and validation

## Hypothesis 1

It's believed that the attributes most people naturally consider important, like the size of the house and its overall quality, will turn out to be the key factors affecting house prices when we analyze the data and apply machine learning techniques.

* **Validation:**
The Feature Importance search on our selected algorithm showed us that 'Overall Quality' and 'Ground Floor Living Area' are the two most important attributes that influence sale price.

## Hypothesis 2

It's also expected that predicting the prices of houses with lower values will be easier compared to houses with higher values. The idea here is that as house prices go up, things get trickier because the relationships between different factors and the final price become more complex and uncertain.

* **Validation:**
When inspecting the scatterplots in the House Price Study, it was clear that as price went up, the datapoints became fewer and more spread out. This indicates a less obvious trend after a certain level, which in turn will lead to less accurate predictions for houses with higher value.

[Back to Index](#index)

---

# The rationale to map the business requirements to the Data Visualisations and ML tasks

As a client, I have the following requirements:

**Business Requirement 1:**

* I want to analyze the house records data to determine which variables have a significant impact on the sale price.
  
* I want to view the correlation coefficients on a heatmap to prioritize variables based on their importance for the sale price.
  
* I would like to plot the important variables against the sale price to visually understand their correlation.

**Business Requirement 2:**

* I need easy access and navigation of the inherited houses data to locate specific house attributes.
  
* I want an accurate ML model capable of predicting the prices of my four inherited houses in Ames, Iowa.

* I need that the ML model provides precise price predictions for any other house in Ames, Iowa.

[Back to Index](#index)

---

# ML Business Case
What are the business requirements?

* The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.

* The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.

Is there any business requirement that can be answered with conventional data analysis?
* Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

Does the client need a dashboard or an API endpoint?

* The client needs a dashboard

What does the client consider as a successful project outcome?

* A study showing the most relevant variables correlated to sale price.

* Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.

Can you break down the project into Epics and User Stories?

* Information gathering and data collection.
* Data visualization, cleaning, and preparation.
* Model training, optimization and validation.
* Dashboard planning, designing, and development.
* Dashboard deployment and release.

Ethical or Privacy concerns?

* No. The client found a public dataset.
  
Does the data suggest a particular model?

* The data suggests a regressor where the target is the sale price.

What are the model's inputs and intended outputs?

* The inputs are house attribute information and the output is the predicted sale price.

What are the criteria for the performance goal of the predictions?

* We agreed with the client on an R2 score of at least 0.75 on the train set as well as on the test set.

How will the client benefit?

* The client will maximize the sales price for the inherited properties.

[Back to Index](#index)

---

# Dashboard Design

The dashboard consists of five pages:

1. **Quick Project Summary** - The page descrives the project, the dataset and the business requirements.

2. **House Price Study** - The page displays visualisation of the correlation between the house attributes and house sale price. *This fulfills Business Requirement 1.*

3. **Project Hypothesis** - The page lists the two project hypothesises and how they have been valiated.

4. **Price Predictor** - The page displays the attributes of the client's four inherited houses and the predicted sale price of them.
It also contains a live function that lets the client predict the price of any house in Ames, Iowa. *This fulfills Business Requirement 2.*

5. **Technical Details** - The page displays the R2 performance score of the model, followed by descriptions of the pipeline and features used to make the predictions. It also shows an overview of how well the Machine Learning model performs.

[Back to Index](#index)

---



# Unfixed Bugs
* There are no unfixed bugs.

[Back to Index](#index)

---

# Deployment
## Heroku

* The App live link is: https://heritage-house.herokuapp.com/
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

[Back to Index](#index)

---

## Main Data Analysis and Machine Learning Libraries

*(from requirements.txt)*<br>

numpy==1.18.5<br>
pandas==1.4.2<br>
matplotlib==3.3.1<br>
seaborn==0.11.0v
pandas-profiling==3.1.0<br>
plotly==4.12.0<br>
ppscore==1.2.0<br>
streamlit==0.85.0<br>
feature-engine==1.0.2<br>
imbalanced-learn==0.8.0<br>
scikit-learn==0.24.2<br>
xgboost==1.2.1<br>
yellowbrick==1.3<br>
Jinja2==3.1.1<br>
MarkupSafe==2.0.1<br>
protobuf==3.20<br>
ipywidgets==8.0.2<br>
altair<5<br>

[Back to Index](#index)

---

# Credits 

* Most of the code was adapted from the Churnometer walkthrough project, by Code Institute
  
* General structure of the code was inspired by
Farid 'faridjos' Benachenhou PP5 project: <https://github.com/faridjos/milestone-project-heritage-housing-issues>

[Back to Index](#index)

---