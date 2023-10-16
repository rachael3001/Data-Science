import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

df = pd.read_csv("airline_delay.csv")

#print(df.head())

y = df["arr_flights"]
x = df["arr_del15"]
delays  = ["nas_ct","security_ct","late_aircraft_ct", "weather_ct","carrier_ct"]

df["flightdelays_arrivals"] = x/y
plot = sns.histplot(df["flightdelays_arrivals"])
#sns.boxenplot(x=x, y=y,width_method="linear")
# plt.ylim(0,7500)
plt.ylabel("Frequency")
plt.xlabel("Percent of flights delayed at an airport")
plt.title("Distribution of percentage of flights delayed out of total Flights arriving")
plot.xaxis.set_major_formatter(mtick.PercentFormatter())
vals = plot.get_xticks()
plot.set_xticklabels(['{:,.0%}'.format(x) for x in vals])
plt.show()