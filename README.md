#  WATCHLIST

#### Author: [Kiptoo-Rotich](https://github.com/Kiptoo-Rotich)

## Screenshots
![watchlist1](https://user-images.githubusercontent.com/48821300/123549644-8acf0a00-d772-11eb-8987-940c8e13a0a0.png)
![watchlist2](https://user-images.githubusercontent.com/48821300/123549680-a63a1500-d772-11eb-9fb1-44cb1637b4d9.png)
![watchlist3](https://user-images.githubusercontent.com/48821300/123549686-afc37d00-d772-11eb-90ab-37ccdf2e1ddc.png)
![watchlist4](https://user-images.githubusercontent.com/48821300/123549701-bb16a880-d772-11eb-82e7-7c9b08e14ef4.png)


## Description
This application uses movie API to display various movies in three categories i.e popular, upcoming and now-showing. Users can give their reviews in any movie they want to. However, to do this, they need to register first, if they don't have an account or login in the already have an account.

As a user of the web application you will be able to:

1. Sign up and log in
2. View movies
3. Write a review
4. Edit profile
5. Update profile

## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/kiptoo-rotich/Watchlist
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='development'
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:5000](http://127.0.0.1:5000/)



   
## Built With

* [Python3.8](https://docs.python.org/3/)
* Postgresql 
* Boostrap
* Flask
* HTML
* CSS


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license)