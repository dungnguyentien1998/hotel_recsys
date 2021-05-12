from rest_framework import views


def exception_handler(exception, context):
    response = views.exception_handler(exception, context)
    if response is not None:
        # Set status code to exception code
        response.data['status_code'] = response.data.get('detail').code
        # Set success to false
        response.data['success'] = False

    return response
