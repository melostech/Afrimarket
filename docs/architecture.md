# System Architecture

## Overview
Afrimarket uses a decoupled client-server architecture, separating the frontend presentation layer from the backend business logic and data storage. The communication between the frontend and backend happens exclusively through a RESTful API.

## Core Technologies

### 1. Frontend: React
React is responsible for the User Interface (UI) and User Experience (UX).
- **Role:** It runs in the user's web browser, rendering pages, handling user interactions (clicks, form submissions), and displaying data fetched from the backend.
- **Communication:** It makes HTTP requests (GET, POST, PUT, DELETE) to the Django REST API endpoints using `fetch` or a library like `axios` to send and receive JSON data.

### 2. Backend: Django & Django REST Framework (DRF)
Django serves as the core backend framework, handling the business logic, security, and data validation.
- **Django:** Provides the foundation, including the ORM (Object-Relational Mapper) to interact with the database, authentication mechanisms, and an admin panel.
- **Django REST Framework (DRF):** An extension for Django that makes it easy to build robust web APIs. It handles:
  - **Serializers:** Converting complex Django model instances into Python datatypes that can be easily rendered into JSON, and vice versa (validating incoming JSON data to create/update models).
  - **Views/ViewSets:** Defining the logic for what happens when a specific API endpoint is hit (e.g., querying the database, creating a new record).
  - **Authentication & Permissions:** Ensuring only authorized users can access specific endpoints.

### 3. Database: PostgreSQL
PostgreSQL is the primary relational database management system (RDBMS) for Afrimarket.
- **Role:** It stores all persistent data, including users, seller profiles, products, rental listings, orders, and payments.
- **Integration:** Django communicates with PostgreSQL using its ORM. We define our database structure using Python classes (Django Models), and Django translates these into SQL queries behind the scenes.

## System Flow

1. **Client Request:** A user interacts with the React frontend (e.g., clicks "View Products").
2. **API Call:** React sends an HTTP GET request to the backend endpoint (e.g., `/api/products/`).
3. **Routing:** Django receives the request and routes it to the appropriate DRF View based on the URL.
4. **Processing & DB Query:** The View uses the ORM to fetch the requested product data from PostgreSQL.
5. **Serialization:** The fetched data is passed to a Serializer, which converts it into a structured JSON format.
6. **API Response:** DRF sends an HTTP response containing the JSON data back to the React frontend.
7. **UI Update:** React receives the JSON data and updates the UI to display the products to the user.
