# Afrimarket Backend

## Project Overview
Afrimarket is an online marketplace that connects buyers, sellers, and rental service providers. Developed by Melos Technologies, the platform allows users to discover products, purchase items, sell their products, and offer rental services in one centralized location while providing businesses with tools to manage their listings and grow their online presence.

## Tech Stack
- **Backend Framework:** Django
- **API Framework:** Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Frontend Integration:** React (Client-side)

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL
- Git

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Afrimarket
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables
Create a `.env` file in the project root and add the following configuration:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=afrimarket_db
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```

## Running the Project

1. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

3. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.

## Git Workflow
We follow a feature-branch workflow.
1. `main` branch is protected and contains production-ready code.
2. Create a new branch for every task: `git checkout -b feature/task-name` or `bugfix/issue-description`.
3. Commit your changes with clear, descriptive messages.
4. Push your branch and open a Pull Request (PR) against `main`.

## Contribution Guide
- Ensure your code follows PEP 8 standards.
- Write tests for new features where applicable.
- Document any new API endpoints or significant changes in the `docs/` folder.
- Wait for a code review and approval before merging your PR.