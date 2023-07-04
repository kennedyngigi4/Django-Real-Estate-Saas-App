# Django Real Estate SaaS App

This project is an illustration of how one can develop a SaaS application using Django. How to tackle the issue of tenancy dynamically 
by identifying each registered user with a Unique Tenant ID. The project will also use multiple databases i.e for users, listings, etc. 
Django doesn't solve the issue of cross-database relations while using multiple databases and thus we shall use the unique tenant id generated during registration across the different databases.

This is a web application that can be used in marketing and management of properties by a property management company. 

The key things I want to tackle in the backend development are;
  * How to use a Custom UserModel in Django
  * Assigning of different roles in a Django application
  * Using multiple databases for different applications in a Django project
  * Since Django doesn't support cross-database relations we are going to overcome this by the use of a unique tenant ID.
  * Integration of SimpleJwt for Authentication & Token generation.





### Technologies used
* Django Rest Framework
* SimpleJWT
* MySQL & PostgreSQL databases
* VueJS for the frontend
* Angular 13 for Admin & Realtor dashboards
* Tailwind
* 







