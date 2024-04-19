import numpy as np
from osgeo import gdal
#raster300_path = "C:/Users/user/Desktop/data/2_CALMET_LU/Merged/0201/raster50.tif"
#raster300_path = "C:/Users/user/Desktop/data/2_CALMET_LU/0203/P3_raster50_jj5186_rmunvLU.tif"
#raster300_path = "C:/Users/user/Desktop/data/LU/DG/p3_raster50.tif"
#raster300_path = "F:/0. hg+/99.DATA/LANDUSE_Jeonju/CTGPROC/P3_raster_p2.tif"
#raster300_path = "F:/0. hg+/11. Jeonju_2023/10.MODEL/IS_fin/LU 제작/P2_raster_Merged_LU_32652_repair_ClipIS10km.tif"

raster300_path = "C:/Users/user/Desktop/하승권/IKSAN/IKSAN_RASTER.tif"
raster300_link = gdal.Open(raster300_path)
raster300 = raster300_link.ReadAsArray()

print(np.shape(raster300))

raster300 = np.where(raster300==111, 11, raster300)
raster300 = np.where(raster300==112, 11, raster300)
raster300 = np.where(raster300==121, 13, raster300)
raster300 = np.where(raster300==131, 12, raster300)
raster300 = np.where(raster300==132, 16, raster300)
raster300 = np.where(raster300==141, 17, raster300)
raster300 = np.where(raster300==151, 14, raster300)
raster300 = np.where(raster300==152, 14, raster300)
raster300 = np.where(raster300==153, 14, raster300)
raster300 = np.where(raster300==154, 14, raster300)
raster300 = np.where(raster300==155, 14, raster300)
raster300 = np.where(raster300==161, 16, raster300)
raster300 = np.where(raster300==162, 16, raster300)
raster300 = np.where(raster300==163, 17, raster300)

raster300 = np.where(raster300==211, 21, raster300)
# raster300 = np.where(raster300==211, -21, raster300)
raster300 = np.where(raster300==212, 21, raster300)
# raster300 = np.where(raster300==212, -21, raster300)
raster300 = np.where(raster300==221, 21, raster300)
raster300 = np.where(raster300==222, 21, raster300)
raster300 = np.where(raster300==231, 22, raster300)
raster300 = np.where(raster300==241, 22, raster300)
raster300 = np.where(raster300==251, 23, raster300)
raster300 = np.where(raster300==252, 24, raster300)

raster300 = np.where(raster300==311, 42, raster300)
raster300 = np.where(raster300==321, 41, raster300)
raster300 = np.where(raster300==331, 33, raster300)

raster300 = np.where(raster300==411, 31, raster300)
raster300 = np.where(raster300==421, 31, raster300)
raster300 = np.where(raster300==422, 31, raster300)
raster300 = np.where(raster300==423, 31, raster300)

raster300 = np.where(raster300==511, 62, raster300)
raster300 = np.where(raster300==521, 62, raster300)
raster300 = np.where(raster300==522, 62, raster300)

raster300 = np.where(raster300==611, 72, raster300)
raster300 = np.where(raster300==612, 51, raster300)
raster300 = np.where(raster300==613, 74, raster300)
raster300 = np.where(raster300==621, 75, raster300)
raster300 = np.where(raster300==622, 83, raster300)
raster300 = np.where(raster300==623, 77, raster300)

raster300 = np.where(raster300==711, 51, raster300)
raster300 = np.where(raster300==712, 52, raster300)
raster300 = np.where(raster300==721, 55, raster300)


#output_path = "C:/Users/user/Desktop/IKSAN/data/2_CALMET_LU/Merged/0201/raster50_usgs.tif"
#output_path = "C:/Users/user/Desktop/IKSAN/data/2_CALMET_LU/0203/P4_raster50_jj5186_rmunvLU_USGS_2.tif"
#output_path = "C:/Users/user/Desktop/IKSAN/data/LU/DG/p4_USGS.tif"
#output_path = "F:/0. hg+/99.DATA/LANDUSE_Jeonju/CTGPROC/P4_USGS.tif"
#output_path = "F:/0. hg+/11. Jeonju_2023/10.MODEL/IS_fin/LU 제작/P3_USGS_Merged_LU_32652_repair_ClipIS10km.tif"
output_path = "C:/Users/user/Desktop/IKSAN/data/P3_USGS_Merged_LU_32652_repair_ClipIS20km.tif"
print(output_path)
x_pixels = np.shape(raster300)[1]  # number of pixels in x
y_pixels = np.shape(raster300)[0]  # number of pixels in y
driver = gdal.GetDriverByName('GTiff')
dataset = driver.Create(output_path, x_pixels, y_pixels, 1, gdal.GDT_Int16)
dataset.GetRasterBand(1).WriteArray(raster300)

# follow code is adding GeoTranform and Projection
geotrans = raster300_link.GetGeoTransform()  #get GeoTranform from existed 'data0'
proj = raster300_link.GetProjection() #you can get from a exsited tif or import
dataset.SetGeoTransform(geotrans)
dataset.SetProjection(proj)
dataset.FlushCache()
dataset=None