# django-excel-export demo
The demo app for django-excel-export.
 
## Running Locally

Make sure you have Python3 [installed locally](http://install.python-guide.org). 

```sh
$ git clone https://github.com/zhangyu836/django-excel-export-demo.git
$ cd demo
$ pip install -r requirements.txt
$ python manage.py runserver
```

The demo app should now be running on [localhost:8000](http://localhost:8000/).
-  User: admin
-  Password: admin

## Deploying to Heroku

To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

```sh
$ heroku create
$ git push heroku main/master
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku run python manage.py loaddata app
$ heroku open
```

[Live Demo](https://tranquil-tundra-83829.herokuapp.com/)   
-  User: admin
-  Password: admin   

Note:   
["Heroku has an ephemeral filesystem....So Any file written on disk will be lost when the dyno is restarted, and is not recoverable."](https://stackoverflow.com/questions/32459959/heroku-paperclip-images-appear-but-then-disappear)   
Images uploaded via Django admin site will be lost too.    
Files collected from 'static' folders will be copied to /tmp/bulid_xxxxx/staticfiles, they will persist across restarts.

## Testing Template File

You can test your template file in the same way as in the test.py file.
