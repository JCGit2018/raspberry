import http.client
import urllib.request
import urllib.parse
import json
import time
import datetime
from random import random


#Datos para conexion con CARRIOTS
api_url = "http://api.carriots.com/streams"
device = 'defaultDevice@JCarriot.JCarriot'
api_key="27817cfff89c3e1e49c4a130e22a983bf56692ff0229527b88d450af1ed09133"
#api_key="11a793435d0a8b061e829ddb3b23edda3facce13c57ded5dfcf8d23999530461"
#api_key="2447585f28859ba6ce342682d1d25d686322df6d41849c26787950da6e850aef"


#Lazo para envio de datos
    
while True:
    #Tiempo en el que se envia el mensaje
    timestamp =int(time.time())

    currentDate = datetime.datetime.today()
    currentTime = datetime.datetime.now()
    print('Tiempo de envío: ' +currentDate.strftime('%d %b,%Y')+' '+datetime.datetime.strftime(currentTime,'%H:%M'))

    #Parametros cuerpo del mensaje
    #Se generan valores aleatorios para simulación

    temperatura=random()*80+1
    humedad=random()*99+1
    presion=random()*99+1

    #redondeamos a dos decimales
    temperatura=round(temperatura,2)
    humedad=round(humedad,2)
    presion=round(presion,2)

    temperaturaf=format(temperatura)+'ºC'
    humedadf=format(humedad)+'%'
    presionf=format(presion)+'kpa'

    #Se muestran Valores a enviar
    print('Valores: Temperatura: '+ temperaturaf+' Humedad: ' + humedadf + ' Presión: '+ presionf )

    #Parametros de conexion para el post en Carriots
    params = {"protocol": "v2",
              "device": device,
              "at": timestamp,
              "data": dict(
                   temp=temperatura,
                   hum=humedad,
                   pressure=presion)}


    binary_data = json.dumps(params).encode('ascii')

    #Encabezado
    header ={"User-agent": "JC_Vzlaraspberrycarriots",
         "Content-Type": "application/json",
         "carriots-apikey": api_key}		 


    #Petición
    req = urllib.request.Request(api_url,binary_data,header)
    f = urllib.request.urlopen(req)

    #Mostrar Respuesta del host
    print(f.read().decode('utf-8'))

    #Se espera 1 min antes de volver a enviar
    time.sleep(60)
