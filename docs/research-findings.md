# Research Findings

This document summarizes research on key technologies and best practices required for the Afrimarket backend.

## 1. JSON Web Tokens (JWT)

**What is it?**
JWT is an open standard for securely transmitting information between parties as a JSON object. It is widely used for authentication and authorization.

**How it works in our architecture:**
1. A user logs in with their credentials (email/password).
2. The Django backend verifies the credentials and, if valid, generates a JWT.
3. This JWT is sent back to the React frontend.
4. The React frontend stores the JWT (usually in memory or secure cookies) and includes it in the `Authorization` header (`Bearer <token>`) of subsequent requests.
5. Django validates the token on protected routes to identify the user without needing to look up a session in the database.

**Why use it?**
- **Stateless:** The server doesn't need to keep a record of logged-in users, making the backend easier to scale.
- **Decoupled:** Works perfectly with separated frontend (React) and backend (Django) architectures.

## 2. Cross-Origin Resource Sharing (CORS)

**Why we need CORS:**
By default, web browsers enforce a "Same-Origin Policy," which prevents a frontend running on one domain (e.g., `http://localhost:3000` for React) from making API requests to a backend on a different domain (e.g., `http://localhost:8000` for Django). Since our architecture separates the frontend and backend, we will hit this security restriction.

**How React will communicate with Django:**
We need to configure Django to explicitly allow requests coming from the React application's URL. This is done using the `django-cors-headers` package.

**Recommended Configuration:**
1. Install `django-cors-headers`.
2. Add it to `INSTALLED_APPS` and `MIDDLEWARE` in `settings.py`.
3. Configure `CORS_ALLOWED_ORIGINS` to include the React app's URL during development (and the production domain later).

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

## 3. Django Logging

**Why it matters:**
Logging is crucial for debugging errors, tracking user activity, and monitoring the health of the application, especially in production where we don't have access to the standard console output.

**Logging Configuration in Django:**
Django uses Python's built-in `logging` module. We configure it in `settings.py` via the `LOGGING` dictionary.

- **Error Logging:** We should configure a handler to write `ERROR` and `CRITICAL` level logs to a file (e.g., `errors.log`).
- **Debug Logging:** During development, we can set the log level to `DEBUG` to see detailed information about SQL queries, request routing, etc.

**Recommended approach:**
Create separate formatters and handlers. Use a standard format `[Time] [Level] [Message]` to make logs easily searchable.

## 4. DRF Best Practices

**Serializers:**
- Use `ModelSerializer` when your API closely maps to a database model. It automatically generates fields and validators based on the model.
- Keep serializers focused on data translation. Move complex business logic into services or model methods, not the serializer's `create` or `update` methods unless absolutely necessary.

**APIViews vs ViewSets:**
- **APIView:** Use this when you need fine-grained control over a specific endpoint that doesn't map neatly to standard CRUD operations.
- **ViewSets (and ModelViewSets):** Use these for standard CRUD operations on models. They combine the logic for multiple endpoints (e.g., list, retrieve, create, update, delete) into a single class, reducing boilerplate code. *Recommendation: Use ModelViewSets for standard entities like Products and Rentals.*

**Permissions:**
- DRF provides built-in permissions like `IsAuthenticated`, `IsAdminUser`, and `AllowAny`.
- Always default to secure settings (e.g., require authentication globally) and explicitly open up specific views (like registration) using `permission_classes = [AllowAny]`.
- Create custom permissions for complex logic (e.g., `IsOwnerOrReadOnly` to ensure only a seller can edit their product).

**Pagination:**
- Essential for endpoints that return lists of objects (like `/api/products`). It prevents the server from sending too much data at once, which can crash the client and slow down the database.
- Configure default pagination classes in `settings.py` (e.g., `PageNumberPagination` or `LimitOffsetPagination`).

**Filtering:**
- Use `django-filter` to allow the frontend to easily query data (e.g., `/api/products?category=electronics&min_price=100`). This pushes the filtering logic to the database rather than fetching everything and filtering in Python.
