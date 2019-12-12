from multiping import MultiPing
#import sys
#import psutil
#import socket
#import subprocess
import boto3
from datetime import datetime

addrs = ["1.1.1.1","8.8.8.8","75.75.75.75"]
mp = MultiPing(addrs)
mp.send()
responses, no_responses = mp.receive(0.1)
for addr, rtt in responses.items():
    print("%s responded in %f seconds" % (addr, rtt))
if no_responses:
    print("These addresses did not respond %s" % ", ".join(no_responses))

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