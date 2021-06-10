# Arduino Code
## Description
The following code shows how to connect to a MQTT broker with an Arduino to record and send temperature data. The second file simulates the microcontroller's response when receiving an alert. If an alert is received (in this case, a button is pushed), a fan is turned on (controlled with a DC motor). Unfortunately, we ran into issues connecting to the HiveMQ client due to TLS security protocols and an unstable internet connection.

## Required Libraries
- Arduino MQTT Client
- WiFi
- Cooperative Multitasking
- Si7020
- Wire
- MCP23017
