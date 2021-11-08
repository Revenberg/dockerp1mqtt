"""Exporter configuration."""
import os

PREFIX = os.getenv("PROMETHEUS_PREFIX", "mqtt_")
TOPIC_LABEL = os.getenv("TOPIC_LABEL", "topic")
TOPIC = os.getenv("MQTT_TOPIC", "#")
IGNORED_TOPICS = os.getenv("MQTT_IGNORED_TOPICS", "").split(",")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
MQTT_ADDRESS = os.getenv("MQTT_ADDRESS", "127.0.0.1")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_KEEPALIVE = int(os.getenv("MQTT_KEEPALIVE", "60"))
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", "9000"))


do_raw_log = os.getenv("LOGGING", "no")

device = os.getenv("P1_DEVICE", "/dev/ttyUSB0")
baudrate = int("P1_BAUDRATE", os.getenv("115200"))

mqttBroker = os.getenv("MQTT_ADDRESS", "192.168.2.59")
mqttPort = int(os.getenv("MQTT_PORT", "1883"))
mqttTopic = os.getenv("MQTT_TOPIC", "p1")
