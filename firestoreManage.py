# -*- coding:utf-8 -*-

import json
import pandas as pd

#Firebase-Firestore libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("hexa-firestore-secret.json")
firebase_admin.initialize_app(cred, {
  'databaseURL': ''
})

db = firestore.client()


### ---------------------------------------------------------------------------------------------------------------------
#List users function:
def listUsers():
  users = read('users')
  for user in users:
    print(user.get('display_name'))
  
### ---------------------------------------------------------------------------------------------------------------------

#List collections function
### ---------------------------------------------------------------------------------------------------------------------
def listCollections():
  collections = db.collections()
  
  for collection in collections:
    print(collection.id)
  
### ---------------------------------------------------------------------------------------------------------------------

#Write function
### ---------------------------------------------------------------------------------------------------------------------
## Tengo que revisar muy bien esta función --- XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def write(collectionName, dataToWrite):
  doc_ref = db.collection(collectionName).document()
  return doc_ref.set(dataToWrite)
### ---------------------------------------------------------------------------------------------------------------------


### ---------------------------------------------------------------------------------------------------------------------
#Read function:
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
#get times function:
def get_times(incidents):
    """
    Imprime los tiempos de un incidente a partir de un diccionario.

    Args:
        incidents: Una lista de diccionarios, donde cada diccionario representa un incidente.

    Returns:
        None
    """

    for incident in incidents:
        # Obtener los tiempos utilizando una lista de claves
        times = {"Hora de llamada": incident.get('horaLlamada'), 
                 "Hora de respuesta": incident.get('horaRespuesta'), 
                 "Hora de despacho HEXA":incident.get('horaDespachoHEXA'), 
                 "Hora de despacho institución": incident.get('horaDespachoInstitucion'), 
                 "Hora de llegada": incident.get('horaLlegada'), 
                 "Hora de cierre": incident.get('horaCierre')}
       
        return times
### ---------------------------------------------------------------------------------------------------------------------
