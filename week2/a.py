import pandas as pd

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 2000)

df_exams = pd.read_csv('StudentsPerformance.csv')
print(df_exams['math score'].mean())
print(df_exams['reading score'].mean())
print(df_exams['writing score'].mean())