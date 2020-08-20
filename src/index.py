from aws_lambda_powertools import Logger


logger = Logger()

@logger.inject_lambda_context
def handler(event, context):
    result = event['result'].lower()
    if result == 'success':
        logger.info(event)
    else:
        logger.error(event)
        raise Exception('Not success')