#This code integrates two peaks from a given sample, calculates their areas, visualizes the data along with the detected peaks, and provides useful statistical information about the peaks, including their integrals and positions. 
#It evidences my use of dictionaries and data management in Python

with open("C:/Users/chem-sjoh4999/Documents/Presenting Results/MS H integration Graph/Results/Combined time vs H2.txt",'r') as f:
    dict = {}
    Lines = f.readlines()
    for line in Lines:
        if line[:6]=='Sample':
            dict[line]={}
            current_sample=line
            dict[line]["time"]=[]
            dict[line]["H2"]=[]
        else:
            data=line.strip().split()
            dict[current_sample]["time"].append(float(data[0]))
            dict[current_sample]["H2"].append(float(data[1]))
print(dict)
    
x=dict["Sample_007\n"]["time"]
y=dict["Sample_007\n"]["H2"]

import matplotlib.pyplot as plt

import numpy as np
import scipy as sp
from scipy import signal
def integrate(Sample):
    x=dict[Sample]["time"]
    y=dict[Sample]["H2"]
    peaks, peak_dict =signal.find_peaks(y,height=0.01)
    peaks=list(peaks)
    print(peaks)
    plt.scatter([x[i] for i in peaks], [y[i] for i in peaks])
    plt.plot(x,y)
    centroid=int((peaks[0]+peaks[1])/2)
    Peak1=np.trapz(y[0:centroid],x[0:centroid],dx=x[1]-x[0])
    Peak2=np.trapz(y[centroid:-1],x[centroid:-1],dx=x[1]-x[0])
    print("Integral of Peak 1=",Peak1)
    print("Integral of Peak 2=",Peak2)
    print("Peak 1/ Peak 2=",Peak1/Peak2)
    print("Position of centroid=",centroid)
    plt.scatter(x[centroid],y[centroid],color='red')
    plt.show()
    return x[peaks[0]], x[peaks[1]]
x = []
y = []

print("Sample 029, 83.3:16.7")
peak1, peak2 =integrate("Sample_029\n") #83.3:16.7
x.append(83.3)
y.append(peak2)

print("Sample 033, 75:25")
peak1, peak2 =integrate("Sample_033\n") #83.3:16.7
x.append(75)
y.append(peak2)

print("Sample 021, 66.7:33.3")
peak1, peak2 =integrate("Sample_021\n") #66.7:33.3
x.append(66.7)
y.append(peak2)

print("Sample 012, 58.3:41.7")
peak1, peak2 =integrate("Sample_012\n") #58.3:41.7
x.append(58.3)
y.append(peak2)

print("Sample 007, 50:50")
peak1, peak2 =integrate("Sample_007\n") #50:50
x.append(50)
y.append(peak2)

print("Sample 030, 41.7:58.3")
peak1, peak2 =integrate("Sample_030\n") #41.7:58.3
x.append(41.7)
y.append(peak2)

print("Sample 017, 33.3:66.6")
peak1, peak2 =integrate("Sample_017\n") #33.3:66.6
x.append(33.3)
y.append(peak2)

print("Sample 016, 25:75")
peak1, peak2 =integrate("Sample_016\n") #25:75
x.append(25)
y.append(peak2)

print("Sample 015, 16.7:83.3")
peak1, peak2 =integrate("Sample_015\n") #16.7:83.3
x.append(16.7)
y.append(peak2)

plt.scatter(x,y)
plt.xlabel("Molar Percentage of Sodium Hydride in Starting Material")
plt.ylabel("Time of 2nd Hydrogen Release")
plt.show()
