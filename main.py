#Clear the Noise
#submitted February 2018
#last edited 06/08/20 (to work in Python 3 versions)
#
#Given: a dataset of two frequencies with multiple amp values for each
#One frequency is nonsense, the other is a sine wave
#Originally, I output each frequency set to determine which must be the sine wave
#From that point, I simply visualize the sine wave



#Sources:

#Stack Overflow: 'Python creating a dictionary of lists'
#https://stackoverflow.com/questions/960733/python-creating-a-dictionary-of-lists


from __future__ import division
from collections import defaultdict as dd
import numpy as np
import matplotlib.pyplot as mplot
from scipy.interpolate import UnivariateSpline

data = open("PuceFinch_ch1.csv", "r")
data = data.read()
data = data.split("\n")
if (data[-1] == ""):
    data.pop()

s = [] #used for getting frequency, time, and amplitude values
ft = dd(list) #frequency - time pair
fa = dd(list) #frequency - amplitude pair

for index in range(0, len(data)):
    s = data[index].split(", ")
    ft[s[2]].append(s[0])
    fa[s[2]].append(s[1])

#Not the frequency we're looking for
tf1 = [ft['1.825562']]
af1 = [fa['1.825562']]

#The frequency we're looking for
tf2 = np.float32(ft['58.256220'])
af2 = np.float32(fa['58.256220'])

print (tf2[0])

mean = []
u = list(set(tf2))
u.sort()

sum1 = 0
count = 0
for x in range (0, len(u)):
    for y in range (0, len(tf2)):
        if u[x] == tf2[y]:
            sum1 += af2[y]
            count+=1
    avg = sum1/count
    mean.append(avg)
    sum1 = 0
    count = 0


mplot.title("Frequency 58.256220")
mplot.xlabel("Time (ms)")
mplot.ylabel("Amplitude")
mplot.plot(tf2, af2, 'ro')
mplot.plot(u, mean, color = "blue", linestyle = "-", linewidth = 2)
mplot.show()
