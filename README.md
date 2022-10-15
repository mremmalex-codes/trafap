# Trafap 

a simple traffic application with token rewards and social networking 


### ruining the application 

1 install [python](www.python.org)
     download your os version
```shell 
$ pip install pipenv 
```
#### activate a virtual environment using pipenv
```shell
$ pipenv shell
```
#### install the dependencies for the application  
```shell
$ pipenv sync

```
## run database commands 

#### sync your database with the schema 
```shell
$ prisma db push
```
#### generate database client for prisma
```shell
$ prisma generate
```
#### run the application 
```shell
$ uvicorn main:app --reload --port 8080
```