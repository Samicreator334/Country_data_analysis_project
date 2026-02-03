"""
Country Data Project – All-in-one analysis script

What it does:
1) Loads Country_data_project.xlsx
2) Cleans/standardizes column names
3) Top 10 countries by recycling rate
4) Average recycling rate by region
5) Waste_per_1000_people (msw_per_capita_kg_year * population / 1000)
6) Recycling level bins (Low/Medium/High)
7) "Problem countries" filter: msw_per_capita_kg_year > 500 and recycling_rate_percent < 20
8) Bar chart: average recycling rate by region (if matplotlib installed)
9) Exports cleaned data to Country_data_cleaned.xlsx

Run:
    python country_data_analysis.py
"""


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("Country_data_project.xlsx", sheet_name="country_level_data")

#clean column names if there are hidden spaces
df.columns = df.columns.str.strip()

#Top 10 countries by recycling rate
country_col = "country_name"
recycle_col = "waste_treatment_recycling_percent"

df[recycle_col] = pd.to_numeric(df[recycle_col], errors="coerce")

top10_recycling = (
    df[[country_col, recycle_col]]
      .dropna(subset=[recycle_col])
      .sort_values(by=recycle_col, ascending=False)
      .head(10)
)

print(top10_recycling.to_string(index=False))


#Average recycling rate by region
recycle_col = "waste_treatment_recycling_percent"

df[recycle_col] = pd.to_numeric(df[recycle_col], errors="coerce")

top10_recycling = (
    df[["iso3c", "country_name", recycle_col]]
      .dropna(subset=[recycle_col])
      .sort_values(by=recycle_col, ascending=False)
      .head(10)
)

print(top10_recycling.to_string(index=False))


#Waste_per_1000_people (msw_per_capita_kg_year * population / 1000)
msw_col = "MSW_per_capita (kg/year)"
pop_col = "population_population_number_of_people"
country_col = "country_name"

# make sure numeric
df[msw_col] = pd.to_numeric(df[msw_col], errors="coerce")
df[pop_col] = pd.to_numeric(df[pop_col], errors="coerce")

df["Waste_per_1000_people"] = (df[msw_col] * df[pop_col]) / 1000

print(df[[country_col, "Waste_per_1000_people"]].head().to_string(index=False))
df = df.rename(columns=rename_map)



#Recycling level bins (Low/Medium/High)
recycle_col = "waste_treatment_recycling_percent"
df[recycle_col] = pd.to_numeric(df[recycle_col], errors="coerce")

df["Recycling_Level"] = pd.cut(
    df[recycle_col],
    bins=[0, 20, 40, 100],
    labels=["Low", "Medium", "High"],
    include_lowest=True
)

print(df["Recycling_Level"].value_counts(dropna=False))



#Problem countries" filter: msw_per_capita_kg_year > 500 and recycling_rate_percent < 20
msw_col = "MSW_per_capita (kg/year)"
recycle_col = "waste_treatment_recycling_percent"
country_col = "country_name"

# Ensure numeric
df[msw_col] = pd.to_numeric(df[msw_col], errors="coerce")
df[recycle_col] = pd.to_numeric(df[recycle_col], errors="coerce")

problem_countries = df[
    (df[msw_col] > 500) &
    (df[recycle_col] < 20)
]

print(problem_countries[[country_col, msw_col, recycle_col]].to_string(index=False))



#Bar chart: average recycling rate by region (if matplotlib installed)
region_col = "region_id"
recycle_col = "waste_treatment_recycling_percent"

# Make sure recycling % is numeric
df[recycle_col] = pd.to_numeric(df[recycle_col], errors="coerce")

# --- Bar chart: Average Recycling % by Region ---
(df.groupby(region_col)[recycle_col]
   .mean()
   .sort_values(ascending=False)
   .plot(kind="bar")
)

plt.title("Average Recycling Rate by Region")
plt.ylabel("Recycling Rate (%)")
plt.xlabel("Region ID")
plt.tight_layout()
plt.show()





#Exports cleaned data to Country_data_cleaned.xlsx
# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace("%", "percent", regex=False)
)

# make sure recycling column is numeric
df["waste_treatment_recycling_percent"] = pd.to_numeric(
    df["waste_treatment_recycling_percent"], errors="coerce"
)

top10_recycling = (
    df.dropna(subset=["waste_treatment_recycling_percent"])
      .sort_values(by="waste_treatment_recycling_percent", ascending=False)
      .head(10)
)

print(top10_recycling[["country_name", "waste_treatment_recycling_percent"]].to_string(index=False))



