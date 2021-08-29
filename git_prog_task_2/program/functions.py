import pandas as pd
import datetime as dt


def df_norm(filename):
    dateparse = lambda dates: [dt.datetime.strptime(str(date), '%Y%m%d') for date in dates]

    df = pd.read_csv(filename, delimiter=";", encoding="cp1252", 
                     index_col="MESS_DATUM_BEGINN", 
                     parse_dates = ["MESS_DATUM_BEGINN", "MESS_DATUM_ENDE"], 
                     date_parser = dateparse, 
                     na_values = [-999.0, -999])
    
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df.index.name = df.index.name.strip().lower().replace(' ', '_').replace('(', '').replace(')', '')
    df.index = df.index.tz_localize(tz ='UTC')
    
    return(df)
