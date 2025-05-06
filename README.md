# 🐶 Pet Services Booking Web Application

This is a Django-based web application that allows pet owners to book various services for their pets such as grooming, veterinary visits, training, and more. The platform includes user registration, service selection, booking management, booking status and an admin dashboard.

## 🚀 Features

- 📋 List of available pet services
- 🐾 Book appointments for pets
- 🔐 User authentication (signup/login/logout)
- 🧾 View and manage bookings
- 🛠️ Admin panel to manage services and bookings

## 🧰 Technologies Used

- Python (Django)
- SQLite (default database)
- HTML, CSS, JavaScript (Frontend)
- Django Templates
- Git/GitHub (Version Control)

1. Clone the repository:
   ```bash
   git clone https://github.com/praveen21082003/pet_gromming
   cd pet-grooming-project
   
2. Create and activate a virtual environment:
    ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   
3. Install dependencies:
    ```bash
   pip install -r requirements.txt
   
4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser

6. Run the server:
   ```bash
   python manage.py runserver

7. Open in browser:
   ```bash
   http://127.0.0.1:8000/

🧪 Modules (Highlights)
    Booking – schedule appointments
    Services – list all available services
    Users – profile management
    Admin – dashboard to view/manage bookings
    
🔮 Future Enhancements
    Pet accessories shop
    Email/SMS reminders
    Reviews and feedback system
    payment gateway
