# -*- coding: utf-8 -*-
from kafka import KafkaProducer
from kafka.errors import KafkaError


class Producer:
    def __init__(self, bootstrap_servers='', send_message='', topic=''):
        messgae = send_message.encode("utf-8")
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        self.producer.send(topic, messgae)
        self.producer.close()


if __name__ == '__main__':
    messgae = "{'alarmArea': 0, 'alarmAreaId': 87, 'alarmData': '浙A17885', 'alarmLevel': 1, 'alarmType': 'etc_plate', 'comprehensiveCircleId': 40, 'createTime': 1610678684382, 'devId': '701200605021', 'devName': '17065-弘德路西溪银座西大门口南向北', 'facePic': '', 'firstAlarmTime': 1610696732000, 'id': 25332, 'latestAlarmLevel': 1, 'monitorId': 7885, 'personId': 2054, 'personName': '轩辕罗悌'}"
    producer = Producer('10.4.2.66:9092,10.4.2.64:9092,10.4.2.65:9092', messgae, 'test_20181105')
