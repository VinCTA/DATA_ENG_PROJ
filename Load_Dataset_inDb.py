#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[2]:


get_ipython().system('pip install pandas')


# In[3]:


import mysql.connector
import pandas as pd 
# pandas serve leggere i dati e caricarli el database


# In[5]:


def create_database():
    cnx = mysql.connector.connect(user="root", password="Vaffanculo99.", host="localhost", database= "myfirst_proj")
    cnx.autocommit = True
    cur = cnx.cursor()
    #cur = conn.cursor(): This line creates a cursor object cur using the connection object conn. 
    #The cursor is used to execute mySQL and PostgreSQL statements and retrieve results from the database.
    # Now o create a database, you need to execute an SQL statement using the cursor object.
    cur.execute("DROP DATABASE IF EXISTS accounts")
    cur.execute("CREATE DATABASE accounts")
    cnx.close()
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vaffanculo99.",
        database="accounts"
    )
    cur = cnx.cursor()
    
    return cur, conn
    
    


# In[6]:


def drop_tab(cur, cnx):
    drop_tab_queries = [
        "DROP TABLE IF EXISTS table1",
        "DROP TABLE IF EXISTS table2",
        # Add more DROP TABLE queries as needed
    ]
    
    for query in drop_tab_queries:
        cur.execute(query)
    
    cnx.commit()


# In[7]:


def create_tab(cur, cnx):
    for query in create_tab_queries:
        cur.execute(query)
        cnx.commit()


# In[8]:


import os 


# In[9]:


file_path = os.path.abspath('ds_sal_div.csv')
print(file_path)
# attenzione il percorso può essere sbagliato, per vedere bene il percorso
# vai sul file di interesse e cerca il percorso


# In[20]:


AccSale = pd.read_csv(r'C:\Users\vinct\Desktop\ds_salaries.csv') 


# In[21]:


AccSale.head()


# In[22]:


# Now, we want choose some columns
AccSale_clean= AccSale[['work_year','experience_level','job_title','salary','salary_currency']]


# In[23]:


AccSale_clean.head()


# In[24]:


# Now, we want work on other dataset
Accountmelb = pd.read_csv(r'C:\Users\vinct\Desktop\melb_data.csv')


# In[26]:


Accountmelb.head()


# In[27]:


Accountmelb.columns


# In[28]:


#Let see how to drop change a column, using the pandas function .drop
# axis = 0 is a raw, axis = 1 is a columnn
Accountmelb = Accountmelb.drop(['Type'], axis=1)


# In[29]:


Accountmelb.head()


# In[ ]:




