# Setup

1. Open this folder in Terminal. 
2. Start Server using :
      ` python3 manage.py runserver <optional: port Number>`
      Let port number be 8080.
3. If there were no errors, go to localhost:8080 

## Urls

### Authors
* `localhost:8080`  :  Leads to Authors by default and is the same as the following url
* `localhost:8080/authors` : Lists all authors for GET request

* `localhost:8080/authors` : POST request will create new author
    * expected input type : json with following key, value pairs
    * username  : author user name,  unique
    * email : author_email,  unique
    * image : imagefield  (optional)
    * nickname : anystring
    * password : Author_password
    
    sample post query: 
    ```
    {
        "username": "Author4",
        "email": "author4@gmail.com",
        "nickname": "mynickname4",
        "password": "testing321"
    }```
    
*   `localhost:8080/authors/<str:author_username>` GET returns author with username author_username if exists else returns 404
*   `localhost:8080/authors/<str:author_username>` PUT updates author. Expected key values are:
      ```
      {
    "username": "Author4",
    "email": "author4@gmail.com",
    "nickname": "My Updated Nickname4",
    "password": "testing321"
      }
      
      
    ```
    
*   `localhost:8080/authors/<str:author_username>` DELETE request deletes the author


### Users

* `localhost:8080/users` GET request returns list of all Users
* `localhost:8080/users` POST request with json content creates user. Fields :
    * username  : user_user name,  unique
    * email : user_email,  unique
    * image : imagefield (profilepic)  (optional)
    * about : anystring
    * password : User_password

    sample json content:
    ```
    {
       "username": "TestUser11",
       "email": "testuser11@gmail.com",
       "about": "About testuser11",
       "password": "testing321"
    }
    ```
  
 * `localhost:8080/users/<str:user_username>` GET request returns user with the username with status_200_OK if user exists else returns 404
 * `localhost:8080/users/<str:user_username>` PUT request updates user data if exists else return error 404
    Sample json content
    ```
    {
       "username": "TestUser11",
       "email": "testuser11@gmail.com",
       "about": "Updated About testuser11",
       "password": "testing321"
    }
    ```
    
*   `localhost:8080/users/<str:user_username>` DELETE request deleted said user


### Books
note: Books urls can retrive data and delete, however, creation, updation might introduce an error :)

*   `localhost:8080/books` GET request returns list of all Books
*   `localhost:8080/books` POST request with json content creates Book. Fields are :
    ```
     {
        "name": "Book1",
        "description": "Book Description",
        "author": "Author1"
     }
     ```
*   `localhost:8080/books/<str:Book_Name>` GET request return book with Book_Name if exists else returns 404
*   `localhost:8080/books/<str:Book_Name>` PUT
    ```
     {
        "name": "Book1",
        "description": "Book Description",
        "author": "Author1"
     }
     ```
     
*    `localhost:8080/users/<str:Book_Name>` DELETE request deletes book with name Book_Name
   
