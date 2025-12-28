# Agent Instructions for `chipanda`

This document provides instructions for an AI development agent to understand and contribute to the `chipanda` project.

## 1. Project Overview

`chipanda` is a real estate platform built with Django. The primary goal is to provide a portal for agents to manage property listings and for users to search/view properties in Zambia.

## 2. Technology Stack

* **Backend Framework:** Django (Python)
* **Database:** SQLite (Development)
* **Environment Management:** `django-environ`
* **Frontend Styling:** Tailwind CSS CLI

## 3. Project Structure

The project follows a modular Django layout. The `chipanda/` folder serves as both the project configuration directory and a core app for global overrides.

```text
chipanda/
├── .env 
├── accounts/       # User/Agent management (Custom User models)
├── chipanda/       # PROJECT CORE & GLOBAL LOGIC
│   ├── admin.py    # Custom AdminSite class definition
│   ├── apps.py     # Admin monkeypatching & AppConfig
│   ├── templates/  # Global templates (base.html, admin/ overrides)
│   ├── settings.py 
│   └── urls.py 
├── home/           # Landing page logic
├── listings/       # Property models, views, and management
├── manage.py
└── requirements.txt

```

## 4. Key Architectural Patterns

### A. Custom Admin Implementation (The "Monkeypatch")

To avoid `ImproperlyConfigured` and `RuntimeError` (related to `LogEntry`), we do not replace the `admin` app in `INSTALLED_APPS`. Instead, we use a global injection strategy:

1. **`chipanda/admin.py`**: Defines `ChipandaAdminSite(admin.AdminSite)`. It overrides `get_urls()` to prepend custom paths like `my-profile/`.
2. **`chipanda/apps.py`**: The `ready()` method performs a class-level monkeypatch:
* `admin.site.__class__ = ChipandaAdminSite`
* This ensures all apps (including 3rd party) use our custom logic.



### B. Template Priority

**`chipanda` must be the first item in `INSTALLED_APPS`.** Django processes templates in the order apps are listed. By placing `chipanda` first, our file at `chipanda/templates/admin/base_site.html` overrides the default Django admin header, allowing us to inject custom navigation links.

## 5. Development Guidelines

* **Admin Customization:** To add global admin features, modify `ChipandaAdminSite` in `chipanda/admin.py`.
* **Model Registration:** Use standard decorators `@admin.register(Model)`. The monkeypatch ensures they register to the custom site automatically.
* **Custom Admin Views:** Always use `self.admin_view(View.as_view())` in `get_urls` to ensure the view inherits admin permissions and styling.

## 6. How to Run the Project

1. **Environment Setup:**
* `python -m venv venv` && `source venv/bin/activate`
* `pip install -r requirements.txt`
* `cp .env-example .env` (Update `SECRET_KEY`).
* `npm install` (For Tailwind CSS).


2. **Database:**
* `python manage.py migrate`


3. **Execution (VS Code):**
* Run **"Python Debugger: Django"** and **"Tailwind CLI Watcher"** simultaneously from the Run/Debug panel.



## 7. Current Progress Tracking

* [X] **Core Apps:** `accounts`, `home`, and `listings` initialized.
* [X] **Property Model:** Implemented with province/city fields and multi-image support.
* [X] **Custom Admin Site:** `ChipandaAdminSite` implemented via `apps.py` monkeypatching.
* [X] **Admin UI:** Custom branding and "View Profile" link injected into the admin header.
* [X] **Authentication:** Agent registration (auto-staff) and login/logout flows complete.
* [X] **Home Infrastructure:** `home` app template path structured at `home/templates/home/index.html`.
* [X] **Landing Page Development:** Implemented Hero section, search form, and featured listings grid using Tailwind CSS.
* [X] **Navigation:** Integrated responsive navbar with dynamic "Dashboard" and "Logout" (POST) functionality.
* [ ] **Frontend Search Logic:** Connect the home page search form to the backend filtering in `listings/views.py`. (⚡ Current Focus)
* [ ] **Property Detail View:** Build the template to display specific details like `toilet_type` and `water_onsite`.
* [ ] **Agent Profile Logic:** Build out the `AdminProfileView` and performance dashboard in the admin panel.