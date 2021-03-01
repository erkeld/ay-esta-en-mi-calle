import numpy as np
import geopandas as gpd
import pandas as pd
from pandas import DataFrame
import contextily as ctx
import matplotlib.pyplot as plt
from shapely.ops import cascaded_union
from geovoronoi.plotting import subplot_for_map, plot_voronoi_polys_with_points_in_area
from geovoronoi import voronoi_regions_from_coords, points_to_coords
df = pd.read_excel('primarias_muestra.xlsx', index_col=0)########|
Escuelas_primarias = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.long, df.lat)) ### Geodataframe
Escuelas_primarias.head()
Escuelas_primarias.crs = "EPSG:4326"
#Alcaldias = gpd.read_file("Alcaldias.shp")

Miguel_Hidalgo = Alcaldias.drop([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15],axis=0)
Alcaldia = Miguel_Hidalgo
fig, ax = plt.subplots(figsize=(12, 10))
Alcaldia.plot(ax=ax, color="Green")
Escuelas_primarias.plot(ax=ax, markersize=3.5, color="black")
ax.axis("off")
plt.axis('equal')
plt.show()
Alcaldia = Alcaldia.to_crs(epsg=3395)
gdf_proj = Escuelas_primarias.to_crs(Alcaldia.crs)
Alcaldia_shape = cascaded_union(Alcaldia.geometry)
coords = points_to_coords(gdf_proj.geometry)
poly_shapes, pts, poly_to_pt_assignments = voronoi_regions_from_coords(coords, Alcaldia_shape)
fig, ax = subplot_for_map(figsize=(14.5,10))
plot_voronoi_polys_with_points_in_area(ax, Alcaldia_shape, poly_shapes, pts, poly_to_pt_assignments)
ax.set_title('Diagrama de voronoi Escuelas primarias miguel hidalgo muestra')
plt.tight_layout()
plt.show()
