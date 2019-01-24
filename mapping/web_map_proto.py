import folium
#imort csv
import pandas
volcanoes = pandas.read_csv("Volcanoes_USA.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
elev = list(volcanoes["ELEV"])
name = list(volcanoes["NAME"])
#volcanoes = list(csv.reader(open("Volcanoes_USA.txt","r")))
#volcanoes = volcanoes[1:]
def icon_color(elevation):
    if elevation <= 1000:
        return "green"
    elif 1000 < elevation <= 3000:
        return "orange"
    else:
        return "red"

m = folium.Map(location = [45.9297981,-121.8209991],zoom_start = 6)

fgv = folium.FeatureGroup(name = "volcanoes")

for la,ln,el,nm in zip(lat,lon,elev,name):
#    fg.add_child(folium.Marker(location = [la,ln],popup =folium.Popup("Mount "+ nm +", Elevation is "+ str(el) +" m",parse_html = True),icon = folium.Icon(color = icon_color(el))))
    fgv.add_child(folium.CircleMarker(location = [la,ln],radius = 6, popup =folium.Popup("Mount "+ nm +", Elevation is "+ str(el) +" m",
    parse_html = True),fill_color = icon_color(el),fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "population")


fgp.add_child(folium.GeoJson(data = open("world.json","r",encoding = "utf-8-sig").read(),style_function = lambda x:{"fillColor" : "green" if x["properties"]["POP2005"] < 10000000
else "blue" if 10000000 <= x["properties"]["POP2005"] < 20000000
else "orange" if 20000000 <= x["properties"]["POP2005"] < 50000000 else "yellow" if 50000000 <= x["properties"]["POP2005"] < 100000000
else "red"}))

m.add_child(fgv)
m.add_child(fgp)
m.add_child(folium.LayerControl())
m.save("first_map.html")
