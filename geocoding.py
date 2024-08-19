# -*- coding:utf-8 -*-

import googlemaps
from datetime import datetime
#Función que hace geoCoding desde la API de Google MAPS
## Me falta también completar esta hpta por el tema del "Billing Account"

### ---------------------------------------------------------------------------------------------------------------------
def getGeoCoding(address):
  gmaps = googlemaps.Client(key='AIzaSyAmr13Iu3I3vQ5wvbb5dpmxgwLxZ0mjiVA') #Esta API_KEY, luego toca ocultarla, OJO
  geocode_result = gmaps.geocode(address)
  return geocode_result


geocode_result = getGeoCoding('Cra 35 # 15-33, Institución educativa Joaquín De Cayzedo Y Cuero, Sede Joaquín De Cayzedo Y Cuero, Comuna 10, Cali, Valle del Cauca, Colombia')
geocode_result
### ---------------------------------------------------------------------------------------------------------------------