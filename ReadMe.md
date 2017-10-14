## Simple Tasks made possible in Django

Django is a powerful web framework that comes with _batteries_ included for speeding up web development. 

There are also a lot of third party reusable django applications that can be plugged into your codebase. **While this is generally a good thing**, more often than not, most third party reusable django apps suffer from either or both of the problems listed below.

1. Reusable app is poorly documented. 
2. Reusable app is doing way too much than you actually need.

Another problem when you depend on too many reusable django application is the tendency to run into models/db tables bloat. What I mean is you end up with a database with a large number of tables, most of which aren't code you wrote. 

The beautiful thing is, since django comes with some batteries included, some of the tasks which we would normally depend on a third party library on can be accomplished relatively easy using some of the django internals/batteries provided.

I would be making a list of some of these task and providing simple solutions that are easy to follow to them.

1. [Ability to Login with Email.](docs/login-with-email.md) *project-name: email_login*
2. Ability to Login with either Email or Username
3. Easily setting up Social Authentication (Facebook and Google)
4. Ability to Signup without having to set username.

I would be creating a sample django project that implements some of these ideas as they are listed.

