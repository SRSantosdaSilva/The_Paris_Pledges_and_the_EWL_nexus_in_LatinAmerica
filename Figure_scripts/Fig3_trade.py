# This script plots trade volumes for crops as shown in Figure 3, Santos da Silva et al. (2018)
# Note that this script was tested only in python 2.7

import numpy as np
import matplotlib.pyplot as plt

#Dimension = 9 (years 2010 to 2050 every 5 years)
dim = 9    # dimension

#Filling in vectors:
# Note NDC refers to NDC_FullTech scenario data

year = [2010,2015,2020, 2025, 2030, 2035, 2040, 2045, 2050]
REF_ARG = [1.000, 1.090, 1.182, 1.317, 1.445, 1.561, 1.684, 1.788, 1.862]
NDC_ARG = [1.000, 1.090, 1.186, 1.346, 1.526, 1.641, 1.857, 2.074, 2.267]
NDCNOCCS_ARG = [1.000, 1.090, 1.187, 1.374, 1.609, 1.863, 2.195, 2.459, 2.721]
REF_BRA = [1.000, 1.374, 3.327, 2.754, 2.593, 3.669, 4.636, 5.808, 7.023]
NDC_BRA = [1.000, 1.374, 3.312, 2.022, 0.313, 5.811, 9.493, 11.697, 13.656]
NDCNOCCS_BRA = [1.000, 1.374, 3.369, 1.784, -0.796, 2.305, 6.722, 12.862, 16.930]
REF_COL = [-1.000, -0.701, -0.109, 2.110, 4.412, 7.787, 11.271, 13.924, 15.326]
NDC_COL = [-1.000, -0.701, -0.104, 2.950, 6.484, 7.094, 7.381, 8.326, 9.991]
NDCNOCCS_COL = [-1.000, -0.701, -0.055, 3.717, 8.801, 13.304, 16.211, 16.677, 18.130]
REF_MEX = [-1.000, -0.921, -1.101, -0.734, -0.476, -0.547, -0.548, -0.665, -0.875]
NDC_MEX = [-1.000, -0.921, -1.117, -0.554, 0.180, -0.358, -0.412, -0.475, -0.193]
NDCNOCCS_MEX = [-1.000, -0.921, -1.108, -0.390, 0.694, 1.096, 1.456, 0.872, 0.801]

# Figure Aspects
fig1 = plt.figure(figsize=[8,4.5])
ax1 = plt.subplot2grid((1,2),(0,0),colspan=1)
plt.setp(ax1.get_xticklabels())
ax2 = plt.subplot2grid((1,2),(0,1),colspan=1)
plt.setp(ax2.get_xticklabels())

ax1.plot(year,REF_ARG, c='b', label='REF_Arg')
ax1.plot(year, NDC_ARG, c='b', ls='--',label='NDC_FullTech_Arg')
ax1.plot(year, NDCNOCCS_ARG, c='b', ls=':', label='NDC_NOCCS_Arg')
ax1.plot(year,REF_MEX, c='r', label='REF_Mex')
ax1.plot(year, NDC_MEX, c='r', ls='--',label='NDC_FullTech_Mex')
ax1.plot(year, NDCNOCCS_MEX, c='r', ls=':', label='NDC_NOCCS_Mex')
ax2.plot(year, REF_BRA, c='g', label='REF_Bra')
ax2.plot(year, NDC_BRA, c='g', ls='--',label='NDC_FullTech_Bra')
ax2.plot(year, NDCNOCCS_BRA, c='g', ls=':',  label='NDC_NOCCS_Bra')
ax2.plot(year, REF_COL, c='k', label='REF_Col')
ax2.plot(year, NDC_COL, c='k', ls='--', label='NDC_FullTech_Col')
ax2.plot(year, NDCNOCCS_COL, c='k', ls=':',  label='NDC_NOCCS_Col')

ax1.set_title('Net Exports for Crops\nArgentina / Mexico')
ax2.set_title('Net Exports for Crops\nBrazil / Colombia')
ax1.set_ylim([-2.0,4.0])
ax1.set_xlim([2010,2050])
ax2.set_ylim([-2.0,25.0])
ax2.set_xlim([2010,2050])
ax1.grid(True,linestyle=':',linewidth=0.6)
ax2.grid(True,linestyle=':',linewidth=0.6)
ax1.legend(fontsize='small')
ax2.legend(fontsize='small')
ax1.text(2045.0,-1.91,'(a)', fontsize='x-large')
ax2.text(2045.0,-1.6,'(b)', fontsize='x-large')

plt.show()
 
