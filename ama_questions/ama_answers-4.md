# 1. What is metatag and give some examples

Meta tags are HTML tags that provide metadata about a webpage (not visible on the page). Examples include `<meta charset="UTF-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1.0">`, and `<meta name="description" content="Sample page">`.



# 2. Explain the flow of Django

A request hits the URL router → mapped to a view → view interacts with models → data is passed to a template → response is sent back to the client.

# 3. Difference between project and app

A project is the entire Django application setup, while an app is a modular component that handles a specific feature within the project.

# 4. What if I use POST request for update

It will still work, but it's not RESTful; typically PUT/PATCH is used for updates, while POST is meant for creating resources.

# 5. Difference between library and framework

A library gives you tools to use, while a framework controls the flow and you plug your code into it.

# 6. What are Django key features

Django offers built-in ORM, admin panel, authentication, scalability, and security features like CSRF protection.

# 7. Delete on-cascade

On delete cascade means when a parent object is deleted, all related child objects are automatically deleted as well.

# 8. What is settings.py

It is the main configuration file in Django where you define installed apps, database settings, middleware, and more.

# 9. Is Django a library or framework

Django is a full-stack web framework.

# 10. What is ORM

ORM (Object Relational Mapping) allows you to interact with the database using Python code instead of writing SQL queries.

# 11. What is static file in Django

Static files are CSS, JavaScript, and images used to style and add behavior to your web application.

# 12. Top most object in browser

The top-most object in the browser is the `window` object.

# 13. What is MVT

MVT stands for Model-View-Template, Django’s architecture pattern similar to MVC.
