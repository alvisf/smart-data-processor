# AWS Credentials
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Celery
BROKER_URL = "sqs://%s:%s@" % (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_DEFAULT_QUEUE = 'demoQueue'
CELERY_RESULT_BACKEND = None # Disabling the results backend
BROKER_TRANSPORT_OPTIONS = {
    'region': 'us-east-1',
    'polling_interval': 20,
}