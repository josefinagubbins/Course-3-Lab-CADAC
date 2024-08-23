#!/usr/bin/env python
# coding: utf-8

# # **Course 3 Automatidata project**
# **Course 3 - Go Beyond the Numbers: Translate Data into Insights**

# You are the newest data professional in a fictional data consulting firm: Automatidata. The team is still early into the project, having only just completed an initial plan of action and some early Python coding work. 
# 
# Luana Rodriquez, the senior data analyst at Automatidata, is pleased with the work you have already completed and requests your assistance with some EDA and data visualization work for the New York City Taxi and Limousine Commission project (New York City TLC) to get a general understanding of what taxi ridership looks like. The management team is asking for a Python notebook showing data structuring and cleaning, as well as any matplotlib/seaborn visualizations plotted to help understand the data. At the very least, include a box plot of the ride durations and some time series plots, like a breakdown by quarter or month. 
# 
# Additionally, the management team has recently asked all EDA to include Tableau visualizations. For this taxi data, create a Tableau dashboard showing a New York City map of taxi/limo trips by month. Make sure it is easy to understand to someone who isn’t data savvy, and remember that the assistant director at the New York City TLC is a person with visual impairments.
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions.

# # Course 3 End-of-course project: Exploratory data analysis
# 
# In this activity, you will examine data provided and prepare it for analysis. You will also design a professional data visualization that tells a story, and will help data-driven decisions for business needs. 
# 
# Please note that the Tableau visualization activity is optional, and will not affect your completion of the course. Completing the Tableau activity will help you practice planning out and plotting a data visualization based on a specific business need. The structure of this activity is designed to emulate the proposals you will likely be assigned in your career as a data professional. Completing this activity will help prepare you for those career moments.
# 
# **The purpose** of this project is to conduct exploratory data analysis on a provided data set. Your mission is to continue the investigation you began in C2 and perform further EDA on this data with the aim of learning more about the variables. 
#   
# **The goal** is to clean data set and create a visualization.
# <br/>  
# *This activity has 4 parts:*
# 
# **Part 1:** Imports, links, and loading
# 
# **Part 2:** Data Exploration
# *   Data cleaning
# 
# 
# **Part 3:** Building visualizations
# 
# **Part 4:** Evaluate and share results
# 
# <br/> 
# Follow the instructions and answer the questions below to complete the activity. Then, you will complete an Executive Summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work. 
# 
# 

# # **Visualize a story in Tableau and Python**

# # **PACE stages** 
# 
# 
# <img src="images/Pace.png" width="100" height="100" align=left>
# 
#    *        [Plan](#scrollTo=psz51YkZVwtN&line=3&uniqifier=1)
#    *        [Analyze](#scrollTo=mA7Mz_SnI8km&line=4&uniqifier=1)
#    *        [Construct](#scrollTo=Lca9c8XON8lc&line=2&uniqifier=1)
#    *        [Execute](#scrollTo=401PgchTPr4E&line=2&uniqifier=1)

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## PACE: Plan 
# 
# In this stage, consider the following questions where applicable to complete your code response:
# 1. Identify any outliers: 
# 
# 
# *   What methods are best for identifying outliers?
# *   How do you make the decision to keep or exclude outliers from any future models?
# 
# 

# To identify outliers is best to look at the extreme values using visualisations like a boxplot, for better analysing the distribution. The decision whether to keep or exclude them depends on their context and the nature of the outlier (error or legitimate value) and evaluation the sensitivity of the model tot his error.

# ### Task 1. Imports, links, and loading
# Go to Tableau Public
# The following link will help you complete this activity. Keep Tableau Public open as you proceed to the next steps. 
# 
# Link to supporting materials: 
# Tableau Public: https://public.tableau.com/s/ 
# 
# For EDA of the data, import the data and packages that would be most helpful, such as pandas, numpy and matplotlib. 
# 

# In[2]:


# Import packages and libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[3]:


# Load dataset into dataframe
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')


# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## PACE: Analyze 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### Task 2a. Data exploration and cleaning
# 
# Decide which columns are applicable
# 
# The first step is to assess your data. Check the Data Source page on Tableau Public to get a sense of the size, shape and makeup of the data set. Then answer these questions to yourself: 
# 
# Given our scenario, which data columns are most applicable? 
# Which data columns can I eliminate, knowing they won’t solve our problem scenario? 
# 
# Consider functions that help you understand and structure the data. 
# 
# *    head()
# *    describe()
# *    info()
# *    groupby()
# *    sortby()
# 
# What do you do about missing data (if any)? 
# 
# Are there data outliers? What are they and how might you handle them? 
# 
# What do the distributions of your variables tell you about the question you're asking or the problem you're trying to solve?
# 
# 
# 

