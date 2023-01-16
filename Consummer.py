# -*- coding: utf-8 -*-
import os
import sqlite3
import sys

from kafka import KafkaConsumer
import json
import tkinter as TK


# connect to Kafka server and pass the topic we want to consume


class Consummer:
    def __init__(self, textArea, topic='', groupId='', bootstrapServers='',check_btn_var='F'):
        self.bootstrapServers = bootstrapServers
        self.consumer = KafkaConsumer(topic, group_id=groupId, bootstrap_servers=bootstrapServers)

        self.flag = False
        self.textArea = textArea
        self.textArea.insert('end', '连接成功，等待接收数据。。。\n')
        self.check_btn_var = check_btn_var

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
                if self.check_btn_var is not None and self.check_btn_var == 'T':
                    sql = "INSERT OR IGNORE into history_msg('col_key','topic','partition','offset','timestamp_str','timestamp_type','value') " \
                          "values ('%s','%s','%s','%s','%s','%s','%s')" % (self.bootstrapServers,
                                                                           receive_msg['topic'],
                                                                       receive_msg['partition'],
                                                                       receive_msg['offset'],
                                                                       receive_msg['timestamp_str'],
                                                                       receive_msg['timestamp_type'],
                                                                       receive_msg['value'])
                    # print(sql)
                    conn = sqlite3.connect(os.path.join(os.path.dirname(sys.argv[0]), "kafka_info.db"))
                    c = conn.cursor()
                    c.execute(sql)
                    conn.commit()
                    c.close()
                    conn.close()
        except Exception as e:
            print(e)

    def close(self):
        self.flag = True
        self.consumer.close()

if __name__ == '__main__':
    sql = "INSERT OR IGNORE into history_msg('col_key','topic','partition','offset','timestamp_str','timestamp_type','value') " \
          "values ('%s','%s','%s','%s','%s','%s','%s')" % ('10.4.2.66:9092',
                                                           'test',
                                                           '0',
                                                           '10',
                                                           '2019-12-12 12:12:12',
                                                           '0',
                                                           'sjhdjashkdjsahjkdhjaskhdkjashj')
    # print(sql)
    conn = sqlite3.connect(os.path.join(os.path.dirname(sys.argv[0]), "kafka_info.db"))
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()