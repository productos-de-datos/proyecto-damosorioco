"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
Descarga de los datos a la carpeta landing, se importan los datos desde la URL desde 1995 a 2022


"""


from gettext import install


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    import os
    import pandas as pd
    import sys    
    

    import requests
    ruta = "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/"

    for year in range(1995, 2022):
        if year in [2016,2017]:
            url = ruta + "{}.xls?raw=true".format(year)
            file = requests.get(url, allow_redirects=True)
            open('data_lake/landing/{}.xls'.format(year),"wb").write(file.content)
        else:
            url = ruta + "{}.xlsx?raw=true".format(year)
            file = requests.get(url, allow_redirects=True)
            open('data_lake/landing/{}.xlsx'.format(year),"wb").write(file.content)


    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    
    
    import doctest
    ingest_data()
    doctest.testmod()
