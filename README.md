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
          cd activate
          cd ..
          cd..
  #### .Install requirements :
        pip install requirements.txt
  #### . Start the server :
        python manage.py runserver
## Usage : 
  Access The Application :
      Once the Docker containers are up and running, you can access the Django application at-
      http://localhost:8000
       
