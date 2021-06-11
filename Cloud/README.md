# Cloud Code
## Description
The following code receives temperature data from the edge nodes and uploads it to an InfluxDB database. Additionally, if the central node receives a temperature reading above a set threshold, it sends an alarm via MQTT back to the sender to trigger a response. 

## Required Libraries
- Paho-MQTT
- InfluxDB-Client
- ast
- time
- json
