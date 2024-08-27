# -*- coding:utf-8 -*-
### ---------------------------------------------------------------------------------------------------------------------
'''
IMPORTACIONES
'''
### ---------------------------------------------------------------------------------------------------------------------
import json
import pandas as pd
import firestoreManage
from datetime import datetime
import re

### ---------------------------------------------------------------------------------------------------------------------
'''
CREACIÓN DE FUNCIONES
'''
### ---------------------------------------------------------------------------------------------------------------------
#dataFrame creation function:
def createDataFrame(read): ##Recibe datos como lo es el documento .json encapsulado en una lista lml
    # Convert JSON dataList to Pandas DataFrame
    df = pd.DataFrame(read)

    # Return DataFrame
    return df #llamar como una función cualquiera y usar la sintaxis para DataFrames para representar lo que sea mi brother
### ---------------------------------------------------------------------------------------------------------------------

### ---------------------------------------------------------------------------------------------------------------------
#JSON creation function:
def createJSONFile(dataframe):
    '''
    #Le entra un DataFrame de pandas, la idea es que este cosito ya deje la vuelta lista para generar las transformaciones
    '''
    jsonFile = dataframe.to_json(orient='table')
    return jsonFile #Bota un String
### ---------------------------------------------------------------------------------------------------------------------

### ---------------------------------------------------------------------------------------------------------------------

def convert_datetime_string(datetime_string):
    """
    Converts a datetime string in the format "YYYY-MM-DD HH:MM:SS.ffffff+00:00" to the format "dd/mm/yyyy - HH:MM:ss".

    Args:
        datetime_string: The datetime string to convert.

    Returns:
        The converted datetime string in the format "dd/mm/yyyy - HH:MM:ss".
    """

    # Parse the datetime string into a datetime object
    dt = datetime.datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S.%f%z")

    # Format the datetime object to the desired format
    formatted_datetime = dt.strftime("%d/%m/%Y - %H:%M:%S")

    return formatted_datetime

### ---------------------------------------------------------------------------------------------------------------------

### ---------------------------------------------------------------------------------------------------------------------
def format_datetime(dt):
    """
    Formatea un objeto datetime a 'dd/mm/yyyy - HH:MM:ss'.

    Args:
        dt: Un objeto datetime.

    Returns:
        Una cadena con la fecha y hora formateada.
    """
    
    match = re.match(r"DatetimeWithNanoseconds\((\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), tzinfo=datetime\.timezone\.utc\)", dt)

    if match:
        # Extract the numeric values from the match groups
        year, month, day, hour, minute, second, microsecond = match.groups()
        return int(year), int(month), int(day), int(hour), int(minute), int(second), int(microsecond)
    else:
        raise ValueError("Invalid datetime string format")

    # Formatea la fecha y hora utilizando f-strings
    formatted_datetime = f"{dt.day:02d}/{dt.month:02d}/{dt.year} - {dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}"
    return formatted_datetime
### ---------------------------------------------------------------------------------------------------------------------

### ---------------------------------------------------------------------------------------------------------------------
'''
CÓDIGO {PROCESOS}
'''
### ---------------------------------------------------------------------------------------------------------------------
#Lectura de datos firebase:

firebaseIncidentData = firestoreManage.read('incidents')


### ---------------------------------------------------------------------------------------------------------------------
#Modificación de las fechas:
for x in firebaseIncidentData:
    #mod = convert_datetime_string(str(x['horaLlamada']))
    #print(mod)
    print(x['horaLlamada'])
    
    
    ######### DEBO INTENTAR QUE ESTO FUNCIONE MEJOR