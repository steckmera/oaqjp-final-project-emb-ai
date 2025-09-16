import requests
import json

def emotion_detector(text_to_analyse):
    # Define la URL para la API de anÃ¡lisis de sentimientos
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Crea la carga util con el texto a analizar
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Establece los encabezados con el ID de modelo requerido para la API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Realiza una solicitud POST a la API con la carga util y los encabezados
    response = requests.post(url, json=myobj, headers=header)
    
    # retorna la respuesta
    return response.text