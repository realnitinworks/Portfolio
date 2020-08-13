Project
-------
![Continuous Integration and Delivery](https://github.com/realnitinworks/portfolio/workflows/Continuous%20Integration%20and%20Delivery/badge.svg)

This repository contains the source code of my Portfolio project. My portfolio web application which I developed through this project is deployed on Digital Ocean and live on [realnitinworks.com](https://realnitinworks.com/). 

The [Django Web Framework](https://www.djangoproject.com/) powers this project for the most parts while the Frontend is handled by the [Bootstrap Framework](https://getbootstrap.com/) and some custom styles. 

The portfolio web application mainly includes [my portfolio](https://www.realnitinworks.com/portfolio/) and [my blog](https://www.realnitinworks.com/blog/).

The Journey
-----------

I used to write blogs [here](https://realnitinworks.netlify.app/). The posts were served using 3rd-party applications like Pelican and Netlify.
However, I was not satisfied because I could not write the backend for serving my blog posts. Moreover, Netlify had some issues concerning SSL certificates
and on some days my blog was reported as `not secure`. In addition to this, I didn't have a portfolio site until that point. So I decided to develop an application for my portfolio and blog from scratch, writing everything on my own.

The first thing which I did was to create a repository on Github. Then I created a [Project](https://github.com/realnitinworks/portfolio/projects) on the repository and started listing down all the features (in Kanban style) I needed for my web application. This gave me a clear idea of my target. Slowly but surely I knocked down and completed one task after another.

Many a time I did not know how to tackle a task at first. But I stayed long with the problem without losing focus. I struggled with the problem, kept searching for the answer until I found it. 

Before this project, I had experience with `Django` and `Flask`. However, I wanted to get serious with at least one of these. I decided to go with Django. But it does matter. It is just my personal preference. In the past, I used to get bogged down by the UI design. That is where a framework like `Bootstrap` helped me to get started without getting lost in the frontend.

I containerized my applications using `Docker` and `Docker-Compose` for development and production. My applications run on containers deployed through Docker and Docker-Compose on the Digital Ocean cloud.

Features
-------

1. **Blog**
   1. Post list and detail view
   2. Markdown support for rendering post content and code highlighting
       * Used [Mistune](https://mistune.readthedocs.io/en/latest/) Python package
       * Used [Django Pagedown](https://pypi.org/project/django-pagedown/) package for previewing markdown in the admin backend.
   3. Pagination support for the post list view
   4. Support for sharing the posts by email
   5. Comment system for the blog
      * Users of the blog can comment on posts
   6. Blog stats
      * Latest Posts
      * Most commented posts
      * Popular tags
      using Django TemplateTags
   7. Tag posts using keywords
      * Retrieve similar posts using tags
   8. RSS feeds for the posts
   9. Full-Text Search support for posts
      * Using [Django Full Text Search](https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/search/) 
2. **Portfolio**
   1. List and Detail view of 
      * Projects I have completed
      * Certificates I have achieved
      * Opensource projects I have contributed to
      * My coding profile 
3. **CI/CD**
   
   When the local code changes are pushed to Github, Github Actions builds and deploys the application to Digital Ocean droplet
   
4. **Email Support**
   
   Used [SendGrid](https://sendgrid.com/) for sending mails. For example: When someone [contacts](https://www.realnitinworks.com/contact/), I will get a mail notification
   
5. **Code Styling and Formatting**

   Used [Black](https://pypi.org/project/black/), [Flake8](https://pypi.org/project/flake8/) and [isort](https://pypi.org/project/isort/)
   
6. **Form protection**
   
   1. Used [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3)
   2. Used [Django reCAPTCHA](https://pypi.org/project/django-recaptcha/) package
   
7. **Domain and Email**

   1. From Godaddy
   2. Domain: realnitinworks.com

8. **HTTPS support**

   1. SSL certificate from [Let's Encrypt](https://letsencrypt.org/)
   
9. **Digital Ocean Deployment**

   1. Used Docker and Docker-Compose
   2. Following service are deployed in containers
      * Portfolio Web application - the application running on realnitinworks.com
      * PostgreSQL database service - the database runs on PostgresSQL
      * Nginx Proxy - for serving static and media files
      * Nginx Proxy Letsencrypt - for getting and renewing SSL certificate from Let's Encrypt
      
Running the Project locally
-------------------

> $ git clone https://github.com/realnitinworks/portfolio.git

> $ cd portfolio

> $ docker-compose up -d # To start the application. App starts on 127.0.0.1:8000/

> $ docker-compose down  # To shutdown the applicaiton.

Technologies used
-----------------

1. Web App - Django
2. Containerization - Docker, Docker-Compose
3. UI - Bootstrap and CSS
4. Database - PostgreSQL
5. Reverse Proxy - Nginx
6. Cloud deployment - Digital Ocean
7. CI/CD - Github Actions
8. SSL - Let's Encrypt

Advice to those who want to create their own Portfolio
-------------------

1. Study just enough of a web framework.
2. List down the features you want for the portfolio.
3. Don't wait. 
4. Get started.
5. Knockdown one feature at a time.
6. Persist and be consistent.
7. Use Docker for local development. This makes your life much easier without worrying about dependencies

References
----

1. [Django 3 By Example - Antonio Mele](https://www.amazon.in/Django-Example-powerful-reliable-applications/dp/1838981950) - A great book on Django for developing real-world web applications.

   The first project in this book is, in fact, a `blog` application. 
   
2. [Testdriven.io course on Django and Django REST Framework](https://testdriven.io/courses/tdd-django/)

   I cannot thank Testdriven.io for the real quality courses they produce. Learned a lot from here regarding Django development for production, using Docker, etc.
   
3. [Testdriven.io blog](https://testdriven.io/blog/)

   The blog posts here are equally good as their courses. My portfolio app deployment on Digital Ocean, CI/CD using Github, Heroku deployment, SSL certificate generation
   are all based on the learnings from their blog.
 





