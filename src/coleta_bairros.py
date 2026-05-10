from pathlib import Path

from api_client import get_arcgis_layer


URL_BAIRROS = "https://pgeo3.rio.rj.gov.br/arcgis/rest/services/Cartografia/Limites_administrativos/MapServer/4/query"

CAMINHO_SAIDA = Path("data/raw/bairros.csv")


def main():
    """
    Coleta os bairros do município do Rio de Janeiro via API pública do DATA.RIO.
    """

    df_bairros = get_arcgis_layer(
        url=URL_BAIRROS,
        out_fields="objectid,nome,regiao_adm,area_plane,codbairro,codra,cod_rp,rp",
        return_geometry=False
    )

    CAMINHO_SAIDA.parent.mkdir(parents=True, exist_ok=True)

    df_bairros.to_csv(
        CAMINHO_SAIDA,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"Arquivo gerado com sucesso: {CAMINHO_SAIDA}")
    print(f"Total de registros coletados: {len(df_bairros)}")


if __name__ == "__main__":
    main()
