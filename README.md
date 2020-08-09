# Django Search App with Elasticsearch

## Introduction

- This app can perform CRUD operations on a database.
- Uses Elastic search for GET queries.
- Can perform Search and Fliter operations on some fields.

## PreRequisites

* [Python3.6](https://www.python.org/downloads/)
* [JDK](https://www.oracle.com/in/java/technologies/javase-downloads.html)
* [djangorestframework](https://www.django-rest-framework.org/) - pip3 install djangorestframework
* [django-elasticsearch-dsl](https://github.com/django-es/django-elasticsearch-dsl) - pip install django-elasticsearch-dsl
* [ElasticSearch](https://www.elastic.co/downloads/elasticsearch)

### How to run the project
```
$ python manage.py runserver
```
### About the Database

**University**
- alpha_two_code: CharField - 2 digit code
- country: CharField - country name
- domain: CharField - domain
- name: CharField - name of University
- web_page: CharField - url
- created_date: DatetimeField - Date of creation


### APIs

#### 1. GET [search/](http://127.0.0.1:8000/search/)

* READ data using search or filter

#### 2. POST [search/](http://127.0.0.1:8000/search/)

* CREATE object

#### 3. PUT [search/](http://127.0.0.1:8000/search/)

* UPDATE an object using id

#### 4. DELETE [search/](http://127.0.0.1:8000/search/)

> DELETE specific object using id

### Postman Collection for the above APIs

[https://www.getpostman.com/collections/40e5ddc13d38ba1891f4](https://www.getpostman.com/collections/40e5ddc13d38ba1891f4)
