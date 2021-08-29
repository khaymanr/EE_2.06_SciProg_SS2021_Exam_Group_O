import pandas as pd
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
from functions import df_norm


data_path_1078 = r"./data/jahreswerte_KL_01078_19400101_20201231_hist/"
data_file_1078 = r"produkt_klima_jahr_19400101_20201231_01078.txt"
file_path_1078 = data_path_1078 + data_file_1078
df_1078 = df_norm(file_path_1078)

data_path_1300 = r"./data/jahreswerte_KL_01300_19310101_20201231_hist/"
data_file_1300 = r"produkt_klima_jahr_19310101_20201231_01300.txt"
file_path_1300 = data_path_1300 + data_file_1300
df_1300 = df_norm(file_path_1300)

data_path_1303 = r"./data/jahreswerte_KL_01303_18880101_20201231_hist/"
data_file_1303 = r"produkt_klima_jahr_18880101_20201231_01303.txt"
file_path_1303 = data_path_1303 + data_file_1303
df_1303 = df_norm(file_path_1303)

data_path_1327 = r"./data/jahreswerte_KL_01327_19370101_20201231_hist/"
data_file_1327 = r"produkt_klima_jahr_19370101_20201231_01327.txt"
file_path_1327 = data_path_1327 + data_file_1327
df_1327 = df_norm(file_path_1327)

data_path_1590 = r"./data/jahreswerte_KL_01590_19370101_20201231_hist/"
data_file_1590 = r"produkt_klima_jahr_19370101_20201231_01590.txt"
file_path_1590 = data_path_1590 + data_file_1590
df_1590 = df_norm(file_path_1590)

data_path_2110 = r"./data/jahreswerte_KL_02110_19380101_20201231_hist/"
data_file_2110 = r"produkt_klima_jahr_19380101_20201231_02110.txt"
file_path_2110 = data_path_2110 + data_file_2110
df_2110 = df_norm(file_path_2110)

data_path_2483 = r"./data/jahreswerte_KL_02483_19290101_20201231_hist/"
data_file_2483 = r"produkt_klima_jahr_19290101_20201231_02483.txt"
file_path_2483 = data_path_2483 + data_file_2483
df_2483 = df_norm(file_path_2483)

data_path_2497 = r"./data/jahreswerte_KL_02497_19370101_20201231_hist/"
data_file_2497 = r"produkt_klima_jahr_19370101_20201231_02497.txt"
file_path_2497 = data_path_2497 + data_file_2497
df_2497 = df_norm(file_path_2497)

data_path_2629 = r"./data/jahreswerte_KL_02629_18510101_20201231_hist/"
data_file_2629 = r"produkt_klima_jahr_18510101_20201231_02629.txt"
file_path_2629 = data_path_2629 + data_file_2629
df_2629 = df_norm(file_path_2629)

data_path_2698 = r"./data/jahreswerte_KL_02968_19030101_20201231_hist/"
data_file_2698 = r"produkt_klima_jahr_19030101_20201231_02968.txt"
file_path_2698 = data_path_2698 + data_file_2698
df_2698 = df_norm(file_path_2698)

data_path_4371 = r"./data/jahreswerte_KL_04371_19310101_20201231_hist/"
data_file_4371 = r"produkt_klima_jahr_19310101_20201231_04371.txt"
file_path_4371 = data_path_4371 + data_file_4371
df_4371 = df_norm(file_path_4371)

data_path_5717 = r"./data/jahreswerte_KL_05717_19070101_20201231_hist/"
data_file_5717 = r"produkt_klima_jahr_19070101_20201231_05717.txt"
file_path_5717 = data_path_5717 + data_file_5717
df_5717 = df_norm(file_path_5717)

