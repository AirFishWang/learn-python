# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rpc_server
   Description :
   Author :        wangchun
   date：          18-11-15
-------------------------------------------------
   Change Activity:
                   18-11-15:
-------------------------------------------------
"""
import pika
import time

creds = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters(host="10.10.52.51",
                                   port=5672,
                                   virtual_host='/',
                                   credentials=creds,
                                   heartbeat=8)
connection = pika.BlockingConnection(params)

# connection = pika.BlockingConnection(pika.ConnectionParameters('10.10.52.51'))  # also work


channel = connection.channel()

channel.queue_declare(queue='rpc_queue', auto_delete=True)


def f(n):
    return n*n


def on_request(ch, method, props, body):
    n = int(body)

    response = f(n)
    print " [.] f({}) = {}".format(n, response)

    # time.sleep(20)  # time longer heartbeat would miss connection
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                        correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()