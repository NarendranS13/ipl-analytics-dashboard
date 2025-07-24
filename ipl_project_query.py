import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect("E:\de_projects\IPL.db")
    cursor = conn.cursor()
    print("Connection Successfull")
except Exception as e:
    print(e)

### Get list of tables

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(f"Tables: {tables}")


#### Select from a table 

cursor.execute("SELECT * FROM batters_overall_stat LIMIT 10")
rows = cursor.fetchall()
# for row in rows:
#     print(row)

#### Opening the Table on an Dataframe

query = "SELECT * FROM batters_overall_stat"
df = pd.read_sql_query(query,conn)
# print(df.head(20))

#### Dynamic Querying 

def get_top_run_scorers(total_runs):
    query2 = f"""
    SELECT DISTINCT batsman, total_runs, average FROM batters_stat_df
    WHERE total_runs >= {total_runs}
    ORDER BY total_runs DESC
    LIMIT 15
    """

    return pd.read_sql_query(query2, conn)

print(get_top_run_scorers(2500))

conn.close()
