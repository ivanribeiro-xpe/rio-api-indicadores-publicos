import requests
import pandas as pd


def get_json_api(url: str, params: dict | None = None) -> dict:
    """
    Consome uma API pública e retorna o resultado em formato JSON.
    """
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def get_arcgis_layer(
    url: str,
    out_fields: str = "*",
    return_geometry: bool = False
) -> pd.DataFrame:
    """
    Consome uma camada pública ArcGIS REST e retorna os atributos em um DataFrame.
    """
    params = {
        "where": "1=1",
        "outFields": out_fields,
        "f": "json",
        "returnGeometry": str(return_geometry).lower(),
        "outSR": 4326
    }

    data = get_json_api(url, params=params)
    features = data.get("features", [])

    records = [
        feature.get("attributes", {})
        for feature in features
    ]

    return pd.DataFrame(records)
