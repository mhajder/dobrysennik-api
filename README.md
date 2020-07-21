# dobrysennik-api
Unofficial wrapper for [DobrySennik.pl](http://www.dobrysennik.pl/) website that returns data in json format.

## Requirements
* python >=3.6

## Installation
Install using pip:
```shell script
pip install -r requirements.txt
```

## Usage
I use [uvicorn](https://www.uvicorn.org/) to run the application, but you can use any other ASGI server.

Below are some examples of the commands I use.

### Production
```shell script
uvicorn main:app --env-file ".env" --host 127.0.0.1 --port 8000 --workers 2 --no-access-log --proxy-headers
```

### Development
```shell script
uvicorn main:app --reload --env-file ".env"
```