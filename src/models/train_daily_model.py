"""se prepara un dataframe de entrenamiento a partir de los precios diarios y se realiza limpieza de los datos faltantes"""

def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """

    import pandas as pd
    import numpy as np
    from sklearn.neural_network import MLPRegressor
    import pickle

    """prepación de datos"""

    df_train_data = pd.read_csv('data_lake/business/features/precios-diarios.csv')
    df_model_data = df_train_data.dropna()
    X = df_model_data.iloc[:, -1]
    X = np.array(X).reshape(-1, 1)
    y = df_model_data.iloc[:, 2]


    H=1

    MLP = MLPRegressor(
        hidden_layer_sizes= (H,),
        activation='logistic',
        learning_rate='adaptative',
        momentum= 0.0,
        learning_rate_init= 0.1,
        max_iter= 10000,
    )


    """entrenamiento del modelo"""

    MLP.fit(X[:7000],y[:7000])


    """guardar"""

    pickle.dump(MLP, open('src/models/precios-diarios.pkl', 'wb'))

    #raise NotImplementedError("Implementar esta función")


    return

if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
