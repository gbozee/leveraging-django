## Login with Email
Django by default, comes with a `User` model that has the following fields `username, first_name, last_name, email, password`

To follow the explanation, take a look at the `email_login` django project.

Since django comes with a default authentication module, we would be reusing that but kinda customizing it to suit our purpose. Django by default requires both a `username` and a `password` for login in, in its default implementation. 

We would be implementing a custom version of the LoginForm in our case [forms.py](../email_login/email_login/forms.py)

We need to tell django that we want to authenticate using email and password, so we would need to implement a custom authentication backend [backends.py](../email_login/email_login/backends.py)

After implementing this `backends.py`, we need to add it to the list of authentication backends supported by django in the [settings.py](../email_login/email_login/settings.py)

```
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "email_login.backends.EmailLoginBackend"
)
```
**NB**: Note we did retain the default backend provided by django so that we can still login to our admin.

We then implemented a custom version of the login view in the [urls.py](../email_login/email_login/urls.py) and added all the necessary urls

You can choose to specify where to be redirected to when logged in and when logged out in the `settings.py` if nothing is specified, the `/accounts/profile/` url and view would need to be implemented and the [registration/logged_out.html](../email_login/templates/registration/logged_out.html) template would need to be customized

the settings config are as follows 
```
LOGOUT_REDIRECT_URL='/login/'
LOGIN_REDIRECT_URL='/accounts/profile/'
```
**NB**: Based on the default [settings.py](../email_login/email_login/settings.py) I added a configuration for the `TEMPLATES` config
```
# this directory is in the same location as the manage.py
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR,'templates')], 
        ...
    },
]

```