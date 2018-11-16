# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rpc_client
   Description :
   Author :        wangchun
   date：          18-11-15
-------------------------------------------------
   Change Activity:
                   18-11-15:
-------------------------------------------------
"""
import pika
import uuid
import time

class RpcClient:
    def __init__(self):
        creds = pika.PlainCredentials('guest', 'guest')
        params = pika.ConnectionParameters(host="10.10.52.51",
                                           port=5672,
                                           virtual_host='/',
                                           credentials=creds)
        self.connection = pika.BlockingConnection(params)

        # self.connection = pika.BlockingConnection(pika.ConnectionParameters('10.10.52.51')) # also work
        self.channel = self.connection.channel()

        # result = self.channel.queue_declare(exclusive=True)
        # self.callback_queue = result.method.queue

        self.callback_queue = "rpc_queue_response_" + str(uuid.uuid4())   # each client have exclusive response queue
        self.channel.queue_declare(exclusive=True, queue=self.callback_queue)
        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):

        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()

        return int(self.response)


if __name__ == "__main__":
    client = RpcClient()

    for i in range(100):
        response = client.call(i)
        print "client.call({}) = {}".format(i, response)
        #time.sleep(1)