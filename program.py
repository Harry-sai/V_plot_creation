#importing libraries 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

#reading the file 
lr= pd.read_csv('PLOT_file.tsv', sep='\t', header='infer')

#Assigning colour to the plot  
colour="Blues"

#Giving labels
plt.title('V_plot')
plt.xlabel('Range')
plt.ylabel('Frequency')

#Plotting scattered plot 
plt.scatter(lr['x_axis'],lr['y_axis'], c=lr['Freq'], cmap=colour , vmin=1 ,vmax=100,s=10,marker="o")

#Giving code idea to read Freq coloumn for colour intensity
plt.colorbar(label='Freq')

#printing the plot
plt.show()


