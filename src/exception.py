import sys
import logging
def error_message(error_detail: sys) -> str:
    """Generate a formatted error message with file name and line number.

    Args:
        error_detail (sys): The sys module to extract exception information.

    Returns:
        str: A formatted error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {str(error_detail)}"
    return error_message
class CustomException(Exception):
    """Custom exception class that includes detailed error information.

    Args:
        error_detail (sys): The sys module to extract exception information.
        message (str, optional): Additional message to include. Defaults to None.
    """
    def __init__(self, error_detail: sys, message: str = None):
        super().__init__(message)
        self.error_detail = error_detail
        self.message = error_message(error_detail)

    def __str__(self) -> str:
        return self.message
    
# if __name__ == "__main__":
#         try:
#             a = 1/0
#         except Exception as e:
#             logging.info("Division by zero log occured")
#             instance = CustomException(e, sys)
#             raise instance
