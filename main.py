# CodeGrade step0 - Run without changes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandasql import sqldf

# CodeGrade step1
df = pd.read_csv('titanic.csv', index_col=0)
df.head()

# CodeGrade step2
women_and_children_df = df.loc[(df['Sex'] == 'female') | (df['Age'] <= 15)]
adult_males_df = df.loc[(df['Sex'] == 'male') & (df['Age'] > 15)]

# CodeGrade step3
df['Pclass'] = pd.to_numeric(df['Pclass'], errors='coerce')
first_class_df = df.loc[df['Pclass'] == 1]
second_third_class_df = df.loc[df['Pclass'] != 1]

# CodeGrade step4
query_string = 'PassengerId >= 500'
high_passenger_number_df = df.query(query_string)
high_passenger_number_df.head()

# CodeGrade step5
query_string = "Sex == 'female' or Age <= 15"
female_children_df = df.query(query_string)
female_children_df.head()

# CodeGrade step6
df = df.eval('Age_x_Fare = Age * Fare')
df.head()

# CodeGrade step7
pysqldf = lambda q: sqldf(q, globals())

# CodeGrade step8
query1 = """
SELECT Name
FROM df
LIMIT 10
"""
passenger_names = pysqldf(query1)
passenger_names

# CodeGrade step9
query2 = """
SELECT Name, Fare
FROM df
WHERE Sex = 'male'
AND Survived = 1
LIMIT 30
"""
sql_surviving_males = pysqldf(query2)
sql_surviving_males

# CodeGrade step10
query3 = """
SELECT Pclass, COUNT(*) AS 'Count(*)'
FROM df
WHERE Sex = 'female'
AND Survived = 1
GROUP BY Pclass
"""
query4 = """
SELECT Pclass, COUNT(*) AS 'Count(*)'
FROM df
WHERE Sex = 'female'
AND Survived = 0
GROUP BY Pclass
"""
survived_females_by_pclass_df = pysqldf(query3)
died_females_by_pclass_df = pysqldf(query4)
