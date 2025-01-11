import os
from pathlib import Path

# List of files to create
list_of_files = [
    ".github/workflows",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception",
    "tests/unit/__init__.py",
    "tests/integration/__init.py",
    "init_setup.sh",
    "requirments.txt",
    "requirments_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

# Function to create directories and files
for file_path in list_of_files:
    file_path_obj = Path(file_path)
    
    # Create parent directories if they don't exist
    if file_path_obj.suffix:  # Check if it's a file
        file_path_obj.parent.mkdir(parents=True, exist_ok=True)
        # Create an empty file if it doesn't exist
        file_path_obj.touch(exist_ok=True)
    else:
        # If it's a directory, create it
        file_path_obj.mkdir(parents=True, exist_ok=True)

print("File structure created successfully!")
