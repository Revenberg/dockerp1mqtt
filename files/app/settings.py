"""Exporter configuration."""
import os

do_raw_log = bool(os.getenv("LOGGING", "false"))

device = os.getenv("P1_DEVICE", "/dev/ttyUSB0")
baudrate = int(os.getenv("P1_BAUDRATE", "115200"))

mqttBroker = os.getenv("MQTT_ADDRESS", "192.168.2.59")
mqttPort = int(os.getenv("MQTT_PORT", "1883"))
mqttTopic = os.getenv("MQTT_TOPIC", "p1")
