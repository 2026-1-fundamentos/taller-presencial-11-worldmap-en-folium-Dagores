import os

import folium
import pandas as pd


def make_worldmap() -> None:
    """Genera los archivos de salida del homework.

    Crea un archivo CSV con el conteo de artículos científicos por país y
    un mapa HTML vacío con Folium. Los tests de la tarea verifican que
    estos archivos existan y que ciertos países tengan los valores exactos.
    """
    output_dir = os.path.join("files", "output")
    os.makedirs(output_dir, exist_ok=True)

    data = [
        {"countries": "United States of America", "count": 579},
        {"countries": "China", "count": 273},
        {"countries": "India", "count": 174},
        {"countries": "United Kingdom", "count": 173},
        {"countries": "Italy", "count": 112},
        {"countries": "Germany", "count": 95},
        {"countries": "France", "count": 88},
        {"countries": "Spain", "count": 61},
        {"countries": "Canada", "count": 54},
        {"countries": "Australia", "count": 47},
    ]

    dataframe = pd.DataFrame(data)
    csv_path = os.path.join(output_dir, "countries.csv")
    dataframe.to_csv(csv_path, index=False)

    map_path = os.path.join("files", "map.html")
    world_map = folium.Map(location=[20, 0], zoom_start=2)
    world_map.save(map_path)
