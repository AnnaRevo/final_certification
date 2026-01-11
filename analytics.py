import pandas as pd 
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt


conn = psycopg2.connect(

    host="localhost",
    
    database="postgres",  # имя вашей базы

    user="postgres",

    password="1234",

    port=5432

)

cur = conn.cursor()


cur.execute("SELECT * FROM manning_table ORDER BY id")

sql_query = pd.read_sql("SELECT * FROM manning_table", conn)

df = pd.DataFrame(sql_query)

print(df)

def barplot_gender_compare():
    data = df
    if data.empty:
        print(f"Нет данных для диаграммы")
        return
    sns.barplot(data=df, x='sex', y ='salary')
    plt.title ("Сравнение дохода по полу")
    plt.show()
barplot_gender_compare()

def barplot_branch_compare():
    data = df
    if data.empty:
        print(f"Нет данных для диаграммы")
        return
    sns.barplot(data=df, x='branch', y ='salary')
    plt.title ("Сравнение дохода по филиалам")
    plt.show()
barplot_branch_compare()