# IoT-Project
A simple IoT project for Software Engineering course (SKEL413) on a Agriculture Monitoring System using NodeMCU ESP8266 with Soil Moisture and LDR Sensor Module for data acquisition.
## Table of Contents

- [Stage 2: Overview IoT Agriculture Monitoring System](#stage-2-overview-iot-agriculture-monitoring-system)
  * [Problem Statement](#problem-statement)
  * [Use Case Description](#use-case-description)
  * [System Architecture](#system-architecture)
  * [Sensor](#sensor)
  * [Cloud Platform](#cloud-platform)
  * [Dashboard](#dashboard)
- [Stage 3: RDBMS Design](#stage-3-rdbms-design)
- [Stage 4: Dashboard Design](#stage-4-dashboard-design)

## Stage 2: Overview IoT Agriculture Monitoring System

### Problem Statement

<p style="text-align: justify;">
Food security has been listed in the 17 Sustainable Development Growth (17 SDGs) under 'Zero Hunger'. Agriculture is an important aspect of life as it could source an adequate foodstuff. It contributes to most of the world's food, one of the human's basic need of life. Hence, explains the importance of maintaining the quality of the crops. Cultivation of soil for the growth of crops has become the attention of all farmers. Frequent monitoring is required to ensure plants to grow healthily.

There are a few parameters that need to be monitored in growing a healthy crops which includes soil humidity and light intensity. A soil which is too humid could catalyst the growth of mold and bacteria that cause plants to wilt and become unhealthy whereas plants that does not receive enough lights will also become wilt and eventualy dies.

The intervention of Internet of Things (IoT) technology in agriculture could facilitate farmers in managing their crops by a proper schedule of plant monitoring. They need not to worry about the condition of their crops as the sensor will aid them to monitor the plants. The sensor senses the changes happen to the crops and immediately notify them for any changes occur and they can take action accordingly. This project will focus on the development of IoT-based agriculture monitoring system.
</p>


### Use Case Description

![Use Case Agriculture (3)](https://user-images.githubusercontent.com/117179191/211964029-1f989870-7ccc-443e-8366-bd63ddc81803.jpeg)

| Elements | Description |
| ------- | ---------------|
| System | Farms or nursery |
| Use Case | Report and notify plant condition |
| Actors | Farms or nursery, Farmers |
| Data | Farms or nursery sends summary of collected data from the sensors such as soil humidity and light intensity |
| Stimulus | Farms (Sensor location) establish communication link with the user to send and update requested data |
| Response | The summarized data are sent and displayed to the user for data analysis and user may take action accordingly based on the analyzed data |
| Comments | The plant's conditions need to be monitored every day. |

### System Architecture

This section present an overview of the system architecture of IoT Agriculture Monitoring System. This project use NodeMCU ESP8266 to control, process and transmit moisture and light intensity data received from soil moisture and ldr sensor. NodeMCU will communicate using HTTP data protocol transmission to Flask Web Framework for data ingestion. Then, Flask will store the data to PythonAnywhere Web Hoisting platform and finally update to simple dashboard using Grafana Web Application.

![system architecture](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/architechture-stage2-v5.png)

### Sensor

+ The Nodemcu ESP8266 is a microcontroller board with built-in Wi-Fi capabilities that can be used to collect data from sensors and transmit it wirelessly to a cloud server.
+ The LDR sensor module can be used to monitor the amount of light received by crops in real-time. By placing the sensor in the field, the sensor can detect the amount of light that reaches the crop and transmit the data to the Nodemcu ESP8266 microcontroller board.
+ The HTTPS protocol can be used to provide secure data transfer between the Nodemcu ESP8266 and the cloud server. This ensures that the data collected from the LDR sensor module is securely transmitted over the internet and cannot be intercepted or tampered with by unauthorized parties.


![image](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/hardware-diagram.png "Figure 2: Circuit Diagram for Sensor")

![image](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/nodemcu-pinout.png "Figure 3: Pinout for Nodemcu ESP8266")

### Cloud Platform

This [video](https://youtu.be/_i5_W27mgAI) shows the result of integrated [PythonAnywhere Web Hosting](https://www.pythonanywhere.com/) with the [Flask Web Framework](https://flask.palletsprojects.com/en/2.2.x/) where the web-app link can be found [here](http://mohdafiqazizi.pythonanywhere.com/).


### Dashboard
The prototype dashboard will developed using Grafana Web Application. The dashboard mainly focus on **Graphical-User-Interface (GUI)** approach consist element of:
- icon - small picture represent sub-application
- cursor - as interactive between GUI element
- menu - information or data group together and placed at visible place
 
![Dashboard](https://github.com/SolaireAstora125/IoT-Project/blob/main/asset/dashboard.png)

## Stage 3: RDBMS Design

## Stage 4: Dashboard Design
