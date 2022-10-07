## Trafap 

a simple traffic application with token rewards and social networking 


### ruining the application 

1 install python 
    www.python.org
     download your os version
```bash 
$ pip install pipenv 
```
#### activate a virtual environment using pipenv
```bash
$ pipenv shell
```
#### install the dependencies for the application  
```bash
$ pipenv sync

```
#### run the application 
```bash
$ uvicorn main:app --reload --port 8080
```