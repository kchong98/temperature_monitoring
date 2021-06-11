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

## Procedure
### Step 1: Setting up communication
To begin, we set up the HiveMQ broker. For our purposes, we decided to use [HiveMQ cloud](https://www.hivemq.com/mqtt-cloud-broker/) which is a free service that allows for up to 100 devices to communicate with the broker. For examples of publishing or subscribing to branches from our broker please refer to the Arduino and Pi folders.

Next, we set up our [InfluxDB](https://www.influxdata.com/products/influxdb-cloud/) database. It is an easy to use platform that allows for cloud hosting on AWS, Azure, or GCS. All of our data was stored in a 'bucket' which can be modified or accused using Flux or SQL-like queries. 

Finally, we set up a dashboard with [Grafana](https://grafana.com/products/cloud/) Cloud. We chose this service because it is a highly customizable, open-source platform that allows us to actively visualize our data in real-time which is very helpful for IoT solutions such as ours. Another helpful feature Grafana offers is compatiblity with many other services including InfluxDB, PostgreSQL, MySQL, MariaDB, and many more. Our dashboard was 

For all of these services, there is also the option to host them on your own machine which we chose not to do because our team did not have stable internet connections. 
