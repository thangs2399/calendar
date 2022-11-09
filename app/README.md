# Installation Guide

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




## Using Docker

#### build
> sudo docker build -t capp:latest .
#### run
> sudo docker run -p 5000:5000 capp:latest


---