## Setup Backend API server

1. Create virtual python environment `python -m venv .venv`
2. Activate .venv
3. Install packages django and djangorestframework
4. Run `django-admin startproject newproject` to create a new project
5. Go to the newproject folder, to create a RestFul API, run `python manage.py api`
6. To create the database table, run `python manage.py makemigrations`, then `python manage.py migrate`
7. Now start your backend: `python manage.py runserver`. You might get page not found errors if you forgot to include `rest_framework` and `api` in the `INSTALLED_APP` block of your `settings.py`.
8. You will get a CORS error as the front-end is making an API call from a different ORIGIN. To resove this, you need to install `django-cors-headers` package, include it in the INSTALLED_APPS and MIDDLEWARE block, then add the `CORS_ALLOWED_ORIGINS` and `CORS_ALLOW_METHODS`
   > Keep in mind that each of these topics are separate and distinct issues:
   >
   > - Cookies: A cookie issue might be that a cookie set by one site is not visible and is not supposed to be leaked to any other sites
   > - CRSF: A CSRF issue applies if you are not getting the proper token from a site when you try to post to that site.
   > - CORS: Policies that control the JavaScript code loaded from one site to make an AJAX call to a different site
9.
