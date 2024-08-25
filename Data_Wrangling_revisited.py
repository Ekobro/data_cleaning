#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[1]:


# To get pandas runing in your system, 
import pandas as pd

#If you are runing jupyter notebook outside anaconda, you will not have pandas in it
#The run this; !pip install pandas
#the; import pandas as pd 


# In[2]:


df = pd.read_csv("C:/Users/EKOISO'S PC/Desktop/diabetes.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


# To inspect the structure and properties of the data
df.info()


# In[6]:


df.shape


# In[7]:


df.describe()


# In[8]:


# To transpose the .describe output
df.describe().T


# In[9]:


df.Outcome.unique()


# In[10]:


file = r"C:\Users\EKOISO'S PC\Desktop\One Campus\diabetesd.csv"
df1 = pd.read_csv(file)


# In[11]:


df1.info()


# In[12]:


df1.Outcome.unique()


# In[13]:


df.Outcome.unique()


# In[14]:


df2 = pd.read_csv(r"C:\Users\EKOISO'S PC\Desktop\diabetesd.csv")


# In[15]:


df2


# In[16]:


df2.Outcome.unique()


# In[17]:


# The above unique values for the outcome column indicated that there are mis-labeled data
#We can correct this by using the .replace funtion
#E.g: df2['Outcome'] = df['Outcome'].replace(ItemToBeReplaced, ItemToReplaceWith)


# In[18]:


df2['Outcome'] = df['Outcome'].replace("Falsee", "FALSE")


# In[19]:


df2.Outcome.unique()


# In[20]:


df2['Outcome'] = df2['Outcome'].replace(['1', '0', 'Truee', 'Falsee', "1'", "0'"], ["TRUE", "FALSE", "TRUE", "FALSE", 'TRUE', 'FALSE'])


# In[21]:


df2.Outcome.unique()


# In[22]:


df2


# In[23]:


# Inspect the data for mising values
df2.isna().sum()


# In[24]:


# To filter out all missing values
df3 = df2.fillna("99999")


# In[25]:


df2.info()


# In[26]:


df3.loc[df3["BMI"]== "99999"]


# In[27]:


df4 = df2.copy()


# In[28]:


df4.head(50)


# In[29]:


#Treating missing values using padding
df4['BloodPressure'] = df4['BloodPressure'].fillna(method = 'pad')


# In[30]:


#Treating missing values using backfill
df4['SkinThickness'] = df4['SkinThickness'].fillna(method = 'bfill')


# In[31]:


#Treating missing values using interpolation
df4['BMI'] = df4['BMI'].interpolate(method = 'linear', limit_direction = 'forward')


# In[ ]:





# In[32]:


df4.head(50)


# In[33]:


df4.isna().sum()


# In[34]:


df.Pregnancies.plot(kind = 'density')


# In[38]:


# Normally Distributed data
x =[2,4,6,8,10,12,14,16,18,20]


# In[39]:


pd.DataFrame(x).plot(kind ='density')


# In[ ]:





# In[ ]:





# In[ ]:




