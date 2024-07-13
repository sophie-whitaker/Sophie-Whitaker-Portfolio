#This code creates a subplot of Raman spectra of different samples obtained from experiment.
#It demonstrates my use of pandas, and ability to handle and effectly visualise large datasets

import pandas as pd
import matplotlib.pyplot as plt

fpath_019 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW019.5.xy'
fpath_005 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW.22.11.15-005.2.xy'
fpath_013 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW013.xy'
fpath_021 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW021.1.xy'
fpath_012 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW.28.11.22.012.dpt'
fpath_007 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW.22.11.17-007.xy'
fpath_030 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW030.1.xy'
fpath_017 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW017.1.xy'
fpath_016 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW 221206 016.dpt'
fpath_015 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW.5.12.22.015.xy'
fpath_018 = r'C:\Users\chem-sjoh4999\Documents\Presenting Results\Stacked Raman 2\SW018.1.xy'

save_fpath = 'C:\\Users\\chem-sjoh4999\\Documents\\Part II Results\\Presenting Results\\Stacked Raman\\Stacked Raman plot.png'

x_019 = pd.read_table(fpath_019, header = 0, usecols=[0]).values
y_019 = pd.read_table(fpath_019, header = 0, usecols=[1]).values
x_005 = pd.read_table(fpath_005, header = 0, usecols=[0]).values
y_005 = pd.read_table(fpath_005, header = 0, usecols=[1]).values
x_013 = pd.read_table(fpath_013, header = 0, usecols=[0]).values
y_013 = pd.read_table(fpath_013, header = 0, usecols=[1]).values
x_021 = pd.read_table(fpath_021, header = 0, usecols=[0]).values
y_021 = pd.read_table(fpath_021, header = 0, usecols=[1]).values
x_012 = pd.read_table(fpath_012, header = 0, usecols=[0]).values
y_012 = pd.read_table(fpath_012, header = 0, usecols=[1]).values
x_007 = pd.read_table(fpath_007, header = 0, usecols=[0]).values
y_007 = pd.read_table(fpath_007, header = 0, usecols=[1]).values
x_030 = pd.read_table(fpath_030, header = 0, usecols=[0]).values
y_030 = pd.read_table(fpath_030, header = 0, usecols=[1]).values
x_017 = pd.read_table(fpath_017, header = 0, usecols=[0]).values
y_017 = pd.read_table(fpath_017, header = 0, usecols=[1]).values
x_016 = pd.read_table(fpath_016, header = 0, usecols=[1]).values
y_016 = pd.read_table(fpath_016, header = 0, usecols=[1]).values
x_015 = pd.read_table(fpath_015, header = 0, usecols=[0]).values
y_015 = pd.read_table(fpath_015, header = 0, usecols=[1]).values
x_018 = pd.read_table(fpath_018, header = 0, usecols=[1]).values
y_018 = pd.read_table(fpath_018, header = 0, usecols=[1]).values

plt.rcParams['font.family']='serif'
fig, axes = plt.subplots(12, 1, sharex=True)
plt.xlim(3325, 3175)

axes[0].plot(x_019, y_019, label='019', color='black', linewidth=0.9)
axes[0].set_ylim(9000, 14000)

axes[1].plot(x_005, y_005, label='005', color='red', linewidth=0.9)
axes[1].set_ylim(74000, 78000)

axes[2].plot(x_013, y_013, label='013', color='black', linewidth=0.9)
axes[2].set_ylim(145000, 147000)

axes[3].plot(x_021, y_021, label='021', color='red', linewidth=0.9)
axes[3].set_ylim(610000, 635000)

axes[4].plot(x_012, y_012, label='012', color='black', linewidth=0.9)
axes[4].set_ylim(500000, 570000)

axes[5].plot(x_007, y_007, label='007', color='red', linewidth=0.9)
axes[5].set_ylim(80000, 120000)

axes[6].plot(x_030, y_030, label='030', color='black', linewidth=0.9)
axes[6].set_ylim(56000, 64000)

axes[7].plot(x_017, y_017, label='017', color='red', linewidth=0.9)
axes[7].set_ylim(13000, 17000)

axes[8].plot(x_016, y_016, label='016', color='black', linewidth=0.9)
axes[8].set_ylim(65000, 80000)

axes[9].plot(x_015, y_015, label='015', color='red', linewidth=0.9)
axes[9].set_ylim(175000, 200000)

axes[11].plot(x_018, y_018, label='018', color='red', linewidth=0.9)
axes[11].set_ylim(6000, 11000)

axes[0].title.set_text('Stacked Raman')
fig.subplots_adjust(hspace=0)

plt.xlabel('Wavenumber, cm$^{-1}$', color = 'black', fontsize='14', horizontalalignment='center')
axes[3].set_ylabel('Intensity', fontsize='14')

for i in range(1, 12):
    axes[i-1].tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    axes[i-1].spines["bottom"].set_visible(False)
    axes[i].spines["top"].set_visible(False)
    
for i in range(12):
    axes[i].tick_params(axis='y', which='both', left=False, top=False, labelleft=False)

axes[0].annotate('100:0', xy=(3200, 14000), xytext=(3170, 10000), color='black', fontsize=9)
axes[1].annotate('83.3:16.7', xy=(3200, 74000), xytext=(3170, 75000), color='red', fontsize=9)
axes[2].annotate('75:25', xy=(3200, 78000), xytext=(3170, 76000), color='black', fontsize=9)
axes[3].annotate('66.7:33.3', xy=(3200, 635000), xytext=(3170, 560000), color='red', fontsize=9)
axes[4].annotate('58.3:41.7', xy=(3200, 570000), xytext=(3170, 570000), color='black', fontsize=9)
axes[5].annotate('50:50', xy=(3200, 120000), xytext=(3170, 120000), color='red', fontsize=9)
axes[6].annotate('41.7:58.3', xy=(3200, 64000), xytext=(3170, 64000), color='black', fontsize=9)
axes[7].annotate('33.3:66.7', xy=(3200, 17000), xytext=(3170, 17000), color='red', fontsize=9)
axes[8].annotate('25:75', xy=(3200, 80000), xytext=(3170, 80000), color='black', fontsize=9)
axes[9].annotate('16.7:83.3', xy=(3200, 20000), xytext=(3170,2000), color='black', fontsize=9)
axes[11].annotate('0:100', xy=(3200, 11000), xytext=(3170, 11000), color='black', fontsize=9)

fig.set_figheight(20)
fig.set_figwidth(10)

