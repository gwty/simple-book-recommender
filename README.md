
# Simple Book Recommender

Simple book recommender django app

Loom: https://www.loom.com/share/3790f26a80ce448189836bb6ff0809d1


Dataset: https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries?resource=download



## Installation

Install this django project

```
  pip3 install -r .\requirements.txt
  python3 manage.py makemigrations
  python3  manage.py migrate
```

And then run it
```
   python3 manage.py runserver
```
    
## Installation

Install this django project

```
  pip3 install -r .\requirements.txt
  python3 manage.py makemigrations
  python3  manage.py migrate
```

And then run it
```
   python3 manage.py runserver
```
To register:
go to http://127.0.0.1:8000/register/

To login:
go to http://127.0.0.1:8000/login/

To get API access token:
go to http://127.0.0.1:8000/api/token/ and copy paste access token


Assuming you have downloaded the kaggle dataset,

Add access token to utils.py
you can load data into database from it.
python3 utils.py book
python3 utils.py author
python3 utils.py shelf




To add 20 favorites to the first user:
python3 utils.py add_favorites

To test API and suggestion functions:
python3 utils.py test


## Documentation
Suggested Books Algorithm:

1) We get favorite books of the user
2) We get the top shelves associated to those favorite books of the user
3) We then get 1000 books associated with those shelves
4) We sort those books by average rating (highest) and return the top 5 books

There are many ways to suggest books, this is a very simple example that is very fast (measured 60ms for 20 favorite books, on ~50000 books dataset).

We can use other data such as Author data, List data to enhance our suggestions.
We can also use machine learning and/or clustering algorithms to further enhance our suggestion algorithm.
## API Reference


## Books
#### Get all books

```http
  GET /books
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |

#### Get item

```http
  GET /books/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of book to fetch |

#### POST item

```http
  POST /books/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`   | `string` | **Required**. Your access token |
| `id`      | `string` | **Required**. Id of item to fetch |

```http
  PUT /books/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`   | `string` | **Required**. Your access token |
| `id`      | `string` | **Required**. Id of book to update |

```http
  DELETE /books/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`   | `string` | **Required**. Your access token |
| `id`      | `string` | **Required**. Id of book to delete |

```http
  SEARCH /books?search=query
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `query`      | `string` | **Required**. Search query |


## Authors
#### Get all authors

```http
  GET /authors
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |

#### Get author

```http
  GET /authors/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of author to fetch |

#### POST Authors

```http
  POST /authors/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`   | `string` | **Required**. Your access token |
| `id`      | `string` | **Required**. Id of author to add |

```http
  PUT /authors/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`   | `string` | **Required**. Your access token |
| `id`      | `string` | **Required**. Id of author to update |

```http
  DELETE /authors/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`   | `string` | **Required**. Your access token |
| `id`      | `string` | **Required**. Id of author to delete |
