from extract_transform import modello
import pymysql

# Funzione per ottenere la stringa di connessione
def _getconnection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="chicago_db"
    )

# Funzione per il caricamento dei dati nella main table
def load(df):
    with _getconnection() as connection:
        with connection.cursor() as cursor:
            sql = ("INSERT INTO air_pollution (mean_temp, dew_point, registration_date, pm10_mean, ozone_mean, no2_mean) "
                   "VALUES (%s, %s, %s, %s, %s, %s)")
            valori = [(
                row["mean_temp"],
                row["dew_point"],
                row["date"],
                row["pm10_mean"],
                row["ozone_mean"],
                row["no2_mean"]
            ) for _, row in df.iterrows()]

            cursor.executemany(sql, valori)
            connection.commit()

            print("Dati caricati con successo")

#load(modello.dataframe_sistemato)