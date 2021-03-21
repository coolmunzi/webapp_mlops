import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "data_given",
    "notebooks",
    "saved_models",
    "src",
    "report",
    "tests"
]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)
    #Create .gitkeep file for commiting empty folder to git
    with open(os.path.join(dir, ".gitkeep"), "w") as f:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file in files:
    with open(file, "w") as f:
        pass
