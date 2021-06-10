# Temperature Monitoring
## Introduction
The purpose of this project was to develop a temperature sensor network. This type of network can be used for several different applications ranging from smart home automation to monitoring the health of industrial machinery. 

## Materials
### Software
- HiveMQ
- Grafana
- InflxuDB
- Raspbian
- ArduinoIDE

### Hardware
- GoRobo.io board
- Arduino MKR 1000
- Raspberry Pi 3
- DHT11 Temperature & Humidty sensor

## Description
The network comprised of several nodes which collected temperature readings that sent temperature readings to a central node via MQTT. This cental node then processed the data and forwarded it to a cloud hosted database (influxDB). The data is then visualized on a Grafana dashboard. 

![alt text](https://github.com/kchong98/temperature_monitoring/blob/main/Images/Flow.png)
