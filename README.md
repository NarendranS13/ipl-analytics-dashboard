# ipl-analytics-dashboard
ETL Project using Python, Pandas, SQLite and PBI


### Datasets Link. (Extract)
Kaggle: https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set/data

#### Python, Pandas, SQLite3 and PowerBI.

##### Transformation
Players.xlsx (File)

1. Replacing the value of Country name na with Unknown.
2. Dropped Records of the Players whose DOB is not available
3. Corrected the Country name from Zimbabwae to Zimbabwe
4. Converted the Players name to lowercase.

most_runs_average_strikerate.csv (File)

1. Converted the players name to lowercase.
2. Rounded the decimal points to 2 for average and strikerate.

Merging Players.xlsx and most_runs_average_strikerate.csv

1. Merging the Tables on the basis of name using Left Join.

##### Load

1. cleaned_players.csv
2. cleaned_palyers_stat.csv

SQLITE3 DB
1. IPL_DB created for storing the Table.
2. Use DBeaver for Viewing the Tables.

##### Querying the Tables using Pandas.
1. Demonstrated the Querying and Dynamic Querying using Pandas

##### Visualization
1. Utlizied the PowerBI to showcase the data.
2. Utilized the Merged Table.
3. Created the Line and Clustered Column Chart where X axis is Players & Y-Axis Total Runs & Y-Axis Line Strike Rate
4. Added Slicers for Country, Batter Hand and Player Filter.

<img width="1178" height="662" alt="image" src="https://github.com/user-attachments/assets/ab2dfc8e-87c9-40fc-afde-a766dc9673c3" />

