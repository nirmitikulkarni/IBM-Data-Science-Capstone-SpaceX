"""Interactive site map using report-derived aggregates; not launch-level records."""
import folium
from pathlib import Path
sites=[
("CCAFS SLC 40",28.5618571,-80.577366,55,33,60.0),
("KSC LC 39A",28.6080585,-80.6039558,22,17,77.3),
("VAFB SLC 4E",34.632093,-120.610829,13,10,76.9)]
out=Path(__file__).resolve().parents[1]/"evidence"/"folium_launch_sites_map.html"
out.parent.mkdir(exist_ok=True)
m=folium.Map(location=[30.5,-100],zoom_start=4)
for name,lat,lon,n,s,rate in sites:
 popup=f"<b>{name}</b><br>Coordinates: {lat:.6f}, {lon:.6f}<br>Report records: {n}<br>Report successes: {s}<br>Success rate: {rate}%<br><em>Aggregates from submitted report, not re-computed.</em>"
 folium.Marker([lat,lon],tooltip=name,popup=folium.Popup(popup,max_width=300),icon=folium.Icon(color="blue",icon="rocket",prefix="fa")).add_to(m)
 folium.Circle([lat,lon],radius=10000,tooltip="10 km radius",fill=False).add_to(m)
m.save(out)
print(out)