# ==> ENTER YOUR RESPONSE HERE

# Start by discovering, using head and size. 

# In[4]:


df.head()


# In[8]:


df.size


# Use describe... 

# In[5]:


df.describe()


# And info. 

# In[6]:


df.info()


# ### Task 2b. Assess whether dimensions and measures are correct

# On the data source page in Tableau, double check the data types for the applicable columns you selected on the previous step. Pay close attention to the dimensions and measures to assure they are correct. 
# 
# In Python, consider the data types of the columns. *Consider:* Do they make sense? 

# Review the link provided in the previous activity instructions to create the required Tableau visualization. 

# ### Task 2c. Select visualization type(s)

# Select data visualization types that will help you understand and explain the data.
# 
# Now that you know which data columns you’ll use, it is time to decide which data visualization makes the most sense for EDA of the TLC dataset. What type of data visualization(s) would be most helpful? 
# 
# * Line graph
# * Bar chart
# * Box plot
# * Histogram
# * Heat map
# * Scatter plot
# * A geographic map
# 

# ==> ENTER YOUR RESPONSE HERE

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## PACE: Construct 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Construct stage.

# ### Task 3. Data visualization
# 
# You’ve assessed your data, and decided on which data variables are most applicable. It’s time to plot your visualization(s)!
# 

# ### Boxplots

# Perform a check for outliers on relevant columns such as trip distance and trip duration. Remember, some of the best ways to identify the presence of outliers in data are box plots and histograms. 
# 
# **Note:** Remember to convert your date columns to datetime in order to derive total trip duration.  

# In[7]:


# Convert data columns to datetime
#==> tpep_pickup_datetime	tpep_dropoff_datetime 03/25/2017 9:09:47 AM	

from datetime import datetime

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


# **trip distance**

# In[8]:


# Create box plot of trip_distance
plt.figure(figsize=(7,2))
plt.title("Trip Distance")
sns.boxplot(data=None, x=df.trip_distance, fliersize=1);


# In[24]:


# Create histogram of trip_distance
plt.hist(df.trip_distance)
plt.title("Trip distance histogram")
plt.show()


# **total amount**

# In[9]:


# Create box plot of total_amount
plt.figure(figsize=(7,2))
plt.title("Total Amount")
sns.boxplot(x=df.total_amount, fliersize=1);


# In[10]:


# Create histogram of total_amount
plt.hist(df.total_amount)
plt.title("Total Amount histogram")
plt.show()


# **tip amount**

# In[11]:


# Create box plot of tip_amount
plt.figure(figsize=(7,2))
plt.title("Tip Amount")
sns.boxplot(x=df.tip_amount, fliersize=1);


# In[40]:


# Create histogram of tip_amount
plt.hist(df.tip_amount, bins=range(0,25,1))
plt.title("Tip Amount histogram")
plt.show()
#XWe left out the maximum value of 200 for clarity


# **tip_amount by vendor**

# In[12]:


# Create histogram of tip_amount by vendor
plt.figure(figsize=(12, 6))

# Create a histogram using seaborn
sns.histplot(data=df, x= df.tip_amount, hue=df.VendorID, multiple='stack',bins=range(0,21,1), palette="pastel")
plt.title('Histogram of Tip Amount by Vendor')
plt.xlabel('Tip amount')
plt.ylabel('Frequency')

# Show the plot
plt.show()


# Next, zoom in on the upper end of the range of tips to check whether vendor one gets noticeably more of the most generous tips.

# In[13]:


# Create histogram of tip_amount by vendor for tips > $10 
plt.figure(figsize=(12, 6))

# Create a histogram using seaborn
sns.histplot(data=df, x= df.tip_amount, hue=df.VendorID, multiple='stack',bins=range(10,21,1), palette="pastel")
plt.title('Histogram of Tip Amount by Vendor')
plt.xlabel('Tip amount')
plt.ylabel('Frequency')

# Show the plot
plt.show()


