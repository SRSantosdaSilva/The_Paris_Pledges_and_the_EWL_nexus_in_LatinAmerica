# The_Paris_Pledges_and_the_EWL_nexus_in_LatinAmerica

This repository includes the scenarios results generated by the Global Change Assessment Model (GCAM), which are reported in Santos da Silva et al. (2019). As discussed in the manuscript, the study explores the Energy-Water-Land nexus interlinkages in Latin America under mitigation scenarios based on the emissions reductions pledges made by countries under the Paris Agreement. 

The repository contains three folders: 
-	Data: Raw GCAM outputs for the variables relevant for this analysis. Each .csv file corresponds to a single scenario specified by the file name. Data are in the original format as extracted from the GCAM output database.
-	Figure_Scripts: IDL and python scripts used to process data and plot the key figures of the paper.
-	 Supporting_Excel_sheets: Sheets used to process, analyze and visualize data.

COMPUTE_LAND.pro and COMPUTE_LAND_ALLOC_REF.pro in the Figure_Scripts directory process raw GCAM outputs of land allocation and generate plots of land allocation by country and scenario as illustrated in Figure 2. COMPUTE_WATER.pro and COMPUTE_WATER_REF.pro in the Figure_Scripts directory process raw GCAM outputs of water withdrawals by sector and generate the bar charts presented in Figure 3. The .csv files required as input files are indicated in each script. Note that it is assumed that the input .csv files and the idl scripts are in the same working directory.

The Supporting_Excel_sheets directory contains the following excel sheet: Figure1_PrimaryEnergy_Consumption.xlsx. Figure1_PrimaryEnergy_Consumption.xlsx filters the raw GCAM outputs of primary energy consumption (located in the data folder), presenting these results by country and scenario. This sheet also produces the plots presented in Figure 1. 

Requirements: IDL and Python. The IDL scripts have been used in IDL 8.0. Python scripts have only been tested on Python 2.7. Python required libraries: Numpy and Matplotlib.

Citation:
Santos Da Silva SR, Miralles-Wilhelm F, Muñoz-Castillo R, Clarke LE, Braun CJ, Delgado A, et al. (2019) The Paris pledges and the energywater-land nexus in Latin America: Exploring implications of greenhouse gas emission reductions. PLoS ONE 14(4): e0215013. https://doi.org/10.1371/journal.pone.0215013
