import folium
import pandas as pd
import os

states = os.path.join('data', 'us-states.json')
unemployement_data = os.path.join('data', 'us_unemployment.csv')
state_data = pd.read_csv(unemployement_data)

m = folium.Map(location=[48, -102], zoom_start=3)

m.choropleth(
    geo_data=states,
    name='choropleth',
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate %'
)

folium.LayerControl().add_to(m)

m.save('map2.html')
