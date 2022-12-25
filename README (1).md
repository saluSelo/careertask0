
# CAREER ACCElerator - BACKEND TASK 0

making a dB table using models with two end-points

/GET -> show all posts that save within posts table.

/POST -> to  add new post to posts table.

## API Reference

#### Get all items

```http
  baseapp/GET
```

| id     | title     | text                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` |  `string` |




## Authors

- [@saluselo](https://github.com/saluSelo)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![Django License](https://img.shields.io/badge/Django-4.1.4-brightgreen)](https://www.djangoproject.com/)
[![python License](https://img.shields.io/badge/python-3.11.1-green)](https://www.python.org/)
[![sqllite License](https://img.shields.io/badge/sqllite-3.39.4%20-9cf)](https://www.sqlite.org/index.html)


## INSTALLATION

### Prerequisites
- Git
- Python 3.x
- pip (Python package manager)
- virtualenv (Python virtual environment tool)

### Setting up the project

Clone the project

```bash
  git clone https://github.com/saluSelo/careertask0
```

Go to the project directory

```bash
  cd careertask00
```

create virtual env 
```bash
  virtualenv env  

```
activate env for (Windows)
```bash
.\env\Scripts\activate

```

activate env for (Linux/Mac)
```bash
./env/bin/activate 

```


Install the dependencies

```bash
 pip install -r requirments.txt
```



### Running the server

1. Run the following command to start the server:

```bash
 python manage.py runserver
```

2. The server should now be running at 
http://127.0.0.1:8000/


### Maintenance
- To stop the server, press CTRL+C in the terminal window where the server is running.
- To deactivate the virtual environment, run :

(Windows)
```bash
.\env\Scripts\deactivate
```

(Mac/Linux)
```bash
./env/bin/deactivate 
```
