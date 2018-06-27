import json
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info('got event{}'.format(event))
    logger.error('something went wrong')

    data = {
        'output': 'Hello World - from Cloud9!',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
            
            

