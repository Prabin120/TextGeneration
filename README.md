# Project Setup

This project is a Django application that includes JWT authentication and endpoints for generating summaries and bullet points.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Python 3.8+](https://www.python.org/downloads/)
- Pipenv (pip install pipenv)
- [Git](https://git-scm.com/)

## Project Setup

   1. **Clone the Repository:**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/Prabin120/TextGeneration
   cd TextGeneration
   ```

2. **Virtual environment**
   
   Creating and activating virtual environment
    ```bash
    pipenv install  #to install the packages
    pipenv shell    #to acticate the virtual environment
    ```

3. **Environment Variable**

   i) create a new file in the project level as **.env**
   
   ii) Look into the **.env.example** file and setup the variables inside the **.env** file




## Running the server

``` bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Now your server is running and can be access through **localhost:8000**

## API endpoints

Follow the links to get the available api endpoints after running the application

1. **Swagger Docs**
link: **localhost:8000/swagger**

2. **Redoc docs**
link: **localhost:8000/redoc**


## Testing the APIs

Run the below code in terminal to run all the test cases
``` bash
python manage.py test
```