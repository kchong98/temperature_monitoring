# Temperature Monitoring

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

## Introduction
The purpose of this project was to develop a temperature sensor network. The network comprised of several nodes which collected temperature readings that sent temperature readings to a central node via MQTT. This cental node then processed the data and forwarded it to a cloud hosted database (influxDB). The data is then visualized on a Grafana dashboard. 
