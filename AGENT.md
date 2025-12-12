# Agent Instructions for `chipanda`

This document provides instructions for an AI development agent to understand and contribute to the `chipanda` project.

## 1\. Project Overview

`chipanda` is a web application built with the Django framework.

**The main goal of the application is to serve as a real estate platform where users can list, search, and view properties available for rent or purchase, complete with features like photos, detailed descriptions, and agent contact information.**

## 2\. Technology Stack

  * **Backend Framework:** Django (Preference: Django for backend/APIs)
  * **Programming Language:** Python
  * **Database:** SQLite (for development)
  * **Environment Management:** `django-environ` is used for managing environment variables from a `.env` file.
  * **Frontend Styling:** **Tailwind CSS CLI** is used for compiling styles.

## 3\. Project Structure

The project follows a standard Django layout and includes several core applications: `accounts`, `home`, and `listings`.

```
chipanda/
├── .env            # Environment variables (not committed to git)
├── .env-example    # Template for required environment variables
├── accounts/       # Manages user registration, login, and agent profiles
├── chipanda/       # Django project configuration directory
│   ├── settings.py # Main project settings
│   ├── urls.py     # Root URL configuration
│   └── ...
├── home/           # Handles the main landing page
├── listings/       # Core app for property models, views, and templates
├── db.sqlite3      # Development database
├── manage.py       # Django's command-line utility
└── requirements.txt
```

## 4\. Key Files

  * `chipanda/settings.py`: Contains all project settings, including database configuration, installed apps, middleware, and static file locations. **Note: Ensure `listings` and `accounts` are added to `INSTALLED_APPS`.**
  * `chipanda/urls.py`: The root URLconf. All app-specific URLs should be included from this file (e.g., `path('listings/', include('listings.urls'))`).
  * `manage.py`: The script used to execute Django management commands.
  * `requirements.txt`: This file lists all Python dependencies for the project. **Current dependencies include `Django` and `django-environ`.**
  * **`.env` and `.env-example`:** The `.env-example` serves as a template showing all required environment variables. **The actual `.env` file should be created from this template and is excluded from Git.**

## 5\. How to Run the Project (VS Code Debug)

1.  **Set up the environment:**

      * Create a virtual environment: `python -m venv venv`
      * Activate it: `source venv/bin/activate` (on Linux/macOS) or `.\venv\Scripts\activate` (on Windows).
      * **Set up environment variables:**
          * Copy the template file:
            ```bash
            cp .env-example .env
            ```
          * **EDIT the newly created `.env` file to replace placeholder values (e.g., defining a unique `SECRET_KEY`, setting `DEBUG=True`).**
      * Install dependencies: `pip install -r requirements.txt`
      * **Install Node Dependencies:** If needed for Tailwind CSS, ensure you run: `npm install`

2.  **Set up the database:**

      * Run migrations: `python manage.py migrate`

3.  **Run the development server (Using VS Code):**

      * **Open the VS Code Debug/Run panel (`Ctrl+Shift+D` or `Cmd+Shift+D`).**
      * **Run both the "Python Debugger: Django" and the "Tailwind CLI Watcher" configurations.**
      * The application will be available at `http://127.0.0.1:8000/`.

## 6\. Development Goals & Tasks

Here is a list of potential next steps for developing this project.

  * [X] **Create a `requirements.txt` file:** List all current and future dependencies.
  * [X] **Create core apps:** `accounts`, `home`, and `listings` apps have been created.
  * [ ] **Define Property Model:** The `Property` model has been defined in `listings/models.py`. **Migrations need to be made and applied.**
  * [ ] **Set up Admin Interface:** The `Property` model has been registered in `listings/admin.py`.
  * [ ] **Create Views for Listings:** Implement the business logic in `listings/views.py` for a list view (index) and a detail view of properties.
  * [ ] **Configure URLs:** Add URL patterns for the `listings` app in `listings/urls.py` and include them in the main `chipanda/urls.py`.
  * [ ] **Build Templates:** Create initial HTML templates (e.g., `listings/index.html` and `listings/detail.html`) to display the property data.
  * [ ] **Set up Static Files:** Configure a `static` directory for CSS, JavaScript, and images.
  * [ ] **Develop User Authentication:** Complete the views and templates for the `accounts` app (login, register, logout).

