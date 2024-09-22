import json
import requests
import sys
import timeit
import random
## get token from http://127.0.0.1:8000/api/token/
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2OTc3ODIwLCJpYXQiOjE3MjY5NzQyMjAsImp0aSI6IjM0ZGNlZmQ1MDRhMTRkN2RhNTcyM2RjZDJjMjg2Zjc0IiwidXNlcl9pZCI6MX0.6b-IZuyYODFkfk7AZOg6sehH_9C9sxnup47ir7zc0qs"
headers = {'Content-Type': 'application/json',
           "Authorization": "Bearer " + token}

# get datasets from https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries?resource=download


def books():
    with open("../dataset/books.json",'r') as f:
        while True:
            line = f.readline()
            data = json.loads(line)  
            book_mapping = {  
            "id": "book_id",
            "title": "title",
            "isbn": "isbn",
            "isbn13": "isbn13",
            "ratings_count": "ratings_count",
            "average_rating": "average_rating",
            "description": "description",
            "author_id":"author_id",
            "author_name":"author_name",
            }
            post_data = {}
            url="http://127.0.0.1:8000/books/"
            for k,v in data.items():
                if k in book_mapping.keys():
                    post_data[book_mapping[k]] = v
            try:
                x = requests.post(url, json = post_data, headers=headers)
            except Exception as e:
                print(e)
                break
            if not line:
                break

def shelf():
    with open("../dataset/books.json",'r') as f:
        while True:
            line = f.readline()
            data = json.loads(line)  
            for shelf in data['shelves']:
                post_data = {}
                url="http://127.0.0.1:8000/books_shelf/"
                post_data["book_id"] = data['id']
                post_data["shelf_name"] = shelf['name']
                post_data["shelf_count"] = shelf['count']
                try:
                    x = requests.post(url, json = post_data, headers=headers)
                except Exception as e:
                    print(e)
                    break
            if not line:
                break

def authors():
    with open("../dataset/authors.json",'r') as f:
        while True:
            line = f.readline()
            data = json.loads(line)  
            author_mapping = {  
            "id": "author_id",
            "name": "name",
            "about": "about",
            "fans_count": "fans_count",
            "image_url": "image_url",
            }
            post_data = {}
            url="http://127.0.0.1:8000/authors/"
            for k,v in data.items():
                if k in author_mapping.keys():
                    post_data[author_mapping[k]] = v
            try:
                x = requests.post(url, json = post_data, headers=headers)
            except Exception as e:
                print(e)
                break
            if not line:
                break

def timed_request(url,method,data=None,get_id=False,print_response=False):
    start_time = timeit.default_timer()
    if method == 'post':
        x = requests.post(url, json = data, headers=headers)
    elif method == 'get':
        x = requests.get(url, headers=headers)
    elif method == 'put':
        x = requests.put(url, json=data, headers=headers)
    elif method == 'delete':
        x = requests.delete(url,json=data, headers=headers)
    end_time = timeit.default_timer()    

    if x.status_code == 400:
        print(x.text)
    if get_id:
        response = x.json()
        for k,v in response.items():
            if k == 'id':
                return v
    if print_response:
        responses = x.json()
        for response in responses:
            for k,v in response.items():
                if k == 'title':
                    print(v)
    print (url,method,x.status_code,str(int((end_time-start_time)*1000)) + 'ms')   
    return None    


def add_favorites():
    print("--Adding Favorite_Books--")
    url="http://127.0.0.1:8000/favorite_book/"
    for i in range(20):
        book_id = random.randint(0,100)
        timed_request(url,'post',data={'user_id':1,'book_id':book_id})

def test():
    ## CRUD operations
    print("--Books--")
    url="http://127.0.0.1:8000/books/"
    timed_request(url,'get')
    url="http://127.0.0.1:8000/books/1/"
    timed_request(url,'get')
    url="http://127.0.0.1:8000/books/"
    my_id = timed_request(url,'post',data={'book_id':-102,'title': 'i am tiny kitten3','ratings_count':100,'description':'cow'},get_id=True)
    url="http://127.0.0.1:8000/books/" + str(my_id) + '/'
    timed_request(url,'put',data={'book_id':-100,'description':'how'})
    url="http://127.0.0.1:8000/books/"+ str(my_id) + '/'
    timed_request(url,'delete') 
    url="http://127.0.0.1:8000/books?search='harry'"
    timed_request(url,'get')

    print("--Authors--")
    url="http://127.0.0.1:8000/authors/"
    timed_request(url,'get')
    url="http://127.0.0.1:8000/authors/1/"
    timed_request(url,'get')
    url="http://127.0.0.1:8000/authors/"
    my_id = timed_request(url,'post',data={'author_id':-102,'name': 'cat','fans_count':1000,'image_url':'123'},get_id=True)
    url="http://127.0.0.1:8000/authors/"+ str(my_id) + '/'
    timed_request(url,'put')
    url="http://127.0.0.1:8000/authors/"+ str(my_id) + '/'
    timed_request(url,'delete') 

    print("--Book Suggestions--")
    url="http://127.0.0.1:8000/suggested_books/"
    timed_request(url,'post',data={'user_id':1},print_response=True)


if __name__ == "__main__":
    if sys.argv[1] == "book":
        books()
    if sys.argv[1] == "shelf":
        shelf()
    if sys.argv[1] == "author":
        authors()
    if sys.argv[1] == "test":
        test()
    if sys.argv[1] == "add_favorites":
        add_favorites()