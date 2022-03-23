#!/usr/bin/env python
# coding: utf-8

# Step 1. Ensure that you have the dataset file named `transactions.csv` in the current directory.
# 
# The dataset is a subset of https://www.kaggle.com/ealaxi/paysim1/version/2 which was originally generated as part of the following research:
# 
# E. A. Lopez-Rojas , A. Elmir, and S. Axelsson. "PaySim: A financial mobile money simulator for fraud detection". In: The 28th European Modeling and Simulation Symposium-EMSS, Larnaca, Cyprus. 2016

# Step 2. Complete the following exercises.
# 
# 0. Read the dataset (`transactions.csv`) as a Pandas dataframe. Note that the first row of the CSV contains the column names.
# 
# 0. Return the column names as a list from the dataframe.
# 
# 0. Return the first k rows from the dataframe.
# 
# 0. Return a random sample of k rows from the dataframe.
# 
# 0. Return a list of the unique transaction types.
# 
# 0. Return a Pandas series of the top 10 transaction destinations with frequencies.
# 
# 0. Return all the rows from the dataframe for which fraud was detected.
# 
# 0. Bonus. Return a dataframe that contains the number of distinct destinations that each source has interacted with to, sorted in descending order. You will find [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) and [agg](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.aggregate.html) useful. The predefined aggregate functions are under `pandas.core.groupby.GroupBy.*`. See the [left hand column](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.nunique.html).

# Use the empty cell to test the exercises. If you modify the original `df`, you can rerun the cell containing `exercise_0`.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def exercise_0(file):
    pass

def exercise_1(df):
    pass

def exercise_2(df, k):
    pass

def exercise_3(df, k):
    pass

def exercise_4(df):
    pass

def exercise_5(df):
    pass

def exercise_6(df):
    pass

def exercise_7(df):
    pass

def visual_1(df):
    pass

def visual_2(df):
    pass

def exercise_custom(df):
    pass
    
def visual_custom(df):
    pass


# In[2]:


df = pd.read_csv("transactions.csv")


# In[3]:


df.columns


# In[4]:


df.head()


# In[5]:


df.sample(5)


# In[6]:


df.type.unique()


# In[7]:


df.nameDest.value_counts().head(10)


# In[8]:


df[df.isFraud == 1]


# In[9]:


df.groupby("nameDest")["newbalanceDest"].agg("mean").sort_values(ascending=False)


# Create graphs for the following. 
# 1. Transaction types bar chart, Transaction types split by fraud bar chart
# 1. Origin account balance delta v. Destination account balance delta scatter plot for Cash Out transactions
# 
# Ensure that the graphs have the following:
#  - Title
#  - Labeled Axes
#  
# The function plot the graph and then return a string containing a short description explaining the relevance of the chart.

# In[10]:


sns.countplot(x=df.type)
plt.title("Transaction types bar chart")
plt.show()


# In[11]:


sns.countplot(x=df.type, hue=df.isFraud)
plt.title("Transaction types bar chart")
plt.show()


# In[12]:


# def visual_1(df):
#     def transaction_counts(df):
#         # TODO
#         pass
#     def transaction_counts_split_by_fraud(df):
#         # TODO
#         pass

#     fig, axs = plt.subplots(2, figsize=(6,10))
#     transaction_counts(df).plot(ax=axs[0], kind='bar')
#     axs[0].set_title('TODO')
#     axs[0].set_xlabel('TODO')
#     axs[0].set_ylabel('TODO')
#     transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
#     axs[1].set_title('TODO')
#     axs[1].set_xlabel('TODO')
#     axs[1].set_ylabel('TODO')
#     fig.suptitle('TODO')
#     fig.tight_layout(rect=[0, 0.03, 1, 0.95])
#     for ax in axs:
#       for p in ax.patches:
#           ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
#     return 'TODO'

# visual_1(df)


# In[13]:


# def visual_2(df):
#     def query(df):
#         # TODO
#         pass
#     plot = query(df).plot.scatter(x='TODO',y='TODO')
#     plot.set_title('TODO')
#     plot.set_xlim(left=-1e3, right=1e3)
#     plot.set_ylim(bottom=-1e3, top=1e3)
#     return 'TODO'

# visual_2(df)


# Use your newly-gained Pandas skills to find an insight from the dataset. You have full flexibility to go in whichever direction interests you. Please create a visual as above for this query. `visual_custom` should call `exercise_custom`.

# In[14]:


def exercise_custom(df):
    # TODO
    pass
    
def visual_custom(df):
    # TODO
    pass


# Submission
# 
# 1. Copy the exercises into `task1.py`.
# 2. Upload `task1.py` to Forage.

# All done!
# 
# Your work will be instrumental for our team's continued success.
