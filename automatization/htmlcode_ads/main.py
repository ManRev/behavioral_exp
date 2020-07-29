import CRN_fill
import pandas as pd

CRN = "taboola"

path = "CRN_code"
out_path = "CRNs"
df = pd.read_csv("titres2.csv", error_bad_lines=False, header=0)
print((df["ID"]))
df = df.fillna(0)


CRN_type = "ob_sfeed_logo"

df_HQ = df.loc[(df["Cat"]==1) & (df["Cat1_HQ"]==1)]
df_LQ = df.loc[(df["Cat"]==1) & (df["Cat1_HQ"]==0)]
df_HQ_pol = df.loc[(df["CatPol"]==1) & (df["Cat2_HQ_Pol"]==1)]
df_LQ_pol = df.loc[(df["CatPol"]==1) & (df["Cat2_HQ_Pol"]==0)]

print((df_HQ))
print(len(df_LQ))
print((df_HQ_pol))
print(len(df_LQ_pol))

df_HQ = df_HQ.sample(4)
url = df_HQ["Image_Url"]
title = df_HQ["Text"].values.tolist()
source = df_HQ["Source"].values.tolist()
tt = []

for line in url:
       line = line.replace("background-image: url(", '')
       line = line.replace(");", '')
       line = line.replace('"', '')
       line = line.replace("''", '')
       line = line.replace("' height: 172px;'", '')
       tt.append(line)
url = tt

CRN_fill.fill_CRN_html(path, "CARFEFUL_crn_hq", url, title, source, CRN_type)

df_LQ = df_LQ.sample(4)
url = df_LQ["Image_Url"]
title = df_LQ["Text"].values.tolist()
source = df_LQ["Source"].values.tolist()
tt = []

for line in url:
       line = line.replace("background-image: url(", '')
       line = line.replace(");", '')
       line = line.replace('"', '')
       line = line.replace("''", '')
       line = line.replace("' height: 172px;'", '')
       tt.append(line)
url = tt
print(title)
print(source)
CRN_fill.fill_CRN_html(path, "CARFEFUL_crn_lq", url, title, source, CRN_type)


df_HQ_pol = df_HQ_pol.sample(4)
url = df_HQ_pol["Image_Url"]
title = df_HQ_pol["Text"].values.tolist()
source = df_HQ_pol["Source"].values.tolist()
tt = []

for line in url:
       line = line.replace("background-image: url(", '')
       line = line.replace(");", '')
       line = line.replace('"', '')
       line = line.replace("''", '')
       tt.append(line)
url = tt

CRN_fill.fill_CRN_html(path, "CARFEFUL_crn_hq_pol", url, title, source, CRN_type)

df_LQ_pol = df_LQ_pol.sample(4)
url = df_LQ_pol["Image_Url"]
title = df_LQ_pol["Text"].values.tolist()
source = df_LQ_pol["Source"].values.tolist()
tt = []

for line in url:
       line = line.replace("background-image: url(", '')
       line = line.replace(");", '')
       line = line.replace('"', '')
       line = line.replace("''", '')
       line = line.replace("' height: 172px;'", '')
       tt.append(line)
url = tt

CRN_fill.fill_CRN_html(path, "CARFEFUL_crn_Lq_pol", url, title, source, CRN_type)
