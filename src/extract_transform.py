from modello_base import ModelloBase
import pandas as pd

class DatasetCleaner(ModelloBase):

    # Metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione()

    # Metodo di sistemazione
    def sistemazione(self):
        # Copia del dataframe
        df_sistemato = self.dataframe.copy()

        # Rimappatura etichetta Unnamed: 0
        df_sistemato = df_sistemato.rename(columns={"Unnamed: 0":"id_air_pollution"})

        # Conversione date in formato data
        df_sistemato["date"] = pd.to_datetime(df_sistemato["date"])

        # Drop variabili univo valore univoco
        colonne_unico_valore = df_sistemato.nunique()[df_sistemato.nunique() < 2].index
        df_sistemato = df_sistemato.drop(colonne_unico_valore, axis=1)

        # Drop pm25tmean2
        df_sistemato = df_sistemato.drop(["pm25tmean2"], axis=1)

        # Sostituzione nan
        df_sistemato['date'] = pd.to_datetime(df_sistemato['date'])
        df_sistemato['year'] = df_sistemato['date'].dt.year
        df_sistemato['month'] = df_sistemato['date'].dt.month
        variabili_quantitative = ["tmpd", "dptp", "pm10tmean2"]
        for col in variabili_quantitative:
            df_sistemato[col] = df_sistemato.groupby(['year', 'month'])[col].transform(
                lambda x: x.fillna(x.median())
            )

        # Rimappatura etichette
        df_sistemato = df_sistemato.rename(columns={
            'tmpd': 'mean_temp',
            'dptp': 'dew_point',
            'pm10tmean2': 'pm10_mean',
            'o3tmean2': 'ozone_mean',
            'no2tmean2': 'no2_mean'
        })

        return df_sistemato

# Estrazione dataset
modello = DatasetCleaner("../Dataset/dataset.csv")
# Trasformazione
# Passo 1. Analisi generali del dataset
#modello.analisi_generali(modello.dataframe)
# Risultati:
# Osservazioni= 6940; Variabili= 9; Tipi= object, float e int; Valori nan= presenti
# Passo2. Analisi valori univoci
#modello.analisi_valori_univoci(modello.dataframe)
# Unnamed: 0 -> Rimappatura etichetta
# date -> Conversione in formato data
# city -> solo 1 valore univoco -> Drop attributo
# pm25tmean2 -> valori nan >50% -> Drop attributo
# tmpd -> un solo valore nan -> sostituzione nan con mediana
# dptp -> due valori nan -> sostituzione nan con mediana
# pm10tmean2 -> sostituzione nan con mediana
# Passo 3. Rimappatura etichetta Unnamed: 0
# Passo 4. Conversione date
# Passo 5. Drop variabili= city e pm25tmean2
# Passo 6. Analisi outliers prima della sostituzione
#modello.individuazione_outliers(modello.dataframe_sistemato, ["id_air_pollution", "date", "o3tmean2", "no2tmean2"])
# Risultati:
# tmpd= 0.01%
# dptp= 0.1%
# pm10tmean2= 3.4%
# Passo 7. Sostituisco i valori NaN con la mediana calcolata per gruppi definiti in base alla data (mese e anno)
# Passo 8. Analisi outliers dopo la sostituzione
#modello.individuazione_outliers(modello.dataframe_sistemato, ["id_air_pollution", "date", "o3tmean2", "no2tmean2"])
# Risultati:
# tmpd= 0.01%
# dptp= 0.1%
# pm10tmean2= 3.4%
# Valori non cresciuti -> lascio cosi
# Passo 9. Rimappatura etichette