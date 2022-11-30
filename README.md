# Installation Guide for CAPP


## Using Python Virutal Environment

#### MacOS/Linux
```python
 python3 -m venv venv                           # create virtual environment
 . venv/bin/activate                            # activate virtual environment
 pip install --upgrade pip                      # upgrade pip
 pip install -r requirements.txt                # install requirements/dependencies
 flask --app capp --debug run --host=0.0.0.0    # run the app
```


#### Windows
```python
 py -3 -m venv venv                             # create virtual environment
 venv\Scripts\activate                          # activate virtual environment
 pip install --upgrade pip                      # upgrade pip
 pip install -r requirements.txt                # install requirements/dependencies
 flask --app capp --debug run --host=0.0.0.0    # run the app
```


## Setting and Getting Environment Variables

#### MacOS/Linux
```
# Setting an Environment Variable
export API_KEY = '123abc'

# Getting an Enviroment Variable
os.getenv('API_KEY')
```


#### Windows
```
# Setting an Environment Variable
set API_KEY = '123abc'

# Getting an Enviroment Variable
os.getenv('API_KEY')
```


## Using Docker
```
########## docker compose ##########

# build
sudo docker-compose build

# run
sudo docker-compose up

# stop
sudo docker-compose down
```

---
