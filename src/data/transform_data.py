"""Esta función mediante el uso de pandas transforma los datos del formato XLS y XLSX a un archivo separado por comas"""

def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """

    import pandas as pd
    import openpyxl


    """mediante el ciclo se juntan los archivos bajo el mismo formato csv"""

    import pandas as pd

    for year in range(1995, 2022):
        
        if year <= 1999:
            file_name = f'data_lake/landing/{year}.xlsx'
            df = pd.read_excel(file_name, sheet_name = 0, header = 3)
            df = df.iloc[:, :25]
            new_file = f'data_lake/raw/{year}.csv'
            df.to_csv(new_file, index=False)
        
        elif year > 1999 and year <= 2015:
            file_name = f'data_lake/landing/{year}.xlsx'
            df = pd.read_excel(file_name, sheet_name = 0, header = 2)
            df = df.iloc[:, :25]
            new_file = f'data_lake/raw/{year}.csv'
            df.to_csv(new_file, index=False)
        
        elif year > 2015 and year <= 2017:
            file_name = f'data_lake/landing/{year}.xls'
            df = pd.read_excel(file_name, sheet_name = 0, header = 2)
            df = df.iloc[:, :25]
            new_file = f'data_lake/raw/{year}.csv'
            df.to_csv(new_file, index=False)

        else:
            file_name = f'data_lake/landing/{year}.xlsx'
            df = pd.read_excel(file_name,  sheet_name = 0)
            df = df.iloc[:, :25]
            new_file = f'data_lake/raw/{year}.csv'
            df.to_csv(new_file, index=False)
            
    return    


#raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
    
