# Python Blog
Webapp written in Python, using Google App Engine, that allows you publish your own posts and like someone elses!

## Features
+ Signup
+ Login
+ Logout
+ Create new posts
+ Edit and delete your posts
+ Like posts made by someone else

## Structure
The backend root file would be _blog.py_, where rests the parent Handler class. The rest of the modules work as child instances of this.

The templates and styles are in the _templates_ folder, powered by Jinja2.

## Usage
If you clone this repo, and have installed [Python](https://www.python.org/downloads/) and [Google App Engine](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python) you could run my code and create your own blog.

Notice that the config.py file is ignored. You have to create one yourself with an string in order to create the salt to hash the userid cookie. Use the following format.

```python
config = {
    'SECRET': 'RandomStringHere'
}
```

In order to launch a local server from terminal:
```sh
$ dev_appserver.py .
```

Don't forget to configure _app.yaml_. Further info [here](https://cloud.google.com/appengine/docs/standard/python/config/appref)

Also, I have deployed the blog [here](https://serene-voltage-144210.appspot.com/blog) if you want to try it without cloning.

### Contributing
If you fancy, you can make a pull request and improve the functionality or even the UI of the site.
Any possible issues, you can report them [here](https://github.com/pgarciaegido/python_blog/issues).

### Contact
You can contact me on pgarciaegido@gmail.com
