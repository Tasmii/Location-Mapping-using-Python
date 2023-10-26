import geopandas as gpd
import matplotlib.pyplot as plt
import requests
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])
print("Latitude:", latitude)
print("Longitude:", longitude)
gdf = gpd.GeoDataFrame(
    geometry=gpd.points_from_xy([longitude], [latitude], crs="EPSG:4326"),
    columns=["geometry"],
)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot()
png_image = plt.imread('C:\\Users\\narut\\Desktop\\Python\\git project\\211230.png')
imagebox = OffsetImage(png_image, zoom=0.01)
ab = AnnotationBbox(imagebox, (longitude, latitude), frameon=False)
ax.add_artist(ab)
plt.show()
