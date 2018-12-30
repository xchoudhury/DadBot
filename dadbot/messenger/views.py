from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def validate_request(request):
    return True
    dadbot_token = "not secure"
    # dadbot_token = os.environ['dadbot_token']

    if 'hub.mode' not in request.query_params \
    or 'hub.verify_token' not in request.query_params \
    or 'hub.challenge' not in request.query_params:
        return False

    mode = request.query_params['hub.mode']
    token = request.query_params['hub.verify_token']

    if mode == 'subscribe' and token == dadbot_token:
        return True
        # return Response(request.query_params['hub.challenge'], status=status.HTTP_200_OK)
    
    return False

@api_view(['GET', 'POST'])
def message(request):
    if not validate_request(request):
        error = {
            "error" : "some error info"
        }
        return Response(error, status=status.HTTP_403_FORBIDDEN)
    
    # Might have to do this in a new thread
    body = request.data
    if body['object'] == 'page':
        for entry in body['entry']:
            event = entry['messaging'][0]
            print(event)

    return Response(status=status.HTTP_200_OK)