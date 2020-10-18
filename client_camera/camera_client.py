import requests
import random
import json
import time

# Sleep time between updates
PRELOAD_COUNT = 4
SLEEP_TIME_s = 10
CAMERA_ID = 'camera_1'
CAMERA_NAME = 'Conference Room'

responses = [
    'Person detected',
    'Cat chasing mouse detected',
    'Local memory almost full',
    'Sweet party detected',
    'Loud noise detected',
    'Unauthorized personnel detected',
    'Authorized entry detected',
    'Bob Ross detected',
    'The cake is a lie'
]
detectionQueue = []


######################
# Internal Functions #
######################

def randomResponse():
    return {'timestamp': round(time.time()), 'message':responses[random.randint(0, len(responses)-1)]}

def makeLogPost():
    return json.dumps({
        'id':CAMERA_ID,
        'data': {
            'metadata': {
                'updated_at': time.time(),
                'name': CAMERA_NAME,
                'update_pending': False
            },
            'logs': detectionQueue
        }
    })

# Preload some detection items
for i in range(PRELOAD_COUNT):
    detectionQueue.append(randomResponse())


#############
# Main Loop #
#############

while(True):

    print('Checking for jobs...')

    # Add a random message
    detectionQueue.append(randomResponse())

    # Check in with the server for jobs
    try:
        getRequest = requests.get('http://localhost:3000/jobs', params={'id':CAMERA_ID})

        # Make sure we get a proper response
        if (200 == getRequest.status_code):
            response = getRequest.json()
            if ('jobs' in response):
                if response['jobs'] == 'send_logs':
                    print('Logs request received, responding...')
                    postRequest = requests.post('http://localhost:3000/', data=makeLogPost())
                    if 200 == postRequest.status_code:
                        print('Logs upload successful!')
                    else:
                        print('Logs upload error!')
                else:
                    print('No pending tasks')
        else:
            print('Server connection error...')

        print('All jobs complete!\n')

    except:
        print("Connection Error!\n")

    time.sleep(SLEEP_TIME_s)












