import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

df = pd.read_csv("airline_delay.csv")
sns.set_style("darkgrid")

y = df["arr_flights"]
x = df["arr_del15"]
delays  = ["nas_ct","security_ct","late_aircraft_ct", "weather_ct","carrier_ct"]
#fig, ax= plt.subplots(nrows=1, ncols=2, figsize=(10,4))

#Graph on comparison between 2019 and 2020 delays
#Creation of data 
df["flightdelays_arrivals"] = x/y

#plotting graph
plot = sns.histplot(data=df, x="flightdelays_arrivals", hue="year", kde=True, palette="muted")
plt.ylabel("Frequency")
plt.xlabel("Percent of flights delayed at an airport")
plt.title("Percent of total flights delayed: 2019 and 2020")

#Converting x-axis to percents for readability

plot.xaxis.set_major_formatter(mtick.PercentFormatter())
vals = plot.get_xticks()
plot.set_xticklabels(['{:,.0%}'.format(x) for x in vals])
plt.show()

#Graph total flights of 2019 and 2020
df_grpd = df.groupby(["year"])["arr_flights"].sum().reset_index()

#Added total at top of barplot
ax = sns.barplot(data=df_grpd, ci=None, x="year", y="arr_flights",estimator=sum,errorbar=None)
ax.bar_label(ax.containers[0])

plt.xlabel("Year")
plt.ylabel("Total flights")
plt.title("Total Flights per year")
plt.show()