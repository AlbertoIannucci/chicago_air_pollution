# 🏙️ Air Quality Chicago – Dataset Cleaning & ETL Pipeline

Questo progetto si occupa della **pulizia**, **trasformazione** e **caricamento** di un dataset sulla qualità dell'aria a Chicago, nell’ambito di un esercizio di esplorazione e analisi dei dati (EDA).

## 🔍 Obiettivo

Analizzare un dataset ambientale reale per:
- Effettuare pulizia e trattamento dei valori mancanti
- Ristrutturare le variabili
- Preparare i dati per l’inserimento in un database relazionale
- Facilitare analisi successive (es. visualizzazione, modellazione)

## 📂 Contenuto del repository

- `extract_transform.py`: Script per il caricamento e la pulizia del dataset originale (CSV), con gestione dei missing values e trasformazioni.
- `load.py`: Script per il caricamento dei dati nel database MySQL.
- `report_retail_store.pdf`: Report finale con raccomandazioni strategiche basate sui dati.
- `db_schema.png`: Diagramma E-R.

## 🧰 Tecnologie utilizzate

- **Linguaggi**: Python
- **Librerie principali**: `pandas`, `pymysql`
- **Database**: MySQL

## 🧪 Funzionalità principali

### 1. Data Cleaning (ET)
- **Rimappatura e rinomina colonne** (es. `Unnamed: 0` → `id_air_pollution`, `tmpd` → `mean_temp`)
- **Conversione timestamp** in formato `datetime` con estrazione di `year` e `month`
- **Eliminazione attributi ridondanti** o con un solo valore (es. `city`)
- **Drop colonne con troppi NaN** (`pm25tmean2`)
- **Riempimento valori mancanti** tramite **mediana mensile** per le variabili quantitative (`mean_temp`, `dew_point`, `pm10_mean`)
- **Conservazione degli outlier** per uso analitico successivo (non vengono rimossi)

### 2. Analisi Preliminare (EDA)
- Statistiche descrittive sulle variabili numeriche
- Analisi dei valori univoci per la rilevazione di feature non informative
- Identificazione degli outlier con metodo IQR su tutte le variabili numeriche

### 3. Data Loading (L)
- **Inserimento automatizzato** dei dati nel database relazionale MySQL (`chicago_db`)
- Utilizzo di `pymysql` per il caricamento batch nella tabella `air_pollution`
- Mapping diretto tra colonne pulite e schema tabellare

## 📊 Risultati Chiave

- **Osservazioni analizzate**: 6.940  
- **Variabili quantitative principali**: temperatura, punto di rugiada, PM10, ozono, NO2  
- **Valori NaN gestiti**: tutti sostituiti con mediane mensili  
- **Outlier individuati**: presenti in meno del 4% dei dati (non rimossi)  
- **Inquinanti principali**: PM10, Ozono e NO2 — coerenti con la metodologia AQI

## 🔒 Licenza

Distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

