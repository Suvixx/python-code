
import numpy as np
import matplotlib.pyplot as plt


def normalizedata(array): # normalize data in the range [0, 100]
    normarray=[] 
    for x in array:
        normx=((x - min(array))/(max(array) - min(array)))*100
        normarray.append(normx)

    return np.array(normarray)


cov1=np.array([36.29,
60.77,
79.66,
90.26,
95.16,
99.08,
99.92,
100,
54.39,
91.69,
98.41,
100,
75.12,
99.8,
100
])

pref1=np.array([92.22,
191.02,
280.56,
363.78,
407.14,
436.01,
451.93,
457.87,
167.97,
350.2,
411.99,
440.23,
268.15,
409.74,
427.43
])


cov2=np.array([39.19,
60.74,
79.65,
90.25,
95.42,
99.08,
99.92,
100,
54.05,
91.69,
98.41,
100,
75.12,
99.8,
100
])

pref2=np.array([92.63,
191,
280.68,
366.08,
403.57,
436.01,
451.8,
457.49,
168.46,
350.2,
98.4,
440.22,
268.17,
409.74,
427.38
])

normcov1=normalizedata(cov1)
normcov2=normalizedata(cov2)
normpref1=normalizedata(pref1)
normpref2=normalizedata(pref2)

##print(normcov1)
##print(normcov2)
##print(normpref1)
##print(normpref1)

##data=[]
##data=[list(normcov2-normcov1),list(normpref2-normpref1)] 
data1 = normcov2-normcov1
data2 = normpref2-normpref1
index = ['(1, 800)', '(2, 800)', '(3, 800)', '(4, 800)', '(5, 800)', '(6, 800)', '(7, 800)', '(8, 800)', '(1, 1200)', '(2, 1200)', '(3, 1200)', '(4, 1200)', '(1, 1600)', '(2, 1600)', '(3, 1600)']
r = np.arange(len(index))
bar_width = 0.25
r1 = [x + bar_width for x in r]
print(r)
#print(data1)
#print(data2)
#print(index)

fig, (ax1,ax2) = plt.subplots(2,1,sharex = True)
ax1.spines['bottom'].set_visible(False)
ax1.tick_params(axis='x',which='both',bottom=False)
ax2.spines['top'].set_visible(False)

##bs = 500
##ts = 1000

ax2.set_ylim(-100, -70)
ax1.set_ylim(-1, 3)
ax2.set_xticklabels( ('(1, 800)', '(2, 800)', '(3, 800)', '(4, 800)', '(5, 800)', '(6, 800)', '(7, 800)', '(8, 800)', '(1, 1200)', '(2, 1200)', '(3, 1200)', '(4, 1200)', '(1, 1600)', '(2, 1600)', '(3, 1600)'), rotation = 25)
ax2.set_xticks(r1)
ax1.axhline(linewidth = 1, color ='k') 

bars1 = ax1.bar(r, data1,bar_width, color = 'm')
bars2 = ax2.bar(r, data1,bar_width,color = 'm')
bars3 = ax1.bar(r1, data2,bar_width, color = 'c')
bars4 = ax2.bar(r1, data2,bar_width, color = 'c')

for tick in ax2.get_xticklabels():
    tick.set_rotation(30)
d = .003  
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
ax2.plot((-d, +d), (-d, +d), **kwargs)      
ax2.plot((1 - d, 1 + d), (-d, +d), **kwargs)
kwargs.update(transform=ax2.transAxes)  
ax1.plot((-d, +d), (1 - d, 1 + d), **kwargs)  
ax1.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

for b1, b2, b3, b4 in zip(bars1, bars2, bars3, bars4):
    posx = b2.get_x() + b2.get_width()/2.
    if b2.get_height() > -70:
        ax2.plot((posx-3*d, posx+3*d), (1 - d, 1 + d), color='k', clip_on=False,
                 transform=ax2.get_xaxis_transform())
    if b1.get_height() > -1:
        ax1.plot((posx-3*d, posx+3*d), (- d, + d), color='k', clip_on=False,
                 transform=ax1.get_xaxis_transform())
    if b3.get_height() > -70:
        ax2.plot((posx-3*d, posx+3*d), (1 - d, 1 + d), color='k', clip_on=False,
                 transform=ax2.get_xaxis_transform())
    if b4.get_height() > -1:
        ax1.plot((posx-3*d, posx+3*d), (- d, + d), color='k', clip_on=False,
                 transform=ax1.get_xaxis_transform())

plt.show()


