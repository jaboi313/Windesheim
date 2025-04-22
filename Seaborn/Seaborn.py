import seaborn as sea, matplotlib.pyplot as mpl

product = ["Brood", "Pindakaas", "Kaas"]
verkocht = [6, 12, 3]

sea.barplot(x=product, y=verkocht, palette=['orange'])

mpl.title("Verkoop producten")
mpl.xlabel("Producten", loc='left')
mpl.ylabel("Aantal Verkocht")
mpl.show()