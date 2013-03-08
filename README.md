django-example-project
======================

- Demonstrates best practices I have learned with my time spent working with [Django].
- Currently targets [Django 1.5].

Features
--------

This repository demonstrates:

- Repository-level layout and organization
- Project-level layout and organization
- Gunicorn WSGI HTTP Server
- Procfile-based process management with [Foreman], which is great for deploying to [Heroku]
- [Supervisor] based process management

Usage
-----

Once you have cloned this repository, you can run the example project with either [Foreman] or [Supervisor]. Either approach is fine.

I've found that Supervisor works great for local development where you have multiple processes to manage (usually a database such as PostgreSQL or MySQL) in conjunction with the Django Python process. I usually use a managed database solution such as [Heroku Postgres] or [Amazon RDS] for staging and production deployments, and a local install for my local development.

The choice is, obviously, up to you. Not being able to blow away your entire staging database as easily as `rf -rf ./db` or whatever is a best practice in my experience because it forces you to use migrations and be thoughtful about how to treat your database.

Running with Foreman
--------------------

Foreman goes well with Heroku. To run the application with Foreman simply run `foreman start` in the repository root (where the Procfile lives).

Running with Supervisor
-----------------------

Alternatively, to run the application with Supervisor simply run `supervisord` in the repository root (where the supervisord.conf file lives).

  [Django]: https://www.djangoproject.com/
  [Django 1.5]: https://docs.djangoproject.com/en/1.5/
  [Foreman]: https://github.com/ddollar/foreman
  [Gunicorn]: http://gunicorn.org/
  [Heroku]: http://www.heroku.com/
  [Supervisor]: http://supervisord.org/
  [Heroku Postgres]: https://postgres.heroku.com/
  [Amazon RDS]: http://aws.amazon.com/rds/
