import logging 
import os
from datetime import datetime
import sys
from exception import CustomException 
LOG_DIR=os.getcwd()
print("current working directory:",LOG_DIR)
LOG_FILE=f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path=os.path.join(LOG_DIR,LOG_FILE)
os.makedirs(LOG_DIR,exist_ok=True)

logs_file_path=os.path.join(LOG_DIR,LOG_FILE)
logging.basicConfig(
    filename=logs_file_path,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO,
)
# if __name__=="__main__":
#     try:
#         a=10/0
#     except Exception as e:
#         logging.info("Division by zero error occurred.")
#         raise CustomException(e,sys)
    


#     logging.info("Logging has been set up.")