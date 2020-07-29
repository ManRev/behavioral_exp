import pandas as pd
import numpy as np
from statistics import mean
import csv

# cond is a dummy variable to specify which treatment / control group one wants:
# cond == "all_3" for all 3 conditions
# cond == "with_wo" for control (no CRN) treatment (CRN, mixed or pol)
# cond == "mixed_pol" for control (mixed CRN) treatment (pol CRN)
cond = "all_3"

path = "results.csv"
data = pd.read_csv(path)
print(list(data.columns.values))


effects = ["trustworthy", "false", "credible", "biased", "provide news information"]

mapping = {"Strongly agree": 5, "Somewhat agree":4, "Neither agree nor disagree":3,
           "Somewhat disagree":2, "Strongly disagree":1}
data = data.applymap(lambda s: mapping.get(s) if s in mapping else s)

a = ["Q619", "Q625", "Q627", "Q630", "Q632"]
b = ["Q812", "Q818", "Q824", "Q830", "Q836"]
c = ["Q814", "Q820", "Q826", "Q832", "Q838"]
d = ["Q816", "Q822", "Q828", "Q834", "Q840"]

p1c1_set = ["p1c1_1", "p1c1_2", "p1c1_3", "p1c1_4", "p1c1_5"]
p1c2_set = ["p1c2_1", "p1c2_2", "p1c2_3", "p1c2_4", "p1c2_5"]
p1c3_set = ["p1c3_1", "p1c3_2", "p1c3_3", "p1c3_4", "p1c3_5"]
p2c1_set = ["p2c1_1", "p2c1_2", "p2c1_3", "p2c1_4", "p2c1_5"]
p2c2_set = ["p2c2_1", "p2c2_2", "p2c2_3", "p2c2_4", "p2c2_5"]
p2c3_set = ["p2c3_1", "p2c3_2", "p2c3_3", "p2c3_4", "p2c3_5"]
p3c1_set = ["p3c1_1", "p3c1_2", "p3c1_3", "p3c1_4", "p3c1_5"]
p3c2_set = ["p3c2_1", "p3c2_2", "p3c2_3", "p3c2_4", "p3c2_5"]
p3c3_set = ["p3c3_1", "p3c3_2", "p3c3_3", "p3c3_4", "p3c3_5"]
p4c1_set = ["p4c1_1", "p4c1_2", "p4c1_3", "p4c1_4", "p4c1_5"]
p4c2_set = ["p4c2_1", "p4c2_2", "p4c2_3", "p4c2_4", "p4c2_5"]
p4c3_set = ["p4c3_1", "p4c3_2", "p4c3_3", "p4c3_4", "p4c3_5"]

data = data.reindex(columns=[*data.columns.tolist(), *p1c1_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p1c2_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p1c3_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p2c1_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p2c2_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p2c3_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p3c1_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p3c2_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p3c3_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p4c1_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p4c2_set], fill_value=np.nan)
data = data.reindex(columns=[*data.columns.tolist(), *p4c3_set], fill_value=np.nan)

p1c1_count = 0
p1c2_count = 0
p1c3_count = 0
p2c1_count = 0
p2c2_count = 0
p2c3_count = 0
p3c1_count = 0
p3c2_count = 0
p3c3_count = 0
p4c1_count = 0
p4c2_count = 0
p4c3_count = 0

