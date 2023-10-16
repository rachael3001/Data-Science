import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("airline_delay.csv")

print(df.head())

delays = ["nas_ct","security_ct","late_aircraft_ct", "weather_ct","carrier_ct"]

sns.distplot(df[delays], bins=30, kde=False,color='red')
plt.xlim([0, 200]) 
plt.show()