import os

# Define the folder structure
folder_structure = {
    ".github/workflows": ["ci.yml", "mlops-pipeline.yml"],
    "data/raw": [],
    "data/processed": [],
    "data/interim": [],
    "notebooks": [
        "01_EDA.ipynb",
        "02_Feature_Engineering.ipynb",
        "03_Modelling.ipynb",
        "04_Serving_API.ipynb",
        "05_Final_Report.ipynb",
    ],
    "src": [
        "__init__.py",
        "data_processing.py",
        "feature_engineering.py",
        "model_training.py",
        "api.py",
        "utils.py",
        "config.yaml",
    ],
    "tests": [
        "test_data_processing.py",
        "test_feature_engineering.py",
        "test_model_training.py",
        "test_api.py",
    ],
    "environments": ["requirements.txt", "environment.yml"],
}

# Create folders and files
for folder, files in folder_structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        open(os.path.join(folder, file), 'w').close()

# Create top-level files
top_level_files = [".gitignore", "README.md", "LICENSE", "setup.py"]
for file in top_level_files:
    open(file, 'w').close()

print("Folder structure created successfully!")
