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
addrs = ["1.1.1.1","8.8.8.8","75.75.75.75"]
def get_ping(x):    
    mp = MultiPing(x)
    mp.send()
    responses, no_responses = mp.receive(1)
    return responses, no_responses




if __name__ == "__main__":
    
    cw_client = boto3.client('cloudwatch', region_name='Oregon')
    date_now = datetime.utcnow()
    metric_data = []

    pings = get_ping(addrs)
    
    print(pings)
    """
    for ping in ping_EP.keys:
        metric_data.append({
            'MetricName': ping_EP[ping_address] + ' Latency',
            'Timestamp': date_now,
            'Value': ping[],
            'Unit': 'Seconds'
        })
    
    print(metric_data)
    """
    """
    cw_client.put_metric_data(
        Namespace='IspCheck',
        MetricData=metric_data
    """
