import requests
import json

def emotion_detector(text_to_analyze):

    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Define the payload with nonsensical text to test the API
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = input_json, headers=headers)

    return response.text