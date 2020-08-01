In this course, I am learning the basics of Django for web development by building my own website—a personal portfolio—from the ground up. Instructor Nick Walter steps through how to create a database, design the layout for the website, add and update URL paths. I am learning how to connect Django project to Postgres, add static files and URLs, and more under mentorship and pair programming with sCam.

# App Learning Objectives

- Setting up URLs in Django project
- Creating models in Django
- Connecting Django project to Postgres
- Adding static images
- Designing the layout for website
- Creating object views
- Updating URL paths

# App Deployment on Heroku
This app will run in multiple environments, locally and in production with Heroku using config vars

```
heroku config
```

```
heroku config:get GITHUB_USERNAME
```

```
heroku config:set GITHUB_USERNAME=xxxxxxx
```

PS: Heroku Dashboard can also edit the config vars


# sCam notes

## Running the project locally

To run the project, you need to set up the environment variables, which can do locally by sourcing the init shell file. You'll need to copy the `init_template.sh` file and add some values if you have not already done this.

```
cd portfolio
source init.sh
```

## Deployment

Project is hosted on Heroku, currently in sCam's account which Em is added as a collaborator to. If you're setting up a new instance of the project on your computer, you can add the exisiting Heroku remote by running:

`heroku git:remote -a portfoilioem`

To deploy the project, just push your local master branch to the `heroku` remote:

`git push heroku master -f`

The force flag is used just in case things have slipped out of sync.

Remember to set a value for `SECRET_KEY` in the Heroku settings / config vars part of the web interface.
