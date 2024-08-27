# -*- coding:utf-8 -*-

import json
import pandas as pd

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