df_1078 = df_1078[['ja_tt']].rename(columns={'ja_tt': '1078'})
df_1300 = df_1300[['ja_tt']].rename(columns={'ja_tt': '1300'})
df_1303 = df_1303[['ja_tt']].rename(columns={'ja_tt': '1303'})
df_1327 = df_1327[['ja_tt']].rename(columns={'ja_tt': '1327'})
df_1590 = df_1590[['ja_tt']].rename(columns={'ja_tt': '1590'})
df_2110 = df_2110[['ja_tt']].rename(columns={'ja_tt': '2110'})
df_2483 = df_2483[['ja_tt']].rename(columns={'ja_tt': '2483'})
df_2497 = df_2497[['ja_tt']].rename(columns={'ja_tt': '2497'})
df_2629 = df_2629[['ja_tt']].rename(columns={'ja_tt': '2629'})
df_2698 = df_2698[['ja_tt']].rename(columns={'ja_tt': '2698'})
df_4371 = df_4371[['ja_tt']].rename(columns={'ja_tt': '4371'})
df_5717 = df_5717[['ja_tt']].rename(columns={'ja_tt': '5717'})

df_tt = pd.concat([df_1078, df_1300,
                   df_1303, df_1327,
                   df_1590, df_2110,
                   df_2483, df_2497,
                   df_2629, df_2698,
                   df_4371, df_5717], 
                   axis=1
                   )

date_from = pd.to_datetime("1970-01-01 00:00:00+00:00")
date_to = pd.to_datetime("2020-01-01 00:00:00+00:00")

df_tt = df_tt[df_tt.index >= date_from]
df_tt = df_tt[df_tt.index <= date_to]

# print(df_1078.head())

df_tt_comp = df_tt[['1303', '2483']]

'''df_tt_comp.plot.scatter(figsize=(12,10),
                        grid=True,
                        title="Temperature Comparison Between Stations 1303 and 1483",
                        x='1303',
                        y='2483',
                        xlabel='Station 1303',
                        ylabel='Station 2483',
                       )
plt.show()
'''

# print(df_tt_comp.diff(periods=-1, axis=1))

# df_tt_comp.plot.scatter(x='1303', y='2483')
# plt.show()



'''
x=df_tt_comp['1303'],
y=df_tt_comp['2483'],
'''

avg_1078 = df_tt['1078'].cumsum().iloc[-1] / len(df_tt)
avg_1300 = df_tt['1300'].cumsum().iloc[-1] / len(df_tt)
avg_1303 = df_tt['1303'].cumsum().iloc[-1] / len(df_tt)
avg_1327 = df_tt['1327'].cumsum().iloc[-1] / len(df_tt)
avg_1590 = df_tt['1590'].cumsum().iloc[-1] / len(df_tt)
avg_2110 = df_tt['2110'].cumsum().iloc[-1] / len(df_tt)
avg_2483 = df_tt['2483'].cumsum().iloc[-1] / len(df_tt)
avg_2497 = df_tt['2497'].cumsum().iloc[-1] / len(df_tt)
avg_2629 = df_tt['2629'].cumsum().iloc[-1] / len(df_tt)
avg_2698 = df_tt['2698'].cumsum().iloc[-1] / len(df_tt)
avg_4371 = df_tt['4371'].cumsum().iloc[-1] / len(df_tt)
avg_5717 = df_tt['5717'].cumsum().iloc[-1] / len(df_tt)


avg_tt = [avg_1078, avg_1300,
          avg_1303, avg_1327,
          avg_1590, avg_2110,
          avg_2483, avg_2497,
          avg_2629, avg_2698,
          avg_4371, avg_5717
         ]

df_diff = df_tt.sub(avg_tt)

df_diff.plot(figsize=(12,8),
                grid=True
            )
# plt.show()


df_diff_trans = df_diff.transpose()
plt.figure(figsize=(18, 10))
heatmap = sns.heatmap(df_diff_trans,
            xticklabels=pd.Series(range(1970, 2021)),
            cmap="icefire",
            cbar_kws={'label': 'Temperature Difference'}
           )

plt.title("Temperature Change of NRW over 50 Years")
plt.xlabel("Years")
plt.ylabel("Station IDs")

plt.show()
