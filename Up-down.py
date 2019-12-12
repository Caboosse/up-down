#!/usr/bin/env python3

from datetime import datetime

#import sys
#import psutil
#import socket
#import subprocess
import boto3  # for cloudwatch publishing and access
from multiping import MultiPing  # for ping process

#set address
#open mp instance
#Send ping to address
#Check each response with receive 
def get_ping(addrs)    
    mp = MultiPing(addrs)
    mp.send()
    responses, no_responses = mp.receive(0.1)


cloudwatch = boto3.client('cloudwatch')
cloudwatch.put_metric_data(
    MetricData=[
        {
            'MetricName': 'Response Time',
            'Dimensions': [
                {
                    'Name': 'Time',
                    'Value': 'MS'
                },
            ],
            'Unit': 'None',
            'Value': 1.0
        },
    ],
    Namespace='ADDRESS/TIME'
)

if __name__ == "__main__":