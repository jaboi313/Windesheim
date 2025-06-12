import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = {
    'Stap': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],
    'Start': ['2025-07-01', '2025-07-02', '2025-07-04', '2025-07-06', '2025-07-06', '2025-08-03', '2025-08-11', '2025-08-14', '2025-08-17', '2025-08-20', '2025-08-22', '2025-08-30', '2025-09-02'],
    'Finish': ['2025-07-02', '2025-07-04', '2025-07-06', '2025-08-03', '2025-07-07', '2025-08-11', '2025-08-14', '2025-08-17', '2025-08-20', '2025-08-22', '2025-08-30', '2025-09-02', '2025-09-03'],
    'Color': ['#292f56', '#21416d', '#005483', '#006794', '#006794', '#007a9a', '#008da1', '#00a1a4', '#00b5a3', '#00ca9a', '#36dc8d', '#76ec7e', '#acfa70'],
    'LineHeigth': [0, 0.1151, 0.1875, 0.329, 0, 0.4, 0.47, 0.5415, 0.612, 0.683, 0.7545, 0.825, 0.8965]

}

df = pd.DataFrame(data)
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])
df['Duration'] = (df['Finish'] - df['Start']).dt.days

fig, ax = plt.subplots(figsize=(10, 5))

fig.patch.set_facecolor("#e4e4e4")     # Whole figure
ax.set_facecolor('#e4e4e4')

bar_height = 0.4

ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Stap'])

for i, row in df.iterrows():
    ax.barh(y=row['Stap'], width=row['Duration'], left=row['Start'], color=row['Color'])
    ax.axvline(x=row['Start'], ymin=0, ymax=row['LineHeigth'], color='black')

ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
plt.xlabel('Date')
plt.title('Project roadmap')
plt.grid(False)
plt.ylabel("Stap")
plt.xlabel("Datum")
plt.xticks(rotation=45)\
    
plt.show()