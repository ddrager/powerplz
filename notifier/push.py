from django.conf import settings
import paho.mqtt.publish as publish
import logging

logger = logging.getLogger('debug')

authdata = {'username':settings.MQTT_BROKER_USER, 'password':settings.MQTT_BROKER_PASSWORD}


def publish_push(topic, json_message):
    try:
        publish.single(topic, payload=json_message,
                hostname=settings.MQTT_BROKER_HOST,
                port=settings.MQTT_BROKER_PORT,
                auth=authdata,
                qos=2,
        )
    except ValueError as e:
        logger.debug("Error sending push: %s" % e)