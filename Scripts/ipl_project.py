import sqlite3
import pandas as pd
# batters_path = "ipl_datasets\Players.xlsx"
players_path = "ipl_datasets\Players.xlsx"
batters_stat_path = "ipl_datasets\most_runs_average_strikerate.csv"

players_df = pd.read_excel(players_path)
batters_stat_df = pd.read_csv(batters_stat_path)

####### Dataframe Check up Queries.

# print(batters_stat_df.head(10))
# print(batters_stat_df.describe())

avg = batters_stat_df['average'].describe()

# print(avg)

# print(players_df.head(5))

# print(players_df.describe())

# print(players_df.info())
# print(players_df['Country'].tail(15))

####### Replace the Records, where Country name is not available. Replace them with Unknown.
####### Remove the Records where DOB is not available
####### Corrected the Name of the Country 
####### Converted the playername into lowercase.

nan_count = players_df['Country'].isna().sum()
non_nan_count = players_df['Country'].notna().sum()

print(f"NaN records : {nan_count}")
print(f"Non-NaN records: {non_nan_count}")


### Print records where country name is not na
# print(players_df[players_df['Country'].notna()])

### Print records where country name is na
# print(players_df[players_df['Country'].isna()])


####### Filling the na with Unknown values
players_df['Country'] = players_df['Country'].fillna('Unknown')

##### Checking whether unknown values is still there.
# print(players_df['Country'].isna().sum())


#### Checking DOB having na values
# print(players_df['DOB'].isna().sum())

# players_df['DOB'] = players_df['DOB'].dropna()

##### Dropping the records where DOB is na

players_df = players_df.dropna(subset=['DOB'])

### To check distinct values in an columns

# print(players_df['Country'].unique())

### To replace the country Zimbabwea with Zimbabwe

players_df['Country'] = players_df['Country'].replace('Zimbabwea','Zimbabwe')


players_df['Player_Name'] = players_df['Player_Name'].str.strip().str.lower()
# print(players_df.head(10))

### File saved as CSV.
# players_df.to_csv("cleaned_players.csv", index = False)


####### Batters_Stats DF 
####### Converting the Batsman name into lowercase
####### Rounding the Average and Strikerate to 2 decimal points.

# print(batters_stat_df.head())

# print(batters_stat_df['total_runs'].isna().sum())

batters_stat_df['batsman'] = batters_stat_df['batsman'].str.strip().str.lower()

batters_stat_df[['average','strikerate']] = batters_stat_df[['average','strikerate']].round(2)

# print(batters_stat_df.head(5))

# batters_stat_df.to_csv("cleaned_players_stat.csv",index = False)


print(players_df.head(5))
print(batters_stat_df.head(5))

##### Merging the two DataFrames using the Batsman name as join key


final_df = pd.merge(
    players_df,
    batters_stat_df[['batsman', 'total_runs', 'average', 'strikerate']],
    left_on = 'Player_Name',
    right_on = 'batsman',
    how = 'left'
)

final_df = final_df[['Player_Name', 'DOB', 'Batting_Hand', 'Bowling_Skill', 'Country',
                     'total_runs', 'average', 'strikerate']]

# final_df.to_excel('players_statistics.xlsx', index = False)




### Saving them in the sqlite DB

###Connect or create an IPL DB
conn = sqlite3.connect("IPL.db")

### Save players Dataframe as an table

players_df.to_sql("players_df", conn, if_exists = 'replace', index = False)

### Save the players stats Dataframe as an Table

batters_stat_df.to_sql("batters_stat_df", conn, if_exists = 'replace', index = False)

### Save the merge table

final_df.to_sql("batters_overall_stat", conn, if_exists = 'replace', index = False)

### Test one

print(pd.read_sql("SELECT * FROM batters_overall_stat LIMIT 5", conn))

conn.close()