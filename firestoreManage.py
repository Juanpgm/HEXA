# -*- coding:utf-8 -*-

import json
import pandas as pd

#Firebase-Firestore libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("hexa-firestore-secret.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


#Write function
### ---------------------------------------------------------------------------------------------------------------------
## Tengo que revisar muy bien esta función
def write(collectionName, dataToWrite):
    doc_ref = db.collection(collectionName).document()
    return doc_ref.set(dataToWrite)
### ---------------------------------------------------------------------------------------------------------------------


### ---------------------------------------------------------------------------------------------------------------------
#Read functions:
def read(collectionName):
    
  """
  Reads documents from the specified collection in Firestore and returns a list of dictionaries.

  Args:
      collectionName (str): The name of the collection to read from.

  Returns:
      list: A list of dictionaries containing the document data.
  """
  documents = []
  try:
    # Get a snapshot of the documents in the collection
    docs = db.collection(collectionName).get()

    # Extract data from each document and append it to the list
    for doc in docs:
      documents.append(doc.to_dict())

  except Exception as e:
    print(f"Error reading collection '{collectionName}': {e}")

  return documents
### ---------------------------------------------------------------------------------------------------------------------

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
