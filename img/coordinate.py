# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:57:59 2024

@author: Maqiang
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 设置全局参数
plt.rcParams.update({
    'figure.figsize': (10/2.54 *2 , 7/2.54 * 1.2),  # 将宽度从cm转换为英寸
    'font.family': 'Times New Roman',
    'font.size': 14,
    'axes.labelsize': 14, # 坐标名称
    'axes.titlesize': 14, # 图名
    'xtick.labelsize': 12, #刻度大小
    'ytick.labelsize': 12,
    'font.serif': ['Times New Roman'],
    'lines.linewidth': 1.2,  # 线宽
    'axes.linewidth': 0.7,  # 坐标轴线宽
    'grid.linewidth': 0.7,  # 网格线宽
    'legend.fontsize': 11,
    'mathtext.fontset': 'stix',  # 使用STIX字体
    'figure.subplot.left': 0.18,   # 左边距
    'figure.subplot.right': 0.95,  # 右边距
    'figure.subplot.bottom': 0.18,  # 下边距
    'figure.subplot.top': 0.95,     # 上边距
})

colors = ['#e5c494', '#f7b6d2', '#bcbd22', '#17becf']
markers = ['', '', '', '']
#markers = ['o', 's', '^', 'd']
lstyles = ['-', '-.', ':', '--']
labels = ['$0^{\circ}$', '$30^{\circ}$', '$60^{\circ}$', '$90^{\circ}$']

fig, (ax1, ax2) = plt.subplots(1, 2)
alpha = np.arange(0, 91,15)
file_name= 'coordinate.csv'
df = pd.read_csv(file_name,  header=None)
for i in range(0,df.shape[1],3):
    Eq = df.iloc[:, i]
    coor = df.iloc[:, i+1]
    cn0 = df.iloc[:, i+2]
    ax1.plot(Eq, coor, color=colors[int(i/3)], label=labels[int(i/3)])
    ax1.set_xlabel( 'Deviatoric strain, '+r'$\gamma_q$ (%)')
    ax1.set_ylabel( 'Coordination number, '+r'$C_n$')
    ax1.set_xlim(0, 1.5)
    ax1.set_ylim(3.4,4.2)
    
    ax2.plot( Eq, cn0, color=colors[int(i/3)])
    ax2.set_xlabel( 'Deviatoric strain, '+r'$\gamma_q$ (%)')
    ax2.set_ylabel( r'$C_n^0$  (%)')
    ax2.set_xlim(0, 1.5)
    ax2.set_ylim(18,26)
     
        
        
        
labels = ['(a)', '(b)']
for i, ax in enumerate(fig.axes):
    ax.text(0.97, 0.1, labels[i], transform=ax.transAxes, 
            ha='right', va='top')        

        

plt.tight_layout()
ax1.legend()
plt.savefig('CSR=0.15.svg')
        
plt.show()

    