data = data.iloc[3:]
for index, rows in data.iterrows():
    if rows["FL_13_DO"] == "FL_17":
        p1c1_count += 1
        p2c1_count += 1
        p3c2_count += 1
        p4c3_count += 1
        for k in range(len(d)):
            data.at[index, p1c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p2c1_set[k]] = rows[b[k]]
        for k in range(len(d)):
            data.at[index, p3c2_set[k]] = rows[c[k]]
        for k in range(len(d)):
            data.at[index, p4c3_set[k]] = rows[d[k]]
    if rows["FL_13_DO"] == "FL_18":
        p1c1_count += 1
        p2c1_count += 1
        p3c3_count += 1
        p4c2_count += 1
        for k in range(len(d)):
            data.at[index, p1c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p2c1_set[k]] = rows[b[k]]
        for k in range(len(d)):
            data.at[index, p3c3_set[k]] = rows[d[k]]
        for k in range(len(d)):
            data.at[index, p4c2_set[k]] = rows[c[k]]
    if rows["FL_13_DO"] == "FL_19":
        p1c1_count += 1
        p2c3_count += 1
        p3c1_count += 1
        p4c2_count += 1
        for k in range(len(d)):
            data.at[index, p1c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p2c3_set[k]] = rows[d[k]]
        for k in range(len(d)):
            data.at[index, p3c1_set[k]] = rows[b[k]]
        for k in range(len(d)):
            data.at[index, p4c2_set[k]] = rows[c[k]]
    if rows["FL_13_DO"] == "FL_366":
        p1c1_count += 1
        p2c2_count += 1
        p3c1_count += 1
        p4c3_count += 1
        for k in range(len(d)):
            data.at[index, p1c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p2c2_set[k]] = rows[c[k]]
        for k in range(len(d)):
            data.at[index, p3c1_set[k]] = rows[b[k]]
        for k in range(len(d)):
            data.at[index, p4c3_set[k]] = rows[d[k]]
    if rows["FL_13_DO"] == "FL_20":
        p1c1_count += 1
        p2c2_count += 1
        p3c3_count += 1
        p4c1_count += 1
        for k in range(len(d)):
            data.at[index, p1c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p2c2_set[k]] = rows[c[k]]
        for k in range(len(d)):
            data.at[index, p3c3_set[k]] = rows[d[k]]
        for k in range(len(d)):
            data.at[index, p4c1_set[k]] = rows[b[k]]
    if rows["FL_13_DO"] == "FL_21":
        p1c1_count += 1
        p2c3_count += 1
        p3c2_count += 1
        p4c1_count += 1
        for k in range(len(d)):
            data.at[index, p1c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p2c3_set[k]] = rows[d[k]]
        for k in range(len(d)):
            data.at[index, p3c2_set[k]] = rows[c[k]]
        for k in range(len(d)):
            data.at[index, p4c1_set[k]] = rows[b[k]]
    if rows["FL_13_DO"] == "FL_22":
        p1c2_count += 1
        p2c1_count += 1
        p3c1_count += 1
        p4c3_count += 1
        for k in range(len(d)):
            data.at[index, p1c2_set[k]] = rows[c[k]]
        for k in range(len(d)):
            data.at[index, p2c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p3c1_set[k]] = rows[b[k]]
        for k in range(len(d)):
            data.at[index, p4c3_set[k]] = rows[d[k]]
    if rows["FL_13_DO"] == "FL_23":
        p1c3_count += 1
        p2c1_count += 1
        p3c1_count += 1
        p4c2_count += 1
        for k in range(len(d)):
            data.at[index, p1c3_set[k]] = rows[d[k]]
        for k in range(len(d)):
            data.at[index, p2c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p3c1_set[k]] = rows[b[k]]
        for k in range(len(d)):
            data.at[index, p4c2_set[k]] = rows[c[k]]
    if rows["FL_13_DO"] == "FL_24":
        p1c2_count += 1
        p2c1_count += 1
        p3c3_count += 1
        p4c1_count += 1
        for k in range(len(d)):
            data.at[index, p1c2_set[k]] = rows[c[k]]
        for k in range(len(d)):
            data.at[index, p2c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p3c3_set[k]] = rows[d[k]]
        for k in range(len(d)):
            data.at[index, p4c1_set[k]] = rows[b[k]]
    if rows["FL_13_DO"] == "FL_25":
        p1c3_count += 1
        p2c1_count += 1
        p3c2_count += 1
        p4c1_count += 1
        for k in range(len(d)):
            data.at[index, p1c3_set[k]] = rows[d[k]]
        for k in range(len(d)):
            data.at[index, p2c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p3c2_set[k]] = rows[c[k]]
        for k in range(len(d)):
            data.at[index, p4c1_set[k]] = rows[b[k]]
    if rows["FL_13_DO"] == "FL_26":
        p1c2_count += 1
        p2c3_count += 1
        p3c1_count += 1
        p4c1_count += 1
        for k in range(len(d)):
            data.at[index, p1c2_set[k]] = rows[c[k]]
        for k in range(len(d)):
            data.at[index, p2c3_set[k]] = rows[d[k]]
        for k in range(len(d)):
            data.at[index, p3c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p4c1_set[k]] = rows[b[k]]
    if rows["FL_13_DO"] == "FL_27":
        p1c3_count += 1
        p2c2_count += 1
        p3c1_count += 1
        p4c1_count += 1
        for k in range(len(d)):
            data.at[index, p1c3_set[k]] = rows[d[k]]
        for k in range(len(d)):
            data.at[index, p2c2_set[k]] = rows[c[k]]
        for k in range(len(d)):
            data.at[index, p3c1_set[k]] = rows[a[k]]
        for k in range(len(d)):
            data.at[index, p4c1_set[k]] = rows[b[k]]

data = data.loc[(data["Q1"]=="I agree to participate") & (data["Finished"]!=False)]
data = data.loc[(data["Q797"]=="The Drudge Report,ABC News website") & (data["Q773"]=="Red,Green")]

print(len(data))
c0 = [p1c1_set, p2c1_set, p3c1_set, p4c1_set]
c1 = [p1c2_set, p2c2_set, p3c2_set, p4c2_set]
c2 = [p1c3_set, p2c3_set, p3c3_set, p4c3_set]


cc0 = []
for col in c0:
    data_col = data[col].iloc[3:]
    sum0 = data_col.mean()
    print(data_col)
    cc0.append(sum0)

cc1 = []
for col in c1:
    data_col = data[col].iloc[3:]
    sum1 = data_col.mean()
    cc1.append(sum1)

cc2 = []
for col in c2:
    data_col = data[col].iloc[3:]
    sum2 = data_col.mean()
    cc2.append(sum2)

cb_1 = []
for col in c1+c2:
    data_col = data[col].iloc[3:]
    sum2 = data_col.mean()
    cb_1.append(sum2)

if cond == "all_3":
    cb0 = cc0
    cb1 = cc1
if cond == "with_wo":
    cb0 = cc0
    cb1 = cb_1
if cond == "mixed_pol":
    cb0 = cc1
    cb1 = cc2


ccc0 = [list(cc0[0]), list(cc0[1]), list(cc0[2]), list(cc0[3])]
ccc1 = [list(cc1[0]), list(cc1[1]), list(cc1[2]), list(cc1[3])]
ccc2 = [list(cc2[0]), list(cc2[1]), list(cc2[2]), list(cc2[3])]

ccb0 = [list(cb0[0]), list(cb0[1]), list(cb0[2]), list(cb0[3])]
ccb1 = [list(cb1[0]), list(cb1[1]), list(cb1[2]), list(cb1[3])]

# ccc(i) is a 4-list list for condition i. The 5-float list j corresponds to publisher j. The float k corresponds to the effect[k]
print(ccb0)
print(ccb1)
print(ccc2)

# *map(mean, zip(*ccci)) is a 5-float list, where float k is the mean effect[k] averaged over all pjci.
print(*map(mean, zip(*ccb0)))
print(*map(mean, zip(*ccb1)))
print(*map(mean, zip(*ccc2)))




