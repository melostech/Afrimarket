# core/exceptions.py
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    """
    Custom exception handler to standardize API error responses.
    
    Response Format:
    {
        "success": false,
        "message": "Error description",
        "errors": { field: ["error details"] } # Optional, for validation errors
    }
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        custom_response_data = {
            'success': False,
            'message': 'An error occurred.',
            'errors': None
        }

        # Handling specific status codes
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            custom_response_data['message'] = 'Validation Error.'
            custom_response_data['errors'] = response.data
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
            custom_response_data['message'] = 'Authentication Error. Please log in.'
        elif response.status_code == status.HTTP_403_FORBIDDEN:
            custom_response_data['message'] = 'Permission Denied. You do not have access to this resource.'
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            custom_response_data['message'] = 'Resource Not Found.'
        else:
            # Fallback for other errors handled by DRF
            if 'detail' in response.data:
                custom_response_data['message'] = response.data['detail']
            else:
                custom_response_data['message'] = str(response.data)

        response.data = custom_response_data
    else:
        # Handle unexpected exceptions (e.g., 500 Internal Server Error)
        logger.error(f"Unhandled Exception: {exc}", exc_info=True)
        response = Response(
            {
                'success': False,
                'message': 'Internal Server Error. Please try again later.',
                'errors': None
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response
