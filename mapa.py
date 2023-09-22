import folium
#! Esto sirve para crear un mapa con marcadores, primero creo un mapa en una posicion inicial y luego agrego marcadores
#! La idea es coon el buscar hacer que muestre la posicion que queremos

def create_map():
    mapa = folium.Map(location=[4.570868, -74.297333], zoom_start=5.5)
    mapa.save("map.html")
    return mapa

def create_maker(nombre, latitud, longitud, mape):
    folium.Marker([latitud,longitud], popup=nombre).add_to(mape)
    mape.save("map.html")


#? https://python-visualization.github.io/folium/latest/getting_started.htmlhttps://python-visualization.github.io/folium/latest/getting_started.html
#? ver lo que se puede hacer con la librería xdd