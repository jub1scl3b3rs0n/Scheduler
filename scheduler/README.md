# Online Appointment Booking System

This project is a full-stack Django-based web application that allows users to register as either **clients** or **service providers**, facilitating a simple and efficient appointment scheduling experience. Clients can browse service providers, check their availability, and book appointments. Service providers can configure their available days and times, manage incoming booking requests, and update appointment statuses directly from a personal dashboard.

The application includes essential features such as user authentication, role-specific dashboards, dynamic time slot rendering with JavaScript, and responsive design with CSS. It is a practical solution that could serve freelancers, consultants, tutors, or any professionals who offer time-based services.

---

## Distinctiveness and Complexity

### Distinctiveness

This project goes beyond the scope of the prior CS50W assignments by introducing:
- **Multiple user roles** with customized behaviors and permissions.
- A scheduling logic that integrates both provider availability and booked appointments to avoid conflicts.
- Dynamic client-side interactivity (JavaScript) that enhances the user experience.
- A real-world use case requiring thoughtful design for UI, UX, and backend logic.

Unlike CS50W’s earlier projects, which mostly handled static content or simple interactions (like a social network or auction listings), this project tackles a more domain-specific problem involving time-sensitive booking and resource allocation.

### Complexity

Key elements that demonstrate complexity include:
- **Availability Logic:** Service providers define the days of the week and time slots they're available. The system calculates which time slots remain open based on existing appointments.
- **JavaScript Integration:** The appointment form dynamically fetches available time slots from the backend without requiring a page reload. This is accomplished using the Fetch API and JSON responses.
- **Custom Validation:** The backend ensures users cannot double-book a time slot or book outside of a provider’s available hours.
- **Role-specific Dashboards:** Providers and clients see different views based on their roles. Providers see received bookings and can update statuses; clients see their upcoming appointments.
- **Responsive UI:** The design is made to work well across different screen sizes using custom CSS and media queries.
- **Security:** Views are protected with `@login_required` decorators, and the application respects access control boundaries between clients and providers.

---

## File Structure

project/
├── core/
│ ├── migrations/
│ ├── static/
│ │ └── core/
│ │   └── styles.css # Custom styling for the entire app
│ ├── templates/
│ │ └── core/
│ │   ├── base.html # Common layout
│ │   ├── book.html # Appointment booking form
│ │   ├── dashboard_client.html # Client dashboard
│ │   ├── dashboard_provider.html # Provider dashboard
│ │   ├── edit_availability.html # Edit provider availability
│ │   ├── index.html # Home page
│ │   ├── login.html # Login form
│ │   ├── provider_detail.html # Provider details
│ │   ├── provider_list.html # Provider list name
│ │   ├── register.html # Registration form
│ │   └── search.html # Search results
│ ├── admin.py
│ ├── apps.py
│ └── forms.py # (Optional) Django forms for cleaner handling
│ ├── models.py # ServiceProvider, Appointment, Availability
│ ├── tests.py
│ ├── urls.py # Route definitions
│ ├── views.py # Application logic
├── scheduler/
│ ├── urls.py # Root URL dispatcher
│ ├──wsgi.py / asgi.py
│ ├──urls.py / urls.py
│ └── settings.py # Django settings (including static and media)
├── manage.py
└── README.md

## How to Run the Application

1. **Clone the repository**
# Bash
    git clone https://github.com/jub1scl3b3rs0n/Scheduler.git
    cd scheduler
    python -m venv venv
    source venv/bin/activate  # or `venv\Scripts\activate` on Windows
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser #optional
    python manage.py runserver

# Open your Browser (Opera, Chrome, Edge, FireFox, Safari)
    Go to http://127.0.0.1:8000/ to use the app locally.
