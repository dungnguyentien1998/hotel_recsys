from rest_framework import views
from rest_framework.response import Response


def exception_handler(exception, context):
    response = views.exception_handler(exception, context)
    if response is not None:
        # Set status code to exception code
        response.data['status_code'] = response.data.get('detail').code
        # Set success to false
        response.data['success'] = False
    else:
        temp = {'status_code': '500', 'success': False}
        response = Response(data=temp)
        # response.data['status_code'] = '500'
        # response.data['success'] = False

    return response
