# -*- coding:utf-8 -*-

import firestoreManage
import pandas as pd

incidentsData = firestoreManage.read('incidents')
incidentsData = firestoreManage.createDataFrame(incidentsData)

#Variables
idNumber = incidentsData['idNumber']
### ---------------------------------------------------------------------------------------------------------------------
def idNumberAssignation(idNumber):
    
    if idNumber[0] != None and idNumber[0] == 0:
        valor_inicial = idNumber[0]
    else:
        valor_inicial = 0
    
    #Función anidada "contador", simplemente hace +1 a la instancia anterior
    def contador(valor_inicial):
        
        """
        Función que incrementa un valor en 1 cada vez que se llama.

        Args:
            valor_inicial: El valor inicial del contador. Por defecto es 0.

        Returns:
            El valor incrementado.
        """
    contador.valor_actual = getattr(contador, 'valor_actual', valor_inicial)
    contador.valor_actual += 1
    return contador.valor_actual

    #Ciclo "for" que va a aplicar el tema a todos los campos
    ##Esta debo terminarla pero NO es tan importante



### ---------------------------------------------------------------------------------------------------------------------