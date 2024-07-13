#This code creates a subplot  of overlayed hydrogen gas release peaks as a function of time from multiple experiments. 
#It demonstrates my use of pandas and matplotlib packages, along with advanced data visualisation methods

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from MS_data_functions import *

#Importing the calibration files for the gas rig used in the experiments.  These are imported as the baseline readings must be accounted for when analysing the data collected in my experiments. 

I_factors = IonizationFactors(fname='C:/Users/chem-sjoh4999/Documents/Part II Results/Calibration/Koala/221014_Koala_LF_Ifactors.txt')
all_sfs = FragmentationRatios(fname='C:/Users/chem-sjoh4999/Documents/Part II Results/Calibration/Koala/221014_Koala_LF_frag_rats.txt')

#The following code imports the data from each experiment and extracts the x and y values to plot.  Each experiment is labeled with a unique 3 digit ID, such as 019. 

data_019 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/22-01-11 019/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_019.assign_csv_fpath('019.csv')
data_019.assign_log_fpath('SW019.log')
data_019.get_log_data(CRD=True)

data_019.extract_MS_data(20)                                            
data_019.all_sfs.self_calibrate('NH3', data_019, x_range=[400, 600])  #Each set of experimental data was also self-calibrated to improve accuracy
data_019.fit_MS_data(t_range=[50, 400])                                 

time_range = data_019.MS_fit_times

x_019=time_range.tolist()
y_019=data_019.MS_gasfracs.T[3].tolist()

data_029 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/029/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_029.assign_csv_fpath('029.csv')
data_029.assign_log_fpath('SW029.log')
data_029.get_log_data(CRD=True)

data_029.extract_MS_data(20)                                            
data_029.all_sfs.self_calibrate('NH3', data_029, x_range=[400, 600])    
data_029.fit_MS_data(t_range=[50, 400])                                 

time_range = data_029.MS_fit_times

x_029=time_range.tolist()
y_029=data_029.MS_gasfracs.T[3].tolist()


data_033 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/033/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_033.assign_csv_fpath('033.csv')
data_033.assign_log_fpath('SW033.log')
data_033.get_log_data(CRD=True)

data_033.extract_MS_data(20)                                            
data_033.all_sfs.self_calibrate('NH3', data_033, x_range=[400, 600])    
data_033.fit_MS_data(t_range=[50, 400])                                 

time_range = data_033.MS_fit_times

x_033=time_range.tolist()
y_033=data_033.MS_gasfracs.T[3].tolist()

data_021 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/23-01-19 021/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_021.assign_csv_fpath('23-01-16-021.csv')
data_021.assign_log_fpath('SW021.log')
data_021.get_log_data(CRD=True)

data_021.extract_MS_data(20)                                            
data_021.all_sfs.self_calibrate('NH3', data_021, x_range=[400, 600])    
data_021.fit_MS_data(t_range=[50, 400])                                 

time_range = data_021.MS_fit_times

x_021=time_range.tolist()
y_021=data_021.MS_gasfracs.T[3].tolist()

data_012 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/22-11-29 012/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_012.assign_csv_fpath('SW.22.11.30.012.csv')
data_012.assign_log_fpath('SW 012.log')
data_012.get_log_data(CRD=True)

data_012.extract_MS_data(20)                                            
data_012.all_sfs.self_calibrate('NH3', data_012, x_range=[400, 600])    
data_012.fit_MS_data(t_range=[50, 400])                                 

time_range = data_012.MS_fit_times

x_012 =time_range.tolist()
y_012 =data_012.MS_gasfracs.T[3].tolist()

data_007 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/16.11.22 007/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_007.assign_csv_fpath('22-11-16-007.csv')
data_007.assign_log_fpath('SW-22-11-16-007.log')
data_007.get_log_data(CRD=True)

data_007.extract_MS_data(20)                                            
data_007.all_sfs.self_calibrate('NH3', data_007, x_range=[400, 600])    
data_007.fit_MS_data(t_range=[50, 400])                                 

