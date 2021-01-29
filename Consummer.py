# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
import json
import tkinter as TK

# connect to Kafka server and pass the topic we want to consume


class Consummer:
    def __init__(self, textArea, topic='', groupId='', bootstrapServers=''):
        self.consumer = KafkaConsumer(topic, group_id=groupId, bootstrap_servers=bootstrapServers)

        self.flag = False
        self.textArea = textArea
        self.textArea.insert('end', '连接成功，等待接收数据。。。\n')

    def start(self):
        try:
            for msg in self.consumer:
                print("接收到数据")
                if self.flag:
                    break
                print(msg)
                receive_msg = {
                    "topic": msg.topic,
                    "partition": msg.partition,
                    "offset": msg.offset,
                    "timestamp": msg.timestamp,
                    "timestamp_type": msg.timestamp_type,
                    "value": msg.value.decode("utf-8")
                }
                # self.textArea.insert('end', msg.value.decode("utf-8") + '\n')
                self.textArea.insert('end', "接收到的消息:" + json.dumps(receive_msg, ensure_ascii=False) + '\n')
                self.textArea.see(TK.END)
        except Exception as e:
            print(e)

    def close(self):
        self.flag = True
        self.consumer.close()
