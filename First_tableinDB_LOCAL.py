#!/usr/bin/env python
# coding: utf-8

# In[53]:


get_ipython().system('pip install mysql-connector-python')


# In[54]:


import mysql.connector


# In[55]:


cnx = mysql.connector.connect(user='root', password='**********', host='localhost', database='myfirst_proj')


# In[56]:


# Now we have to create a new database, to do that we have to create a cursor
cursor = cnx.cursor()
# With the follow code we create a new database
database_name = 'dbi3i_jupyt'
cursor.execute(f" CREATE DATABASE {database_name}")


# In[57]:


# comando per rendere le modifiche permanenti
cnx.commit()


# In[58]:


table_name = 'sti3iudentss'
create_table_query = '''
    CREATE TABLE {} (
        studid int,
        name varchar(40),
        age int,
        gender varchar(40),
        subject varchar(40),
        marks int
    )
'''.format(table_name)


# In[59]:


cursor.execute(create_table_query)


# In[60]:


# comando per rendere le modifiche permanenti
cnx.commit()


# In[61]:


insert_query = '''
    INSERT INTO sti3iudentss  (studid, name, age, gender, subject, marks)
    VALUES (1,"RAJ", 23, "male", "pyt", 85),
           (1,"weJ", 27, "female", "pyt", 75)
'''


# In[62]:


import mysql.connector
import pandas as pd

# Connessione al database MySQL
cnx = mysql.connector.connect(user='root', password='***********', host='localhost', database='myfirst_proj')

# Esecuzione della query per ottenere i dati dalla tabella
query = "SELECT * FROM sti3iudentss"
cursor = cnx.cursor()
cursor.execute(query)

# Ottenere i risultati della query
result = cursor.fetchall()

# Creazione del DataFrame utilizzando i risultati
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Visualizzazione del DataFrame
df.head()

