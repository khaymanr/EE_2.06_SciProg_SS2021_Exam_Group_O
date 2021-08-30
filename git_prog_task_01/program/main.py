import datetime as dt
from datetime import date
import pandas as pd
from pandas.core.tools.datetimes import to_datetime
import seaborn as sns
import matplotlib.pyplot as plt
from to_dataframe import get_desired_year, prec_ts_to_df, vol_rr
from to_dataframe import prec_ts_to_df_hist
print("Libraries imported successfully")

# I downloaded the dataset and added the measurements needed (all from their respective Wikipedia pages).
# Here I already set the index as the river names.

dataset_path = "data/catchments.csv"
df = pd.read_csv(dataset_path, index_col="River")

# After that I loaded in the file using Pandas and renamed the columns as requested. 
# I set errors to raise so it would return me any errors encountered.

df = df.rename(columns={" Length (km)": "length", " Area (km^2)": "area"}, errors="raise")

# Just a check on how the dataframe is looking now, if everything is correct.

# print(df.head())

# Here is the code for plotting and showing both graphs. Top one is related to length, bottom one is related to area.
# On both I set different colours and rotated the river names 45 degrees, for aesthetic reasons.
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
ax1.bar(x=df.index, height=df['length'], color="red")
ax1.set_title("Catchment Length of each River")
ax1.set_xlabel("River Names")
ax1.set_ylabel("Length in m")

ax2.bar(x=df.index, height=df['area'], color="blue")
ax2.set_title("Catchment Area of each River")
ax2.set_xlabel("River Names")
ax2.set_ylabel("Area in $m^2$")

# plt.show()

'''plt.bar(x=df.index, height=df["length"], color="red")
plt.xticks(rotation=45)
plt.show()

plt.bar(x=df.index, height=df["area"], color="blue")
plt.xticks(rotation=45)
plt.show()'''

# For the analysis of the cumulative precipitation, code copied from the assignment page

# This interval catches the severe rain event.
date_from = pd.to_datetime("2021-07-12T12:00:00UTC")
date_to = pd.to_datetime("2021-07-15T12:00:00UTC")

# For the first station analysed
path_03499 = r"./data/DWD/stundenwerte_RR_03499_akt/"
filename_03499 = r"produkt_rr_stunde_20200222_20210824_03499.txt"
pfname_03499 = path_03499 + filename_03499
df_03499 = prec_ts_to_df(pfname_03499)
idx_03499 = (df_03499.index >= date_from) & (df_03499.index <= date_to)

# For the second station analysed
path_03591 = r"./data/DWD/stundenwerte_RR_03591_akt/"
filename_03591 = r"produkt_rr_stunde_20200222_20210824_03591.txt"
pfname_03591 = path_03591 + filename_03591
df_03591 = prec_ts_to_df(pfname_03591)
idx_03591 = (df_03591.index >= date_from) & (df_03591.index <= date_to)

# For the third station analysed
path_05717 = r"./data/DWD/stundenwerte_RR_05717_akt/"
filename_05717 = r"produkt_rr_stunde_20200223_20210825_05717.txt"
pfname_05717 = path_05717 + filename_05717
df_05717 = prec_ts_to_df(pfname_05717)
idx_05717 = (df_05717.index >= date_from) & (df_05717.index <= date_to)

# For the fourth station analysed
path_04219 = r"./data/DWD/stundenwerte_RR_04219_akt/"
filename_04219 = r"produkt_rr_stunde_20200222_20210824_04219.txt"
pfname_04219 = path_04219 + filename_04219
df_04219 = prec_ts_to_df(pfname_04219)
idx_04219 = (df_04219.index >= date_from) & (df_04219.index <= date_to)

# For the fifth station analysed
path_07378 = r"./data/DWD/stundenwerte_RR_07378_akt/"
filename_07378 = r"produkt_rr_stunde_20200222_20210824_07378.txt"
pfname_07378 = path_07378 + filename_07378
df_07378 = prec_ts_to_df(pfname_07378)
idx_07378 = (df_07378.index >= date_from) & (df_07378.index <= date_to)

