## Handle Swachh toilets ##

### Prerequisites ###

    *  Python >= 3.6
    *  pipenv >= 11.10
    *  MongoDB >= 3.6

### Installation ###

    * run `git clone https://github.com/samayamnag/flask-sm-meta-data.git <projectname>` to clone the repository
    * run `cd <projectname>`
    * run `cp .env.example .env`
    * configure .env
    * run `pipenv shell --python=3.6` to set up environment. --python argument is optional. This is to       specify specific python version 
    * run `pipenv install` to install dependencies

### Run the Application


```sh
$ python manage.py run
```

Access the application at the address [http://localhost:5000/](http://localhost:5000/)

### Testing

Run unittests:

```sh
$ python manage.py test
```

Run flake8 on the app:

```sh
$ python manage.py flake
```

or

```sh
$ flake8 project
```
