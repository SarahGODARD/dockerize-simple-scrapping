# A simple scrapping

This is the technical test for Pandascore application.

## requirements

You will need python3 lastest version to run this app. 
Make sure you entered the right informations for email and password in .env file. Do not modify PANDASCORE_URL.

## Run on your own environement. 

```bash
pip install -r requirement.txt
```
```bash
python script.py
```

## Run with Docker.

```bash
docker build .
```
```bash
docker compose up
```
In an other terminal :

```bash
docker exec -it pandascore_tt-app-1 /bin/sh
```
Inside this process :

```bash
python script.py
```

You can also use the docker desktop app.

# Developer

GODARD Sarah
