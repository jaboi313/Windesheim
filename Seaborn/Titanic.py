import seaborn as sea, matplotlib.pyplot as mpl, pandas as pd
data = sea.load_dataset("titanic")

not_survivers = data[data['survived'] == 0].groupby('pclass')['survived'].count().reset_index()
not_survivers.columns = ['pclass', 'count']

sea.barplot(x='pclass', y='count', data=not_survivers, palette=['red', 'blue', 'green'])
mpl.title("Aantal Titanic doden per klasse")
mpl.xlabel("Klasse", loc='left')
mpl.ylabel("Doden", loc='bottom')
mpl.show()