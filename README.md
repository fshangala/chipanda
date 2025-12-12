# 🏡 chipanda

**chipanda** is a modern, full-featured real estate platform built using **Django** and styled with **Tailwind CSS**. It allows users to list, search, and view properties available for rent or purchase.

## ✨ Features

  * **Property Management:** Define and manage properties with detailed fields (price, bedrooms, location, etc.).
  * **Agent Integration:** Associate listings with specific agents (users).
  * **Django Admin Interface:** Secure and comprehensive dashboard for content management.
  * **Modern Styling:** Utilizes Tailwind CSS for a utility-first, responsive, and maintainable frontend.
  * **Configuration:** Secure handling of secrets using `django-environ` and `.env` files.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

  * Python 3.10+
  * Node.js (for Tailwind CSS CLI)
  * A code editor (VS Code is recommended for its integrated debugging setup)

### Installation

Follow these steps to set up your development environment.

#### 1\. Clone the Repository

```bash
git clone <repository-url-here>
cd chipanda
```

#### 2\. Environment Setup

The project uses environment variables for security and configuration.

  * **Create Virtual Environment:**

    ```bash
    python -m venv venv
    ```

  * **Activate Virtual Environment:**

      * *Linux/macOS:* `source venv/bin/activate`
      * *Windows:* `.\venv\Scripts\activate`

  * **Create Configuration File:**

    ```bash
    cp .env-example .env
    ```

    **🛑 IMPORTANT:** Open the newly created `.env` file and replace the placeholder values (especially the `SECRET_KEY`) with unique, secure values.

  * **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    npm install # Install Node dependencies for Tailwind CSS
    ```

#### 3\. Database Setup

The project uses SQLite by default for development.

  * **Run Migrations:** Apply the database changes to create the necessary tables (including the `Property` model):
    ```bash
    python manage.py migrate
    ```
  * **Create Superuser:** Create an admin user to access the Django admin panel and create properties/agents:
    ```bash
    python manage.py createsuperuser
    ```

## ▶️ Running the Application (VS Code)

The project is configured with a `launch.json` file to simplify starting both the Django backend and the Tailwind CSS watcher simultaneously in VS Code.

1.  Open the **VS Code Debug/Run panel** (`Ctrl+Shift+D` or `Cmd+Shift+D`).
2.  Run both the **"Python Debugger: Django"** and the **"Tailwind CLI Watcher"** configurations.

The application will now be accessible at `http://127.0.0.1:8000/`.

-----

## 🛠️ Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend Framework** | Django | Web framework for business logic and data handling. |
| **Frontend Styling** | Tailwind CSS | Utility-first CSS framework for design. |
| **Configuration** | `django-environ` | Secure management of environment variables. |
| **Database (Dev)** | SQLite | Default local database. |

## 📂 Project Structure Overview

```
chipanda/
├── .env            # Environment variables (local secrets)
├── .env-example    # Configuration template
├── accounts/       # User/Agent management app
├── chipanda/       # Project configuration
├── home/           # Landing page app
├── listings/       # Core app for Property models, views, and templates
├── manage.py       # Django command script
└── requirements.txt
```

## 🧑‍💻 Contributing

... *(Instructions for contributing will go here)* ...