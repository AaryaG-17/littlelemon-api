LITTLE LEMON RESTAURANT API - PEER REVIEW GUIDE
================================================
Stack: Django, Django REST Framework, MySQL, Pipenv, Djoser, TokenAuthentication.

SETUP
1. Install Python 3.12, Pipenv, and MySQL Server.
2. In MySQL, run (change the password):
   CREATE DATABASE littlelemon_api CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'littlelemon_user'@'localhost' IDENTIFIED BY 'change-this-password';
   GRANT ALL PRIVILEGES ON littlelemon_api.* TO 'littlelemon_user'@'localhost';
   FLUSH PRIVILEGES;
3. Export local DB configuration:
   export DB_NAME=littlelemon_api
   export DB_USER=littlelemon_user
   export DB_PASSWORD='change-this-password'
   export DB_HOST=127.0.0.1
   export DB_PORT=3306
4. Run:
   pipenv install
   pipenv run python manage.py check
   pipenv run python manage.py migrate
   pipenv run python manage.py test restaurant
   pipenv run python manage.py runserver
5. Optional admin:
   pipenv run python manage.py createsuperuser

API PATHS FOR INSOMNIA
Website:
  GET http://127.0.0.1:8000/

Menu API (public GET; writes require staff or Manager group):
  GET    http://127.0.0.1:8000/api/menu/
  GET    http://127.0.0.1:8000/api/menu/1/
  POST   http://127.0.0.1:8000/api/menu/
  PUT    http://127.0.0.1:8000/api/menu/1/
  PATCH  http://127.0.0.1:8000/api/menu/1/
  DELETE http://127.0.0.1:8000/api/menu/1/

Booking API (authentication required):
  GET    http://127.0.0.1:8000/api/bookings/
  POST   http://127.0.0.1:8000/api/bookings/
  GET    http://127.0.0.1:8000/api/bookings/1/
  PUT    http://127.0.0.1:8000/api/bookings/1/
  PATCH  http://127.0.0.1:8000/api/bookings/1/
  DELETE http://127.0.0.1:8000/api/bookings/1/

Registration/authentication:
  POST http://127.0.0.1:8000/api/auth/users/
  GET  http://127.0.0.1:8000/api/auth/users/me/
  POST http://127.0.0.1:8000/api-token-auth/

REGISTER JSON:
  {"username":"reviewer","password":"StrongPassword123!","re_password":"StrongPassword123!"}
TOKEN JSON:
  {"username":"reviewer","password":"StrongPassword123!"}
Send this header for protected requests:
  Authorization: Token YOUR_TOKEN_VALUE

MENU POST JSON:
  {"title":"Greek Salad","price":"12.50","inventory":20}
BOOKING POST JSON:
  {"name":"Aarya","no_of_guests":2,"booking_date":"2030-12-13T19:00:00+05:30"}

PERMISSIONS
- Anyone can read menu items.
- Menu writes require staff or membership in the Django group named Manager.
- Booking endpoints require authentication.
- Regular users can only access their own bookings; staff can access all bookings.
- Past booking dates are rejected.

GITHUB SUBMISSION
Run:
  git init
  git add .
  git commit -m "Build Little Lemon restaurant API capstone"
  git branch -M main
  git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
  git push -u origin main
Commit Readme.txt. Do not commit real database passwords.
