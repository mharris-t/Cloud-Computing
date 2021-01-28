import os
from google.cloud import translate_v2
from google.cloud import pubsub_v1
import json
import base64

# Instantiates a Pub/Sub client
publisher = pubsub_v1.PublisherClient()
PROJECT_ID = 'mthottoli-cloud-project'

def detect_language_pubsub(event, context):

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    if not pubsub_message:
        return 'Missing "message" parameter.'
    
    trans_client = translate_v2.Client()
    langlist = trans_client.detect_language(pubsub_message)
    
    if 'en' in langlist.values():
        topic_name = 'translated-text'
        lang = langlist['language']
        topic_path = publisher.topic_path(PROJECT_ID, topic_name)
        message_json = json.dumps({'text': pubsub_message, 'src_lang': lang })
        message_bytes = message_json.encode('utf-8')


    elif 'en' not in langlist.values():
        topic_name = 'to-translate-text'
        lang = langlist['language']
        topic_path = publisher.topic_path(PROJECT_ID, topic_name)
        message_json = json.dumps({'text': pubsub_message, 'src_lang': lang })
        message_bytes = message_json.encode('utf-8')

    try:
        publish_future = publisher.publish(topic_path, data=message_bytes)
        publish_future.result()  # Verify the publish succeeded
        return 'Message published.'

    except Exception as e:
        print(e)
        return e