# **Mean tips by passenger count**
# 
# Examine the unique values in the `passenger_count` column.

# In[14]:


df.passenger_count.describe()


# In[15]:


# Calculate mean tips by passenger_count
mean_tips_by_passenger_count = df.groupby(['passenger_count']).mean()[['tip_amount']]
mean_tips_by_passenger_count


# In[16]:


# Create bar plot for mean tips by passenger count
data=mean_tips_by_passenger_count.tail(-1)
ax=sns.barplot(data.index, y=data["tip_amount"])
ax.axhline(df['tip_amount'].mean(), ls='--', color='red', label='global mean')
plt.figure(figsize=(10, 6))
plt.show()


# In[ ]:





# **Create month and day columns**

# In[17]:


# Create a month column
# Create a day column
from datetime import datetime
df["Month"] = df.tpep_pickup_datetime.dt.month_name()
df["Day"] = df.tpep_pickup_datetime.dt.day_name()
df.head()


# **Plot total ride count by month**
# 
# Begin by calculating total ride count by month.

# In[18]:


# Get total number of rides for each month
rides_by_month = df["Month"].value_counts()
rides_by_month


# Reorder the results to put the months in calendar order.

# In[27]:


# Reorder the monthly ride list so months go in order
new_order= ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
rides_by_month = rides_by_month.reindex(index=new_order)
rides_by_month


# In[30]:


# Show the index
rides_by_month.index


# In[52]:


# Create a bar plot of total rides per month
data=rides_by_month
plt.figure(figsize=(15, 6))
ax=sns.barplot(data.index, y=rides_by_month)
ax.axhline(rides_by_month.mean(), ls='--', color='red', label='global mean')
ax.set_xticklabels(data.index, rotation=45)
plt.title('Total rides per month')


plt.show()


# **Plot total ride count by day**
# 
# Repeat the above process, but now calculate the total rides by day of the week.

# In[35]:


# Repeat the above process, this time for rides by day
rides_by_day = df["Day"].value_counts()
week= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
rides_by_day = rides_by_day.reindex(index=week)
rides_by_day


# In[54]:


# Create bar plot for ride count by day
data=rides_by_day
plt.figure(figsize=(15, 6))
ax=sns.barplot(data.index, y=rides_by_day)
ax.axhline(rides_by_day.mean(), ls='--', color='red', label='global mean')
ax.set_xticklabels(data.index, rotation=45)

plt.title("ride count by day")
plt.show()


# **Plot total revenue by day of the week**
# 
# Repeat the above process, but now calculate the total revenue by day of the week.

# In[46]:


# Repeat the process, this time for total revenue by day
revenue_by_day = df.groupby("Day").sum()[["total_amount"]]
revenue_by_day = revenue_by_day.reindex(index=week)
revenue_by_day


# In[55]:


# Create bar plot of total revenue by day
data=revenue_by_day
plt.figure(figsize=(15, 6))
ax=sns.barplot(data.index, y=data["total_amount"])
ax.axhline(data["total_amount"].mean(), ls='--', color='red', label='global mean')
ax.set_xticklabels(data.index, rotation=45)
plt.title("total revenue by day")

plt.show()


# **Plot total revenue by month**

# In[57]:


# Repeat the process, this time for total revenue by month
revenue_by_month = df.groupby("Month").sum()[["total_amount"]]
revenue_by_month = revenue_by_month.reindex(index=new_order)
revenue_by_month


# In[58]:


# Create a bar plot of total revenue by month
data=revenue_by_month
plt.figure(figsize=(15, 6))
ax=sns.barplot(data.index, y=data["total_amount"])
ax.axhline(data["total_amount"].mean(), ls='--', color='red', label='global mean')
ax.set_xticklabels(data.index, rotation=45)
plt.title("total revenue by month")

plt.show()


# #### Scatter plot

# You can create a scatterplot in Tableau Public, which can be easier to manipulate and present. If you'd like step by step instructions, you can review the following link. Those instructions create a scatterplot showing the relationship between total_amount and trip_distance. Consider adding the Tableau visualization to your executive summary, and adding key insights from your findings on those two variables.

# [Tableau visualization guidelines](https://docs.google.com/document/d/1pcfUlttD2Y_a9A4VrKPzikZWCAfFLsBAhuKuomjcUjA/template/preview)

# **Plot mean trip distance by drop-off location**

# In[61]:


# Get number of unique drop-off location IDs
DOLoc_count = df["DOLocationID"].value_counts()
DOLoc_count


# In[ ]:


#Nulber of unique DO locations is 216


# In[71]:


# Calculate the mean trip distance for each drop-off location
mean_distance = df.groupby("DOLocationID").mean()[["trip_distance"]]
mean_distance_desc = mean_distance.sort_values(by="trip_distance",ascending=False)
mean_distance_desc
# Sort the results in descending order by mean trip distance
#==> ENTER YOUR CODE HERE


# In[85]:


# Create a bar plot of mean trip distances by drop-off location in ascending order by distance
plt.figure(figsize=(14,6))
ax = sns.barplot(x=mean_distance_desc.index, 
                 y=mean_distance_desc['trip_distance'],
                 order=mean_distance_desc.index)
ax.set_xticklabels([])
ax.set_xticks([])
plt.title('Mean trip distance by drop-off location', fontsize=16);


# ## BONUS CONTENT
# 
# To confirm your conclusion, consider the following experiment:
# 1. Create a sample of coordinates from a normal distribution&mdash;in this case 1,500 pairs of points from a normal distribution with a mean of 10 and a standard deviation of 5
# 2. Calculate the distance between each pair of coordinates 
# 3. Group the coordinates by endpoint and calculate the mean distance between that endpoint and all other points it was paired with
# 4. Plot the mean distance for each unique endpoint

# In[ ]:


#BONUS CONTENT

#1. Generate random points on a 2D plane from a normal distribution
#==> ENTER YOUR CODE HERE

# 2. Calculate Euclidean distances between points in first half and second half of array
#==> ENTER YOUR CODE HERE

# 3. Group the coordinates by "drop-off location", compute mean distance
#==> ENTER YOUR CODE HERE

# 4. Plot the mean distance between each endpoint ("drop-off location") and all points it connected to
#==> ENTER YOUR CODE HERE


# **Histogram of rides by drop-off location**

# First, check to whether the drop-off locations IDs are consecutively numbered. For instance, does it go 1, 2, 3, 4..., or are some numbers missing (e.g., 1, 3, 4...). If numbers aren't all consecutive, the histogram will look like some locations have very few or no rides when in reality there's no bar because there's no location. 

# In[ ]:


# Check if all drop-off locations are consecutively numbered
#==> ENTER YOUR CODE HERE


# To eliminate the spaces in the historgram that these missing numbers would create, sort the unique drop-off location values, then convert them to strings. This will make the histplot function display all bars directly next to each other. 

# In[ ]:


#==> ENTER YOUR CODE HERE
# DOLocationID column is numeric, so sort in ascending order
#==> ENTER YOUR CODE HERE

# Convert to string
#==> ENTER YOUR CODE HERE

# Plot
#==> ENTER YOUR CODE HERE


# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## PACE: Execute 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Execute stage.

# ### Task 4a. Results and evaluation
# 
# Having built visualizations in Tableau and in Python, what have you learned about the dataset? What other questions have your visualizations uncovered that you should pursue? 
# 
# ***Pro tip:*** Put yourself in your client's perspective, what would they want to know? 
# 
# Use the following code fields to pursue any additional EDA based on the visualizations you've already plotted. Also use the space to make sure your visualizations are clean, easily understandable, and accessible. 
# 
# ***Ask yourself:*** Did you consider color, contrast, emphasis, and labeling?
# 
# 

# ==> ENTER YOUR RESPONSE HERE
# 
# I have learned .... 
# 
# My other questions are .... 
# 
# My client would likely want to know ... 
# 

# In[ ]:


#==> ENTER YOUR CODE HERE


# In[ ]:


#==> ENTER YOUR CODE HERE


# ### Task 4b. Conclusion
# *Make it professional and presentable*
# 
# You have visualized the data you need to share with the director now. Remember, the goal of a data visualization is for an audience member to glean the information on the chart in mere seconds.
# 
# *Questions to ask yourself for reflection:*
# Why is it important to conduct Exploratory Data Analysis? Why are the data visualizations provided in this notebook useful?
# 

# 
# EDA is important because ... 
# ==> ENTER YOUR RESPONSE HERE
# 
# 
# Visualizations helped me understand ..
# ==> ENTER YOUR RESPONSE HERE
# 

# You’ve now completed professional data visualizations according to a business need. Well done! 

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
