import pandas as pd
import matplotlib.pyplot as plt


def prec_ts_to_df(filename):
    from datetime import datetime
    
    dateparse = lambda dates: [datetime.strptime(str(d), '%Y%m%d%H') for d in dates]

    df = pd.read_csv(filename, delimiter=";", encoding="cp1252", 
                     index_col="MESS_DATUM", parse_dates = ["MESS_DATUM"], date_parser = dateparse, 
                     na_values = [-999.0, -999])

    # Column headers: remove leading blanks (strip), replace " " with "_", and convert to lower case.
    
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df.index.name = df.index.name.strip().lower().replace(' ', '_').replace('(', '').replace(')', '')
    # Add time zone: convert from tz naive datetime to tz aware datetime.
    df.index = df.index.tz_localize(tz ='UTC')
    return(df)


def prec_ts_to_df_hist(filename):
    from datetime import datetime
    
    dateparse = lambda dates: [datetime.strptime(str(d), '%Y%m%d') for d in dates]

    df = pd.read_csv(filename, delimiter=";", encoding="cp1252", 
                     index_col="MESS_DATUM_BEGINN", parse_dates = ["MESS_DATUM_BEGINN", "MESS_DATUM_ENDE"], date_parser = dateparse, 
                     na_values = [-999.0, -999])

    # Column headers: remove leading blanks (strip), replace " " with "_", and convert to lower case.
    
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df.index.name = df.index.name.strip().lower().replace(' ', '_').replace('(', '').replace(')', '')
    
    return(df)


def get_hist_month(filename):
    import datetime

    dateparse = lambda dates: [datetime.strptime(str(d), '%Y-%m-%d') for d in dates]

    df = pd.read_csv(filename, delimiter=";", encoding="cp1252", 
                     index_col="mess_datum_beginn", parse_dates = ["mess_datum_beginn", "mess_datum_ende"], date_parser = dateparse, 
                     na_values = [-999.0, -999])


def get_desired_year(df, year, temp_list):

    for date in df.index:
        if date.year == year:
            temp_list.append(df['mo_rr'].loc[date])

    return temp_list

def vol_rr(area, h):

    vol = area * (h / 1000)

    return vol


