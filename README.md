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
- [Development](#development)
- [User Stories](#user-stories)
- [Initial Data Analysis](#initial-data-analysis)
  - [Exploratory Data Analysis (EDA) with Pandas](#exploratory-data-analysis-eda-with-pandas)
- [Correlation Analysis](#correlation-analysis)
- [Testing](#testing)
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
The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.
Is there any business requirement that can be answered with conventional data analysis?
Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.
Does the client need a dashboard or an API endpoint?
The client needs a dashboard
What does the client consider as a successful project outcome?
A study showing the most relevant variables correlated to sale price.
Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.
Can you break down the project into Epics and User Stories?
Information gathering and data collection.
Data visualization, cleaning, and preparation.
Model training, optimization and validation.
Dashboard planning, designing, and development.
Dashboard deployment and release.
Ethical or Privacy concerns?
No. The client found a public dataset.
Does the data suggest a particular model?
The data suggests a regressor where the target is the sale price.
What are the model's inputs and intended outputs?
The inputs are house attribute information and the output is the predicted sale price.
What are the criteria for the performance goal of the predictions?
We agreed with the client on an R2 score of at least 0.75 on the train set as well as on the test set.
How will the client benefit?
The client will maximize the sales price for the inherited properties.

[Back to Index](#index)

---

# Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

[Back to Index](#index)

---

# Development

# User Stories
After reviewing the business requirements, a set of user stories were formulated to guide the development procedure. These were collected in a project planning board which can be viewed here: <https://github.com/users/knutinator/projects/3>
<br><br>

**USER STORY #1: View variables relevant to price**

* As a client, I want to see visualizations of the most relevant variables correlated to sale price, so that I can better understand the relationship between house attributes and sale prices.
<br><br>

**USER STORY #2: View distribution of attributes**

* As a client, I want to see visualizations of the distribution of house attributes, so that I can better understand the range of values for each variable.
<br><br>

**USER STORY #3: Predict house prices**

* As a client, I want a machine learning model that can predict the sale price of my inherited houses, as well as any other house in Ames, Iowa, so that I can make informed decisions about the sales prices.
<br><br>

**USER STORY #4: View prediction accuracy**

* As a client, I want to be able to test the accuracy of the model on a test set, and receive a performance report with an R2 score of at least 0.75 on both the train and test sets.
<br><br>

**USER STORY #5: View project on dashboard**

* As a client, I want a dashboard that presents the data visualizations and machine learning model predictions in a clear and concise manner, so that I can easily access the insights and make informed decisions about the sales prices of the houses.
<br><br>

[Back to Index](#index)

---

# Initial Data Analysis
In this project, I conducted an initial analysis of the house price dataset to gain insights into the factors influencing house prices. The dataset consists of information about various features related to houses, such as square footage, number of bedrooms, basement characteristics, garage details, and more.

1. **Loading the Dataset:** I started by loading the house price dataset into a Pandas DataFrame, allowing me to manipulate and analyze the data efficiently.<br><br>
2. **Data Cleaning:** Before diving into the analysis, I performed data cleaning to make the data more easily computable. This involved converting all float values to integer values, replacing all NaN values with 0, and replacing some of the None values with No (to confirm with the Dataset Content Description.)<br><br>
3. **Data remapping:**
Following that, I mapped all the categorical data values to numerical values based on how many categories were in each column. The result was a DataFrame containing only numerical values, which is much more suitable for further analysis.

## Exploratory Data Analysis (EDA) with Pandas

To get a better understanding of the dataset, I performed Exploratory Data Analysis (EDA) using the Pandas library in Python. Here are the key steps I took:

1. **Descriptive Statistics:** I computed descriptive statistics for the numerical variables, such as mean, standard deviation, minimum, maximum, and quartiles. This provided an overview of the central tendencies and distributions of the data.<br><br>
2. **Visualization:** To visualize the relationships between the house price and other variables, I created various types of plots, including scatter plots, box plots, and bar charts. These visualizations allowed me to identify potential correlations and patterns.

# Correlation Analysis

Correlation analysis is crucial for understanding the relationships between variables and their impact on house prices. I used the correlation coefficient to measure the strength and direction of the linear relationship between the variables. Here are the steps I followed:

1. **Selecting Variables:** I identified a set of key variables that I hypothesized might have a significant impact on house prices. These variables included square footage, overall house quality, the house age, size of the garage, and kitchen quality.<br><br>
2. **Computing Correlations:** Using the Pandas library, I computed the correlation coefficients between the selected variables and the house prices. I utilized both Pearson correlation (for numerical variables) and Spearman correlation to capture different types of relationships.<br><br>
3. **Visualization:** To visually represent the correlations, I created scatter plots and heatmaps. Scatter plots helped visualize the relationships between individual variables and house prices, while heatmaps provided a comprehensive view of the correlation matrix.


Overall, this initial analysis and correlation visualization allowed me to identify potential predictors of house prices and gain insights into the dataset. These findings laid the foundation for further analysis and modeling in the project.

[Back to Index](#index)

---

# Testing

## Unfixed Bugs
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
* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

[Back to Index](#index)

---

# Credits 

* Most of the code was adapted from the Churnometer walkthrough project, by Code Institute
* General structure of the code was inspired by
Farid 'faridjos' Benachenhou PP5 project: <https://github.com/faridjos/milestone-project-heritage-housing-issues>

[Back to Index](#index)

---