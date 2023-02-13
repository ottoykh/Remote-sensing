import numpy as np
import rasterio as rio
import earthpy as et
import earthpy.plot as ep

#Read and covert the .tiff geo-tagged image into array
band_4 = rio.open('LC08_L2SP_122044_20221224_20230103_02_T1_SR_B4.TIF')
band_4 = band_4.read(1)
band_4 = np.array(band_4).astype('float')

band_5 = rio.open('LC08_L2SP_122044_20221224_20230103_02_T1_SR_B5.TIF')
band_5 = band_5.read(1)
band_5 = np.array(band_5).astype('float')

#Normalized Difference Vegetation Index
NVDI = (band_5-band_4)/(band_5+band_4)

ep.plot_bands(NVDI,title="NVDI",cmap="BuGn")

plt.show()
