snapsnare-api
=

snapsnare-api, this project, a rest server to communicate to snapsnare

Table of contents:

* Remarks
* Getting started
  * general installation
  * development installation

# Remarks
snapsnare-api currently supports Python 3.5 and higher.

# Getting started
snapsnare-api consists of 2 parts, a flask rest web application and a postgresql database.
When you want to use snapsnare-api it is recommended that you follow the instructions described in the general installation section.


## General installation
snapsnare-api depends on the snapsnare database. 
Before you start the installation of snapsnare it is recommended you execute these [installation instructions](https://github.com/janripke/snapsnare-db/blob/main/README.md) first.

### configure snapsnare-api
For safety reasons the snapsnare database credentials are stored on your local machine. 
To be more exact under ~/.snapsnare/snapsnare-ds.json

create the snapsnare-ds.json in ~/.snapsnare folder: paste the following into this file:
```python
{
  "type": "postgresql",
  "host": "localhost",
  "db": "snapsnare",
  "username": "snapsnare_owner",
  "password": "snapsnare_owner"
}
```

### install snapsnare-api
```shell
pip3 install git+https://github.com/janripke/snapsnare-api.git@0.0.2#egg=snapsnare_api
```

### run snapsnare-api
```shell
$ snapsnare-api
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
2021-01-11 00:07:40,788 werkzeug INFO _internal _log:113 -  * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
```


## Development installation
snapsnare-api depends on the snapsnare database. 
Before you start the installation of snapsnare it is recommended you execute these [installation instructions](https://github.com/janripke/snapsnare-db/blob/main/README.md) first.

### configure snapsnare-api
For safety reasons the snapsnare database credentials are stored on your local machine. 
To be more exact under ~/.snapsnare/snapsnare-ds.json

create the snapsnare-ds.json in ~/.snapsnare folder: paste the following into this file:
```python
{
  "type": "postgresql",
  "host": "localhost",
  "db": "snapsnare",
  "username": "snapsnare_owner",
  "password": "snapsnare_owner"
}
```

### clone snapsnare-api
```
git clone https://github.com/janripke/snapsnare-api.git
```

### run snapsnare-api
```shell
python3 snapsnare_api/app.py
```



