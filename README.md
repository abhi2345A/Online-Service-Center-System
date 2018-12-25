# Restart

DBMS mini-project 1st Sem. It's a fictious service center where users can keep track of their gadgets and miscellaneous repair requests/complaints. Database used is MySql. A quick demo of this project can be seen [here](https://restartx.herokuapp.com/center/). If you'd like to try it locally on your machine follow the steps below:

## Built With

* [Django](https://docs.djangoproject.com/en/2.1/) - Web framework used
* [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) - For designing pages
* [Heroku](https://devcenter.heroku.com/categories/reference#deployment) - For working with project in production

## Prerequisites

It's better to work with this sample in a virtual environment so that you don't mess with the existing python packages. If you don't have virtualenv, open a terminal window and install it by typing this:

```
sudo apt install virtualenv
```

Navigate to your users home directory:

```
cd
```

Create a directory named python env

```
mkdir py-env
```

Navigate in the newly created directory:

```
cd py-env
```

Create a virtual environment in Python 3 with the environment name of env:

```
virtualenv -p python3 env
```

Validate that environment is installed with python3:

```
ls env/lib
```

## Activate Environment

```
source env/bin/activate
```

Make sure you're in the home directory of the project (that is, wherever the manage.py file is present). Now, install the required dependencies via :

```
pip install -r requirements.txt
```

If you want to deactivate virtualenv, do it by simply typing 'deactivate'.


## Demo

Create the database by doing this : 

```
python manage.py migrate
```

Run the project on localhost by typing this into the terminal :

```
python manage.py runserver
```
