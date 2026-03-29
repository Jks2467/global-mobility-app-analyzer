import os
from pathlib import Path
import logging
from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_dir = "logs"

log_dir_path = os.path.join(from_root(), logs_dir)

os.makedirs(log_dir_path, exist_ok=True)

log_path = os.path.join(log_dir_path, LOG_FILE)


logging.basicConfig(filename=log_path, 
                    level=logging.INFO, 
                    format='[%(asctime)s] - %(levelname)s - %(message)s')

