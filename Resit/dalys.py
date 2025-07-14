import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r"C:\Users\cqy111\Desktop\IBI1\QY13-gif.github.io\Resit")
print(os.getcwd())
print(os.listdir())
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#Operate it with some measures
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())
print(dalys_data.iloc[0,3])
print(dalys_data.iloc[2,0:5])
print(dalys_data.iloc[0:2,:])
print(dalys_data.iloc[0:10:2,0:5])
print(dalys_data.iloc[0:10,2:4])
print(dalys_data.iloc[2,3])
print(dalys_data.iloc[0:3,[0,1,3]])
my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3,my_columns])
print(dalys_data.loc[2:4,"Year"])
#Select dalys data in 1990
year_1990 = dalys_data["Year"] == 1990
print(dalys_data.loc[year_1990, "DALYs"])
#Select data of China
china = dalys_data.loc[dalys_data.Entity=="China", ["DALYs", "Year"]]
#Make a plot shoiwing china's data
plt.plot(china.Year, china.DALYs, 'b+')
plt.xticks(china.Year,rotation=-90)
plt.show()
#Select the max and min daly data
max_daly = china["DALYs"].max()
min_daly = china["DALYs"].min()
max_year = china.loc[china["DALYs"] == max_daly, "Year"].values[0]
min_year = china.loc[china["DALYs"] == min_daly, "Year"].values[0]
print(f"China max DALYs: {max_daly} in {max_year}")
print(f"China min DALYs: {min_daly} in {min_year}")
#Make another plot of china's data
plt.plot(china["Year"], china["DALYs"], 'b-', label="China")
plt.title("DALYs Over Time in China")
plt.xlabel("Year")
plt.ylabel("DALYs Rate")
plt.xticks(china.Year,rotation=-90)
plt.legend()
plt.show()

#Other one question
'''How has the relationship between the DALYs in France and the UK (two similarly
sized countries) changed over time? Are they becoming more similar, less similar?'''
france = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs", "Year"]]
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]
plt.plot(france["Year"], france["DALYs"], 'b-', label="France(blue)")
plt.plot(uk["Year"], uk["DALYs"], 'r-', label="UK(red)")
plt.title("DALYs Comparison: France vs UK")
plt.xlabel("Year")
plt.ylabel("DALYs Rate")
plt.xticks(rotation=-90)
plt.legend()
plt.show()
#From the figure: Both of them are generally showing a downward trend, but in the future, they may become increasingly different from each other.