# Extracting the R1 column from all dataframes and changing the name
df_r1_03499 = df_03499[['r1']].rename(columns={'r1' : '03499'})
df_r1_03591 = df_03591[['r1']].rename(columns={'r1' : '03591'})
df_r1_05717 = df_05717[['r1']].rename(columns={'r1' : '05717'})
df_r1_04219 = df_04219[['r1']].rename(columns={'r1' : '04219'})
df_r1_07378 = df_07378[['r1']].rename(columns={'r1' : '07378'})

# Checking if the dataframe is correct
# print(df_r1_03499.head())

# Concatenation makes more sense here than merging. I can join everyone in one line, instead of two at a time
df_RR = pd.concat([df_r1_03499, df_r1_03591, df_r1_05717, df_r1_04219, df_r1_07378], axis=1)

#leaving everything inbetween the correct timeframe 
df_RR = df_RR[df_RR.index >= date_from]
df_RR = df_RR[df_RR.index <= date_to]
index_df_RR = (df_RR.index >= date_from) & (df_RR.index <= date_to)

'''
# Plotting the diagram
df_RR.plot.bar(
    figsize=(18,8),
    grid=True, 
    color={
        '03499': 'red',
        '03591': 'green',
        '04219': 'orange',
        '05717': 'blue',
        '07378': 'cyan'
    }, 
    title="Precipitation Rate at Five DWD Stations, in Five River Catchments (Ruhr, Rur, Ahr, Wupper, Erft)",
    xlabel="Measurement Timestamps",
    ylabel="Precipitation Rate in mm/hr",
    width=2
)

# Adjusting the plot position and legend so everything can be properly seen
plt.subplots_adjust(bottom=0.3, top=0.973)
plt.legend([
        'Station 03499 (Ruhr)',
        'Station 03591 (Rur)',
        'Station 04219 (Ahr)',
        'Station 05717 (Wupper)',
        'Station 07378 (Erft)'
])

# Showing the graphs
plt.show()
'''
'''
# Using seaborn for the heatmap
plt.figure(figsize=(12,8))
sns.heatmap(
    df_RR
)
plt.title("Heatmap of the Rain Rate in each of the Five Stations")
plt.xlabel("Measurement Timestamps")
plt.ylabel("Rain Rate in Each Station in mm")
plt.legend([
        'Station 03499 (Ruhr)',
        'Station 03591 (Rur)',
        'Station 04219 (Ahr)',
        'Station 05717 (Wupper)',
        'Station 07378 (Erft)'
])
plt.subplots_adjust(
    left=0.265,
    right=1
)
plt.show()


# Finding the cumulative precipitation of the five catchment areas
cumsum = df_RR.cumsum()
# Plotting of the line graphs
cumsum.plot.line(
    figsize=(12,8),
    grid=True,
    color={
        '03499': 'red',
        '03591': 'green',
        '04219': 'orange',
        '05717': 'blue',
        '07378': 'cyan'
        },
        title="Cumulative Precipitation in Each of the Five Stations",
        xlabel="Measurement Timestamps",
        ylabel="Cumulative Precipitation in mm of Rain"        
)

# Legend so the stations are better identified
plt.legend([
        'Station 03499 (Ruhr)',
        'Station 03591 (Rur)',
        'Station 04219 (Ahr)',
        'Station 05717 (Wupper)',
        'Station 07378 (Erft)'
])

plt.show()


Okay so. There are null values in one of the stations, even in the correct period, but it was that or just not having any measurements in some days 
(The stations' data for that catchment were not very good). So I left it there and there are gaps in the lines, because of the null values. I tried
to fix them in every way, but apparently I can't, unless I assume different values in those positions, which I won't do. Oh well. 
'''

# Calculating total cumulative precipitation for the cathment areas to add to the csv file
# print(df_RR.cumsum(axis=0))


# Getting the relevant data for the historical analysis
hist_date_from = pd.to_datetime("1961-07-01")
hist_date_to = pd.to_datetime("1990-12-01")
hist_july = pd.to_datetime("")

# Included in the 'to_dataframe' module a modified function to use with the historical data
path_hist_05717 = r"./data/DWD/historical/monatswerte_KL_05717_19070101_20201231_hist/"
filename_hist_05717 = r"produkt_klima_monat_19070101_20201231_05717.txt"
pfname_hist_05717 = path_hist_05717 + filename_hist_05717
df_hist_05717 = prec_ts_to_df_hist(pfname_hist_05717)
df_hist_05717 = df_hist_05717[['mess_datum_ende','mo_rr']]

# Checking if the dataframe parsed correctly
# print(df_hist_05717.head())


# Getting only the values for the months of July
df_hist_05717 = df_hist_05717[df_hist_05717.index >= hist_date_from]
df_hist_05717 = df_hist_05717[df_hist_05717.index <= hist_date_to]

# Checking if my timeframe is correct
# print(df_hist_05717)

# Parsing through to get the months I want (using the function I created in the other module)
df_hist_05717
#print(df_temp.index)

temp_hist = []

for date in df_hist_05717.index:
    if date.month == 7:
        temp_hist.append(df_hist_05717.loc[date])
    
    
df_hist_july_rr = pd.DataFrame(temp_hist)

# Checking as always
# print(df_hist_july_rr.values)
    
# Analysing the values we have the ratio of event and average precipitation
max_cumsum = df_hist_july_rr['mo_rr'].cumsum().iloc[-1]
avg_rr = max_cumsum / len(df_hist_july_rr)
# print(avg_rr)

# With the average rainfall in mm, we can analyse the ratio
temp_list = []
# Iterating to find every value above the average
for value in df_hist_july_rr['mo_rr']:
    if value > avg_rr:
        temp_list.append(value)

# print(len(temp_list))

# Ratio would then be events divided by total
ratio = len(temp_list) / len(df_hist_july_rr)
# print(ratio)

# For the annual precipitation, I created a function on the other module
# It's the ugliest function I ever created
# Gods of Programming forgive me for I'm about to sin
list1961 = []
get_desired_year(df_hist_05717, 1961, list1961)
list1962 = []
get_desired_year(df_hist_05717, 1962, list1962)
list1963 = []
get_desired_year(df_hist_05717, 1963, list1963)
list1964 = []
get_desired_year(df_hist_05717, 1964, list1964)
list1965 = []
get_desired_year(df_hist_05717, 1965, list1965)
list1966 = []
get_desired_year(df_hist_05717, 1966, list1966)
list1967 = []
get_desired_year(df_hist_05717, 1967, list1967)
list1968 = []
get_desired_year(df_hist_05717, 1968, list1968)
list1969 = []
get_desired_year(df_hist_05717, 1969, list1969)
list1970 = []
get_desired_year(df_hist_05717, 1970, list1970)
list1971 = []
get_desired_year(df_hist_05717, 1971, list1971)
list1972 = []
get_desired_year(df_hist_05717, 1972, list1972)
list1973 = []
get_desired_year(df_hist_05717, 1973, list1973)
list1974 = []
get_desired_year(df_hist_05717, 1974, list1974)
list1975 = []
get_desired_year(df_hist_05717, 1975, list1975)
list1976 = []
get_desired_year(df_hist_05717, 1976, list1976)
list1977 = []
get_desired_year(df_hist_05717, 1977, list1977)
list1978 = []
get_desired_year(df_hist_05717, 1978, list1978)
list1979 = []
get_desired_year(df_hist_05717, 1979, list1979)
list1980 = []
get_desired_year(df_hist_05717, 1980, list1980)
list1981 = []
get_desired_year(df_hist_05717, 1981, list1981)
list1982 = []
get_desired_year(df_hist_05717, 1982, list1982)
list1983 = []
get_desired_year(df_hist_05717, 1983, list1983)
list1984 = []
get_desired_year(df_hist_05717, 1984, list1984)
list1985 = []
get_desired_year(df_hist_05717, 1985, list1985)
list1986 = []
get_desired_year(df_hist_05717, 1986, list1986)
list1987 = []
get_desired_year(df_hist_05717, 1987, list1987)
list1988 = []
get_desired_year(df_hist_05717, 1988, list1988)
list1989 = []
get_desired_year(df_hist_05717, 1989, list1989)
list1990 = []
get_desired_year(df_hist_05717, 1990, list1990)


# Creating a database with all the data
idx_hist_year = pd.Index([
    "1961", "1962",
    "1963", "1964",
    "1965", "1966",
    "1967", "1968",
    "1969", "1970",
    "1971", "1972",
    "1973", "1974",
    "1975", "1976",
    "1977", "1978",
    "1979", "1980",
    "1981", "1982",
    "1983", "1984",
    "1985", "1986",
    "1987", "1988",
    "1989", "1990"
    ],
    name="year"
    )

df_hist_year = pd.DataFrame([
    list1961, list1962,
    list1963, list1964, 
    list1965, list1966,
    list1967, list1968,
    list1969, list1970,
    list1971, list1972,
    list1973, list1974,
    list1975, list1976,
    list1977, list1978,
    list1979, list1980,
    list1981, list1982,
    list1983, list1984,
    list1985, list1986,
    list1987, list1988,
    list1989, list1990 
    ], 
    index=idx_hist_year,
    columns=[
    "January", "February",
    "March", "April",
    "May", "June",
    "July", "August",
    "September", "October",
    "November", "December"
    ])

# Check, check, check
# print(df_hist_year.head())

# Getting the cumulative precipitation of each year
# First one doesn't have all values for the year so I have to pick it manually. Rest is fine, I checked
# Making it into a series
avg_hist = pd.Series([df_hist_year.loc["1961"].cumsum().loc["June"],
            df_hist_year.loc["1962"].cumsum().iloc[-1],
            df_hist_year.loc["1963"].cumsum().iloc[-1],
            df_hist_year.loc["1964"].cumsum().iloc[-1],
            df_hist_year.loc["1965"].cumsum().iloc[-1],
            df_hist_year.loc["1966"].cumsum().iloc[-1],
            df_hist_year.loc["1967"].cumsum().iloc[-1],
            df_hist_year.loc["1968"].cumsum().iloc[-1],
            df_hist_year.loc["1969"].cumsum().iloc[-1],
            df_hist_year.loc["1970"].cumsum().iloc[-1],
            df_hist_year.loc["1971"].cumsum().iloc[-1],
            df_hist_year.loc["1972"].cumsum().iloc[-1],
            df_hist_year.loc["1973"].cumsum().iloc[-1],
            df_hist_year.loc["1974"].cumsum().iloc[-1],
            df_hist_year.loc["1975"].cumsum().iloc[-1],
            df_hist_year.loc["1976"].cumsum().iloc[-1],
            df_hist_year.loc["1977"].cumsum().iloc[-1],
            df_hist_year.loc["1978"].cumsum().iloc[-1],
            df_hist_year.loc["1979"].cumsum().iloc[-1],
            df_hist_year.loc["1980"].cumsum().iloc[-1],
            df_hist_year.loc["1981"].cumsum().iloc[-1],
            df_hist_year.loc["1982"].cumsum().iloc[-1],
            df_hist_year.loc["1983"].cumsum().iloc[-1],
            df_hist_year.loc["1984"].cumsum().iloc[-1],
            df_hist_year.loc["1985"].cumsum().iloc[-1],
            df_hist_year.loc["1986"].cumsum().iloc[-1],
            df_hist_year.loc["1987"].cumsum().iloc[-1],
            df_hist_year.loc["1988"].cumsum().iloc[-1],
            df_hist_year.loc["1989"].cumsum().iloc[-1],
            df_hist_year.loc["1990"].cumsum().iloc[-1]
            ])


# Check, check, check
# print(avg_hist.values)
avg_hist_rr = (avg_hist.cumsum().iloc[-1]) / len(avg_hist)
# print(avg_hist_rr)
# print(avg_hist.cumsum().iloc[-1])

# For the next task:

# For the sake of normalization I will also rename the column of max cumulative rain rate
df = df.rename(columns={" Max Cumulative Precipitation (mm)": "max_rr"})

# Created a function in the other module for calculating the area
vol_rr_rur = vol_rr(df['area'].loc['Rur'], df['max_rr'].loc['Rur'])
vol_rr_erft = vol_rr(df['area'].loc['Erft'], df['max_rr'].loc['Erft'])
vol_rr_ahr = vol_rr(df['area'].loc['Ahr'], df['max_rr'].loc['Ahr'])
vol_rr_wupper = vol_rr(df['area'].loc['Wupper'], df['max_rr'].loc['Wupper'])
vol_rr_ruhr = vol_rr(df['area'].loc['Ruhr'], df['max_rr'].loc['Ruhr'])

# Checking the values
# print(vol_rr_rur, vol_rr_erft, vol_rr_ahr, vol_rr_wupper, vol_rr_ruhr)

array = df["Global tilt  W*m-2*nm-1"]
print(array)



