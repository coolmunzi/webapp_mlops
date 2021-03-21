create env 

```bash
conda create -n wineq python=3.7 -y
```

activate env
```bash
conda activate wineq
```

created a req file

install the req
```bash
pip install -r requirements.txt
```
download the data from 

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

```bash
git init
```
```bash
dvc init 
```
```bash
dvc add data_given/winequality.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```

oneliner updates  for readme

```bash
git add . && git commit -m "update Readme.md"
```
```bash
git remote add origin https://github.com/coolmunzi/webapp_mlops.git
git branch -M main
git push origin main
```
Add/ Update stages:
1. **get_data.py**: Involves data capture from csv files and create dataframe 
2. **load_data.py**: Load the captured data, process it and store the processed data as csv file
3. **split_Data.py**: Splits the total dataset into training and testing chunks
4. **train_and_evaluate.py**: Train the model and evaluate the model performance 

Update stages in dvc.yaml

Add all stages to dvc for tracking
```bash
dvc repro
```

To see the model evaluation metrics from dvc
```bash
dvc metrics show
```

If you change the hyper parameters and later on would like to compare the hyper-parameters os all experiments
```bash
dvc metrics diff
```
tox command -
```bash
tox
```
for rebuilding -
```bash
tox -r 
```
pytest command
```bash
pytest -v
```

setup commands -
```bash
pip install -e . 
```

build your own package commands- 
```bash
python setup.py sdist bdist_wheel
```