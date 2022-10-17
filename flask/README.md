# Installation Guide

### Using Python Virutal Environment

#### MacOS/Linux
> python3 -m venv venv   # create virtual environment
> . venv/bin/activate    # activate virtual environment
> pip install -e .       # install requirements/dependencies

#### Windows
> py -3 -m venv venv        # create virtual environment
> venv\Scripts\activate     # activate virtual environment
> pip install -e .          # install requirements/dependencies



### Using Docker

#### build
> sudo docker build -t capp:latest .
#### run
> sudo docker run -p 5000:5000 capp:latest