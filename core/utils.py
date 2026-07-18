# core/utils.py
from rest_framework.response import Response
from rest_framework import status

def api_success_response(data=None, message="Success", status_code=status.HTTP_200_OK):
    """
    Standardize the success API response format.
    
    Response Format:
    {
        "success": true,
        "message": "Success message",
        "data": { ... }
    }
    """
    response_data = {
        "success": True,
        "message": message,
        "data": data
    }
    return Response(response_data, status=status_code)
