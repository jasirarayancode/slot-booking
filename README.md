# Turf Booking Website

This is a website project aimed at providing a platform for managing turf bookings. Users can view available turfs, book slots, make payments, and send complaints. The project is developed using HTML, CSS, JavaScript for the frontend, and Python with Django framework for the backend. MySQL Workbench is used for the database management.

## Features

- User authentication system
- Turf viewing and booking
- Slot management
- Payment integration
- Complaint submission

## Installation and Setup

To run this project locally, follow these steps:

1. Install Python, Django, and MySQL Workbench on your system.
2. Import the `reserva.sql` file to your MySQL database using MySQL Workbench.
3. Connect your database in the `settings.py` file of the Django project.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

4. Run the Django development server using the command `python manage.py runserver`.
5. Access the website in your browser at `http://localhost:8000`.

## Usage

1. **User Registration:** Users can register for an account on the website using their email address and password.
2. **View Turfs:** After logging in, users can view the list of available turfs along with their details such as location, facilities, and pricing.
3. **Book Turf:** Users can select a turf and book slots based on their preferred date and time.
4. **Make Payment:** Once the booking is confirmed, users can proceed to make payments securely through integrated payment gateways.
5. **Send Complaints:** Users can submit complaints or feedback regarding their experience using the website.

## Target Audience

This project is designed for individuals interested in coding and those who are looking to learn web development using Django framework. It can serve as an educational resource for understanding various concepts such as database management, user authentication, and payment integration in web applications.

## Contributing

Contributions to this project are welcome. If you have any suggestions, bug fixes, or new features to add, feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to adjust or expand upon any section further according to your project's needs.
