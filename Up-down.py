#!/usr/bin/env python3

from datetime import datetime

#import sys
#import psutil
#import socket
#import subprocess
import boto3  # for cloudwatch publishing and access
from multiping import MultiPing  # for ping process

#set address
# open mp instance
# Send ping to address
# Check each response with receive 
ping_EP ={'1.1.1.1': 'Cloudflare','8.8.8.8': 'Google','75.75.75.75': 'Comcast'}

def get_ping(addrs):    
    mp = MultiPing(addrs)
    mp.send()
    responses, no_responses = mp.receive(0.1)




if __name__ == "__main__":
    addrs = ["1.1.1.1","8.8.8.8","75.75.75.75"]
    pings = get_ping(addrs)

    cw_client = boto3.client('cloudwatch', region_name='Oregon')

    date_now = datetime.utcnow()

    metric_data = []

    for ping_address in pings.keys():
        metric_data.append({
            'MetricName': pings_EP[ping_address] + 'Latency',
            'Timestamp': date_now,
            'Value': pings[ping_address],
            'Unit': 'Seconds'
        })
    print(metric_data)
    cw_client.put_metric_data(
        Namespace='IspCheck',
        MetricData=metric_data
    )