time_range = data_007.MS_fit_times

x_007 =time_range.tolist()
y_007 =data_007.MS_gasfracs.T[3].tolist()


data_030 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/030/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_030.assign_csv_fpath('030.csv')
data_030.assign_log_fpath('SW030.log')
data_030.get_log_data(CRD=True)

data_030.extract_MS_data(20)                                            
data_030.all_sfs.self_calibrate('NH3', data_030, x_range=[400, 600])    
data_030.fit_MS_data(t_range=[50, 400])                                 

time_range = data_030.MS_fit_times

x_030=time_range.tolist()
y_030=data_030.MS_gasfracs.T[3].tolist()

data_017 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/017/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_017.assign_csv_fpath('017.csv')
data_017.assign_log_fpath('SW017.log')
data_017.get_log_data(CRD=True)

data_017.extract_MS_data(20)                                     
data_017.all_sfs.self_calibrate('NH3', data_017, x_range=[400, 600]) 
data_017.fit_MS_data(t_range=[50, 400])                           

time_range = data_017.MS_fit_times

x_017=time_range.tolist()
y_017=data_017.MS_gasfracs.T[3].tolist()

data_016 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/016/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_016.assign_csv_fpath('22-11-15-016.csv')
data_016.assign_log_fpath('SW016.log')
data_016.get_log_data(CRD=True)

data_016.extract_MS_data(20)                                     
data_016.all_sfs.self_calibrate('NH3', data_016, x_range=[400, 600]) 
data_016.fit_MS_data(t_range=[50, 400])                           

time_range = data_016.MS_fit_times

x_016=time_range.tolist()
y_016=data_016.MS_gasfracs.T[3].tolist()

data_015 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/015/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_015.assign_csv_fpath('015.csv')
data_015.assign_log_fpath('SW 015.log')
data_015.get_log_data(CRD=True)

data_015.extract_MS_data(20)                                            
data_015.all_sfs.self_calibrate('NH3', data_015, x_range=[400, 600])    
data_015.fit_MS_data(t_range=[50, 400])                                 

time_range = data_015.MS_fit_times

x_015=time_range.tolist()
y_015=data_015.MS_gasfracs.T[3].tolist()

data_022 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/23-01-20 022/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_022.assign_csv_fpath('022.csv')
data_022.assign_log_fpath('SW022.log')
data_022.get_log_data(CRD=True)

data_022.extract_MS_data(20)                                            
data_022.all_sfs.self_calibrate('NH3', data_022, x_range=[400, 600])    
data_022.fit_MS_data(t_range=[50, 400])                                 

time_range = data_022.MS_fit_times

x_022=time_range.tolist()
y_022=data_022.MS_gasfracs.T[3].tolist()

data_018 = Experiment('C:/Users/chem-sjoh4999/Documents/Part II Results/22-01-10 018/Mass Spec/',
                  I_factors=I_factors, sfs=all_sfs)
data_018.assign_csv_fpath('22-01-09-018.csv')
data_018.assign_log_fpath('SW018.log')
data_018.get_log_data(CRD=True)

data_018.extract_MS_data(20)                                            
data_018.all_sfs.self_calibrate('NH3', data_018, x_range=[400, 600])    
data_018.fit_MS_data(t_range=[50, 400])                                 

time_range = data_018.MS_fit_times

x_018=time_range.tolist()
y_018=data_018.MS_gasfracs.T[3].tolist()

#Create subplots figure and save as a figure

plt.rcParams['font.family']='serif'
fig, axes = plt.subplots(12, 1, sharex=True)
plt.xlim(50, 200)

axes[0].plot(x_019, y_019, label='019, 100.0:0.0', color='black', linewidth=0.9)
axes[0].set_ylim(-0.02, 0.6)

axes[1].plot(x_029, y_029, label='029, 83.3:16.7', color='red', linewidth=0.9)
axes[1].set_ylim(-0.02, 0.6)

