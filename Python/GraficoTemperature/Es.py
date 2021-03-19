import matplotlib.pyplot as plt
import csv

mesi_n = []
temperature = []
giacca = []
scuola = []
videogame = []

data_file = open("C:/Users/nicol/Dropbox/Scuola/Sistemi/Python/GraficoTemperature/file.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)

for row in data_reader:
    mesi_n.append(int(row[1]))
    temperature.append(float(row[2]))
    giacca.append(float(row[3]))
    scuola.append(float(row[4]))
    videogame.append(float(row[5]))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Grafici')

ax1.plot(mesi_n, temperature, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temperature (C°)')

ax2.plot(mesi_n, giacca, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Giacca (GIORNI)')

ax3.plot(mesi_n, scuola, 'o-b')
ax3.set_xlabel('Mese')
ax3.set_ylabel('Scuola (GIORNI)')

ax4.plot(mesi_n, videogame, 'o-r')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Videogiochi (GIORNI)')

plt.show()