import numpy as np
import rasterio as rio
import earthpy as et
import earthpy.plot as ep
import earthpy.spatial as es
import matplotlib.pyplot as plt
from matplotlib import colors

#Read and covert the .tiff geo-tagged image into array
band_4 = rio.open('LC08_L2SP_122044_20221224_20230103_02_T1_SR_B4.TIF')
band_4 = band_4.read(1)
band_4 = np.array(band_4).astype('float')

band_5 = rio.open('LC08_L2SP_122044_20221224_20230103_02_T1_SR_B5.TIF')
band_5 = band_5.read(1)
band_5 = np.array(band_5).astype('float')

#Normalized Difference Vegetation Index
ndvi = es.normalized_diff(b1=band_5, b2=band_4)

#Compute the proportion of vegetation
Py = ((ndvi-0.2)/(1-0.2))**2

#Compute the emissivity from proportion of vegetation and NVDI
e = 0.004*Py+0.986

# Create the color mapping for NVDI
color_c_ndvi = ['#16489e', '#878b94', '#fff39c', '#8ce854', '#17d123', '#2d7a11']
# Create a color bar
c_ndvi = colors.ListedColormap(color_c_ndvi)
bounds = [-0.28,0.015,0.14,0.18,0.27,0.36]
n_nvdi = colors.BoundaryNorm(bounds, c_ndvi.N)

# Create the color mapping for Emissivity
color_c_e = ['#2d7a11','#17d123','#878b94','#fff39c','#16489e']
# Create a color bar
c_e = colors.ListedColormap(color_c_e)
bounds_2 = [0.980,0.986,0.9861,0.9862,0.9866]
n_e = colors.BoundaryNorm(bounds_2, c_e.N)

# Plot the color bar
ep.plot_bands(ndvi,cmap=c_ndvi,title="Land Cover classification with NDVI", norm=n_nvdi)
ep.plot_bands(e,cmap=c_e,title="Land Cover classification with Emissivity",norm=n_e)

# Show the figure
plt.show()
