import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "data_given",
    "notebooks",
    "saved_models",
    "src",
    "report",
    "tests",
    os.path.join("prediction_service", "model"),
    os.path.join("webapp", "static", "css"),
    os.path.join("webapp", "static", "script"),
    os.path.join("webapp", "templates")

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
    "app.py",
    os.path.join("src","__init__.py"),
    os.path.join("prediction_service", "prediction.py"),
    os.path.join("webapp", "static", "css", "main.css"),
    os.path.join("webapp", "static", "css", "index.js"),
    os.path.join("webapp", "templates","index.html"),
    os.path.join("webapp", "templates","404.html"),
    os.path.join("webapp", "templates","base.html"),
    os.path.join(".github", "workflows","ci-cd.yaml")

]

for file in files:
    with open(file, "w") as f:
        pass
