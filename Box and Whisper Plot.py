#This code creates and box and whisker plot of the mole fraction of hydrogen gas release from multiple experiments
#It demonstrates my use of numpy and scipy packages, along with advanced data manipulation and statistical analysis 

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid


class Box:
    def __init__(self, centre, sigma1, sigma2, sigma3):
        self.centre = centre
        self.sigma1 = sigma1
        self.sigma2 = sigma2
        self.sigma3 = sigma3
    
    def __str__(self):
        s = f"Centre: {self.centre:.4f}\n"
        s += f"1 sigma: {self.sigma1[0]:.4f}, {self.sigma1[1]:.4f}\n"
        s += f"2 sigma: {self.sigma2[0]:.4f}, {self.sigma2[1]:.4f}\n"
        s += f"3 sigma: {self.sigma3[0]:.4f}, {self.sigma3[1]:.4f}"
        return s

class BoxData:
    def __init__(self, x, y, xmin, xmax, use_mode=None):
        use_mode = False if use_mode is None else True
        self.xmin = xmin
        self.xmax = xmax
        if type(x) == type(np.array([])):
            x = [x]
        if type(y) == type(np.array([])):
            y = [y]
        self.get_all_box_data(x, y, use_mode)
        
    def get_all_box_data(self, x, y, use_mode=False):
        boxvals = []
        for xvals, yvals in zip(x, y):
            boxvals.append(self.get_singlebox_data(xvals, yvals, use_mode))
        self.boxvals = boxvals
        
    def get_singlebox_data(self, x, y, use_mode=False):
        i0, i1 = np.searchsorted(x, [self.xmin, self.xmax])
        x = x[i0:i1+1]
        y = y[i0:i1+1]
        ysum = cumulative_trapezoid(y, initial=0)
        ysum /= ysum[-1]
        if use_mode:
            centre = x[y.argmax()]
        else:
            centre = np.interp(0.5, ysum, x)
        s1a, s1b, s2a, s2b, s3a, s3b = [np.interp(v / 100, ysum, x) for v in 
                                        [15.865, 84.135, 2.275,
                                         97.725, 0.135, 99.865]]
        return Box(centre, [s1a, s1b], [s2a, s2b], [s3a, s3b])
    
    def plot_boxes(self, yvals=None, figsize=(5, 4), boxheight=None):
        yvals = np.arange(len(self.boxvals)) if yvals is None else yvals
        boxheight = 1 / (len(self.boxvals) + 1) if boxheight is None else boxheight
        h = boxheight
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_xlim([self.xmin, self.xmax])
        for b, yv in zip(self.boxvals, yvals):
            ymin = yv - h / 2
            ymax = yv + h / 2
            ax.vlines(b.sigma2 + b.sigma3 + [b.centre], [ymin] * 5, [ymax] * 5,
                      color='k')
            ax.vlines(b.sigma1, [ymin] * 2, [ymax] * 2, color='k', ls='dashed')
            ax.hlines([yv, ymin, ymax, yv], 
                      [b.sigma3[0], b.sigma2[0], b.sigma2[0], b.sigma2[1]],
                      [b.sigma2[0], b.sigma2[1], b.sigma2[1], b.sigma3[1]],
                      color='k')
        fig.tight_layout()
        return fig, ax

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

def get_X_and_Y(Sample):
    x=dict[Sample]["time"]
    y=dict[Sample]["H2"]
    return x,y

Mole_Fractions=[]
X = []      #new repeated x
Y = []      #new repeated y

Mole_Fractions.append(83.3)
x,y = get_X_and_Y("Sample_029\n")
X.append(x)
Y.append(y)

Mole_Fractions.append(75)
x,y = get_X_and_Y("Sample_033\n")
X.append(x)
Y.append(y)

Mole_Fractions.append(66.7)
x,y = get_X_and_Y("Sample_021\n")
X.append(x)
Y.append(y)

Mole_Fractions.append(58.3)
x,y = get_X_and_Y("Sample_012\n")
X.append(x)
Y.append(y)

Mole_Fractions.append(50)
x,y = get_X_and_Y("Sample_007\n")
X.append(x)
Y.append(y)

Mole_Fractions.append(41.7)
x,y = get_X_and_Y("Sample_030\n")
X.append(x)
Y.append(y)

Mole_Fractions.append(33.3)
x,y = get_X_and_Y("Sample_017\n")
X.append(x)
Y.append(y)

Mole_Fractions.append(25)
x,y = get_X_and_Y("Sample_016\n")
X.append(x)
Y.append(y)

Mole_Fractions.append(16.7)
x,y = get_X_and_Y("Sample_015\n")
X.append(x)
Y.append(y)

data = np.array([
      [83.3, get_X_and_Y("Sample_029\n")],
      [75, get_X_and_Y("Sample_033\n")],
      [66.7, get_X_and_Y("Sample_021\n")],
      [58.3, get_X_and_Y("Sample_012\n")],
      [50, get_X_and_Y("Sample_007\n")],
      [41.7, get_X_and_Y("Sample_030\n")],
      [33.3, get_X_and_Y("Sample_017\n")],
      [25, get_X_and_Y("Sample_016\n")],
      [16.7, get_X_and_Y("Sample_015\n")]
])

repeated_x = X
repeated_y = Y
example = BoxData(repeated_x, repeated_y, 0, 400)
fig, ax = example.plot_boxes(boxheight=5, yvals=Mole_Fractions)
ax.set_xlabel('Time / min')
ax.set_ylabel('Molar Percentage of NaH in Startting Material')
fig.tight_layout()