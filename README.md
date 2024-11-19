# Challenge 1: User Authentication API with Docker and Django
## Project Description :
  The User Authentication API project is designed for securely managing user authentication in web applications. Built with Django, this API leverages Docker for                               containerization, ensuring consistency across different development and production environments. Additionally, the project integrates JSON Web Tokens (JWT) to handle user                   authentication,providing a secure and stateless mechanism for user sessions.
## Features :
    -1. Users can register and authenticate using JSON Web Tokens (JWT) for secure sessions.
    -2. JWT-based authentication protects all API endpoints, ensuring only authorized access.
    -3. The project is containerized with Docker for consistent environments and easy scalability.
## Installation Instructions :
  ### Prerequisites :
      -Docker.
      -Docker-compose.
      -Git.
  ### Steps :
  #### 1. Clone the Repo :
          git clone https://github.com/Rudraparbat/Jwt-auth.git
  #### 2. Go to the project directory : 
          cd Jwt-auth  
  #### 2. Start the container : 
          docker-compose up --build
  ### In case you dont use docker then (Note that if you dont use docker then) :
        Follow the first cloning step and second step then
  #### . Create a virtual env :
          python -m venv env
  #### . Activate env :
          cd env
          cd scripts
          activate
          cd ..
          cd..
  #### .Install requirements :
        pip install requirements.txt
  #### . Start the server :
        python manage.py runserver
## Installation errors :
  #### 1. When you are starting the Docker container, you might encounter an error: Error response from daemon: Conflict. The container name "my-container-name" is already in use by container "659aac92f48f6498cbcba5614f67c77b8a4b8c60694622e094ae87f2e2d086ac". You have to remove (or rename) that container to be able to reuse that name. If you see this, go to the docker-compose.yml file, change the container name, and then run the docker-compose up --build command in your terminal. This should fix the issue.
  
#### 2. When installing requirements.txt without Docker, you might encounter an error while downloading the psycopg2-binary library, stating that you need pg_config. This is not an issue within the project itself; rather, you need to set up pg_config by installing PostgreSQL. To avoid this conflict, navigate to the Dauth folder, then open the settings.py file. Scroll down to the database configuration part and comment out the PostgreSQL configuration. This should help you avoid the issue.       
## Usage : 
  Access The Application :
      Once the Docker containers are up and running, you can access the Django application at-
      http://localhost:8000
## After Starting The project :
  Home page :
      ![homepage](https://github.com/user-attachments/assets/7f4b02d8-da9d-4c6a-ba2c-8ad50de0d0b6)
  ##### It is the Home page click the "go to the main page button" for next section
  Main page :
      ![mainpage](https://github.com/user-attachments/assets/9dfd30c0-1797-444c-9ee4-de9a95fe731f)
  ##### in these page you can see three endpoints button 1. profile endpoine , 2. register endppoint ,  3. login endpoint. After clicking these endoints you are going to the next section
  Register endpoint :
      ![register](https://github.com/user-attachments/assets/84d6b16b-6c32-4ecb-a05a-d9fb7879f1bb)
  ##### As a user, you're going to register yourself. To do this, copy the instructions I give below
        {
    "username": "your_user_name",
    "password": "user@200",
    "date_of_birth": "21-12-2003",
    "phone_numbers": 9789343431,
    "email": "justin@gmail.com"
        }
  ##### Copy this and change the credentials as you like, but ensure the username and password are included. You can ignore the other fields if you wish.and dont change any structure or you will get json parse error
  ##### As a response you will get the credentials with sucess message with your ip address.
  Login endpoint :
      ![Login](https://github.com/user-attachments/assets/d76373c4-f517-4f4e-8335-75e23f0ab203)
  ##### In this endpoint you have to login with your registered credentials.copy which i give below 
  
      {
    "username": "your_user_name",
    "password": "user@200"
    }
   ##### Copy this and change the credentials which you registered as username and password, but ensure the username and password are registered.
   ##### As a response, you'll receive a greeting message along with a JWT access and refresh token. Don't be surprised; this is just to show you the tokens. Otherwise, they are securely saved into the server session.
   Profile endpoint :
       ![profile](https://github.com/user-attachments/assets/55fa20b7-7e4c-4611-924a-b0c50d67f186)

##### after login you can see your credentials remeber you have to login otherwise it shows a message to login as a user to see the profile

#### After login if you want to logout, in that url paste http://localhost:8000/api/logout/ hit that and you'll logout automatically

## If Youre using Postman or anyother api tester then :
#### Endpoints :
      Register_endpoint : http://localhost:8000/api/register/ (GET request)
      Login_endpoint : http://localhost:8000/api/login/  (POST request)
      Profile_endpoint : http://localhost:8000/api/profile/  (POST request)
      Logout_endpoint : http://localhost:8000/api/logout/     (GET request)
## Running Tests :
#### To test api endpoints i have written 4 test cases but but there is a cache that whenever i try to test it showing me connection error with container even i specify everything in my docker-compose.yml file . So test the test cases just press ctrl+c to stop the container . then 
##### 1st . After stopiing the container install env , activate it and install all reqirements and start server locally for these steps follow installation process without docker
##### 2nd . hit a command
        python -m pytest
##### And tests are running
 ## Note :
   If you guys can help me it would be great for running testcases thank you

## Technology used :
###### Django: Core web framework for the backend.

##### PostgreSQL: Database system for storing user data.

##### JWT: JSON Web Tokens for secure and stateless authentication.

##### Docker: Containerization platform to ensure consistent environments.

  
  




       
