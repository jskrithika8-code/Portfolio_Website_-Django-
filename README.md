### Portfolio Website (Django)

Intern ID: CITS5313

Full Name: J.S.KRITHIKA

No. of Weeks: 4 Weeks

Project Name: Personal Portfolio Website  

Project Scope: A fully functional personal portfolio built with Django that showcases projects, skills, and an about section, along with a working contact form that saves visitor messages to a database.

---

## Introduction

This is a Python/Django-based personal portfolio website for Krithika, a Python developer based in Chennai, India. The site presents her projects, technical skills, and background in a clean, responsive layout, and allows visitors to send messages directly through a contact form.

---

## Features

- 🏠 **Home Page** – Hero section with name, role, and CTA buttons
- 🗂️ **Projects Showcase** – Displays personal projects with title, description, and tech stack
- 🛠️ **Skills Section** – Visual listing of technologies used
- 👩‍💻 **About Page** – Personal introduction and background
- 📬 **Contact Form** – Saves visitor messages (name, email, message) to SQLite database
- ✅ **Success Feedback** – Flash message shown after form submission
- 📱 **Responsive Design** – Clean CSS with custom styling

---

## Pages

| Page    | URL        | Description                          |
|---------|------------|--------------------------------------|
| Home    | `/`        | Projects grid and skills section     |
| About   | `/about/`  | Personal bio and background          |
| Contact | `/contact/`| Contact form with database storage   |

---

## Technologies Used

| Layer     | Technology          |
|-----------|---------------------|
| Backend   | Python, Django      |
| Frontend  | HTML, CSS           |
| Database  | SQLite              |
| Forms     | Django ModelForms   |
| Admin     | Django Admin Panel  |

---

## How It Works

1. User visits the home page and views projects and skills
2. User navigates to the About page to learn more
3. User fills in the Contact form (name, email, message)
4. Form is validated using Django's ModelForm
5. Valid messages are saved to the SQLite database via the `Contact` model
6. A success message is shown to the user after submission
7. Messages can be viewed in the Django Admin panel

---

## Projects Showcased

| Project             | Description                                | Tech               |
|---------------------|--------------------------------------------|--------------------|
| Weather CLI         | CLI weather app using Open-Meteo API       | Python             |
| Expense Tracker     | Track expenses with CSV & JSON storage     | Python, Tkinter    |
| File Organizer      | Auto-organizes files into category folders | Python             |
| Portfolio Website   | This portfolio site                        | Python, Django     |

---

## System Requirements

- Python 3.x
- Django 4.x or above
- Any modern web browser

---

## Conclusion

This portfolio website demonstrates full-stack Django development — from URL routing and views to model-based forms and database storage — all presented through a clean, responsive UI. It serves as both a personal showcase and a practical example of building real-world Django applications.
