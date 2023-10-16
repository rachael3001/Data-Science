import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

df = pd.read_csv("airline_delay.csv")


y = df["arr_flights"]
x = df["arr_del15"]
delays  = ["nas_ct","security_ct","late_aircraft_ct", "weather_ct","carrier_ct"]

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