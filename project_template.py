import os
from pathlib import Path # For handling file paths robustly
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'visa'

dir_list = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    "demo.py",
    "config/model.yaml",
    "config/schema.yaml",

]


for item in dir_list:
    path = Path(item)
    
    if path.suffix:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
        logging.info(f"created file path {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f"created directory path {path}")

print("Structure created.")