# Chipanda Real Estate Platform

`chipanda` is a web application built with the Django framework to serve as a real estate platform. It allows agents to list properties for rent or sale, and public users to browse and view these listings.

## Features

*   **Property Listings:** Agents can create and manage property listings through the Django admin.
*   **Multiple Images:** Each property can have multiple images.
*   **Agent Authentication:** A dedicated registration page allows new agents to create staff accounts.
*   **Public Views:** Anyone can view the list of properties and their details without an account.
*   **Styled with Tailwind CSS:** The frontend is styled using Tailwind CSS for a modern look and feel.

## Technology Stack

*   **Backend:** Django
*   **Database:** SQLite (for development)
*   **Frontend:** Tailwind CSS
*   **Environment Variables:** `django-environ`

## Project Structure

```
chipanda/
├── .env
├── .env-example
├── accounts/       # User registration and authentication
├── chipanda/       # Project configuration & global templates
├── listings/       # Core app for property listings
├── media/          # User-uploaded files (e.g., property photos)
├── static/         # Compiled CSS
├── manage.py
└── requirements.txt
```

## Getting Started

Follow these steps to set up and run the project locally.

### 1. Prerequisites

*   Python 3.x
*   Node.js and npm (for Tailwind CSS)

### 2. Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd chipanda
    ```

2.  **Set up a Python virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Python and Node.js dependencies:**
    ```bash
    pip install -r requirements.txt
    npm install
    ```

4.  **Configure environment variables:**
    ```bash
    cp .env-example .env
    ```
    *Open the `.env` file and generate a new `SECRET_KEY`.*

5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

### 3. Running the Project

You need to run two processes simultaneously: the Django development server and the Tailwind CSS watcher.

1.  **Run the Tailwind CSS watcher:**
    ```bash
    npm run watch
    ```

2.  **In a separate terminal, run the Django server:**
    ```bash
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.

*   **Property Listings:** http://127.0.0.1:8000/listings/
*   **Agent Registration:** http://127.0.0.1:8000/accounts/register/
*   **Admin Login:** http://127.0.0.1:8000/admin/