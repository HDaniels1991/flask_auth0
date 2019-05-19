# Flask Dance using Auth0

This repo demonstrates how to manage user authentication within a simple Flask web application using the Flask-Dance library and Auth0.

* Auth0 operates a cloud based identity platform for developers.
* Flask-Dance handles the OAuth dance with style using Flask, requests, and oauthlib.

## Quickstart

### Auth0

1. Sign up for a free Auth0 account [here](https://auth0.com/)
2. Create a 'Regular web application'
3.  In the settings tab for the new application enter the following values:
* Allowed Callback URLs: http://127.0.0.1:5000/auth0_login/auth0/authorized
* Allowed Logout URLs: http://127.0.0.1:5000

### Flask

1. Clone this repository using the following command:
```bat
git clone https://github.com/HDaniels1991/flask_auth0.git
```
2. Create a virtual environment.
3. Install required libraries using the following command:
```bat
pip install -r requirements.txt
```
4. Create a .env file in the top directory and define the global variables:
```python
auth0_client_id = The Auth0 Client ID
auth0_client_secret = The Auth0 Client Secret
auth0_base_url = The Auth0 Domain
auth0_token_url = The Auth0 Domain + /oauth/token
auth0_authorization_url = The Auth0 Domain + /authorize
```
5. Create the Database with the following commands in python:
```python
from app import db
db.create_all()
```
6. Run the application:
```bat
python app.py
```

## Author

Harry Daniels