axes[2].plot(x_033, y_033, label='033, 75.0:25.0', color='black', linewidth=0.9)
axes[2].set_ylim(-0.02, 0.6)

axes[3].plot(x_021, y_021, label='021, 66.7:33.3', color='red', linewidth=0.9)
axes[3].set_ylim(-0.02, 0.6)

axes[4].plot(x_012, y_012, label='012, 58.3:41.7', color='black', linewidth=0.9)
axes[4].set_ylim(-0.02, 0.6)

axes[5].plot(x_007, y_007, label='007, 50.0:50.0', color='red', linewidth=0.9)
axes[5].set_ylim(-0.02, 0.6)

axes[6].plot(x_030, y_030, label='030, 41.7:58.3', color='black', linewidth=0.9)
axes[6].set_ylim(-0.02, 0.6)

axes[7].plot(x_017, y_017, label='029, 33.3:66.7', color='red', linewidth=0.9)
axes[7].set_ylim(-0.02, 0.6)

axes[8].plot(x_016, y_016, label='016, 25.0:75.0', color='black', linewidth=0.9)
axes[8].set_ylim(-0.02, 0.6)

axes[9].plot(x_015, y_015, label='015, 16.7:83.3', color='red', linewidth=0.9)
axes[9].set_ylim(-0.02, 0.6)

axes[10].plot(x_022, y_022, label='022, 8.3:91.7', color='black', linewidth=0.9)
axes[10].set_ylim(-0.02, 0.6)

axes[11].plot(x_018, y_018, label='018, 0:100', color='red', linewidth=0.9)
axes[11].set_ylim(-0.02, 0.6)

axes[0].title.set_text('H2 Release in NaCa(NH2)3 Synthesis')
fig.subplots_adjust(hspace=0)

plt.xlabel('Time', color = 'black', fontsize='14', horizontalalignment='center')
axes[3].set_ylabel('Gas Fraction', fontsize='14')

for i in range(1, 12):
    axes[i-1].tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    axes[i-1].spines["bottom"].set_visible(False)
    axes[i].spines["top"].set_visible(False)
    
for i in range(12):
    axes[i].tick_params(axis='y', which='both', left=False, top=False, labelleft=False)

axes[0].annotate('100.0:0.0', xy=(200, 0.3), xytext=(200, 0.3), color='black', fontsize=12)
axes[1].annotate('83.3:16.7', xy=(200, 0.3), xytext=(200, 0.3), color='red', fontsize=12)
axes[2].annotate('75.0:25.0', xy=(200, 0.3), xytext=(200, 0.3), color='black', fontsize=12)
axes[3].annotate('66.7:33.3', xy=(200, 0.3), xytext=(200, 0.3), color='red', fontsize=12)
axes[4].annotate('58.3:41.7', xy=(200, 0.3), xytext=(200, 0.3), color='black', fontsize=12)
axes[5].annotate('50.0:50.0', xy=(200, 0.3), xytext=(200, 0.3), color='red', fontsize=12)
axes[6].annotate('41.7:58.3', xy=(200, 0.3), xytext=(200, 0.3), color='black', fontsize=12)
axes[7].annotate('33.3:66.6', xy=(200, 0.3), xytext=(200, 0.3), color='red', fontsize=12)
axes[8].annotate('25.0:75.0', xy=(200, 0.3), xytext=(200, 0.3), color='black', fontsize=12)
axes[9].annotate('16.7:83.3', xy=(200, 0.3), xytext=(200, 0.3), color='red', fontsize=12)
axes[10].annotate('8.3:91.7', xy=(200, 0.3), xytext=(200, 0.3), color='black', fontsize=12)
axes[11].annotate('0.0:100.0', xy=(200, 0.3), xytext=(200, 0.3), color='red', fontsize=12)

fig.set_figheight(20)
fig.set_figwidth(10)


