#!/usr/bin/env python

import os
import argparse
import time

from google.cloud import pubsub_v1

PROJECT_ID = os.environ.get('PROJECT')

def receive_messages_with_flow_control(project, subscription_name):

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(
        project, subscription_name)

    def callback(message):
        print('Received message: {}'.format(message.data))
        time.sleep(120)
        message.ack()

    flow_control = pubsub_v1.types.FlowControl(max_messages=5)

    subscriber.subscribe(
        subscription_path, callback=callback, flow_control=flow_control)

    print('Listening for messages on {}'.format(subscription_path))
    
    
    time.sleep(300)

receive_messages_with_flow_control(PROJECT_ID, 'cyb-sub')
