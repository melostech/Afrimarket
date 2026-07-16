# API Structure

## Overview
This document outlines the planned REST API endpoints for the Afrimarket platform. 

**Base URL:** `/api/`

---

## Authentication & User Management
Prefix: `/api/auth/` or `/api/users/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| POST | `/api/auth/register` | Register a new user | No |
| POST | `/api/auth/login` | Login and get JWT token | No |
| POST | `/api/auth/refresh` | Refresh JWT token | Yes |
| GET | `/api/users/me` | Get current user's profile | Yes |
| PUT | `/api/users/me` | Update current user's profile | Yes |

---

## Seller Profiles
Prefix: `/api/sellers/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| GET | `/api/sellers` | List all verified sellers | No |
| GET | `/api/sellers/{id}` | Get a specific seller's profile | No |
| POST | `/api/sellers/register` | Create a seller profile for current user | Yes |
| PUT | `/api/sellers/me` | Update current user's seller profile | Yes (Seller) |

---

## Categories
Prefix: `/api/categories/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| GET | `/api/categories` | List all categories | No |
| POST | `/api/categories` | Create a new category | Yes (Admin) |

---

## Products
Prefix: `/api/products/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| GET | `/api/products` | List/search products (with filters) | No |
| GET | `/api/products/{id}` | Get specific product details | No |
| POST | `/api/products` | Create a new product listing | Yes (Seller) |
| PUT | `/api/products/{id}` | Update a product listing | Yes (Seller owner) |
| DELETE | `/api/products/{id}` | Delete a product listing | Yes (Seller owner) |

---

## Rental Listings
Prefix: `/api/rentals/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| GET | `/api/rentals` | List/search rental listings | No |
| GET | `/api/rentals/{id}` | Get specific rental details | No |
| POST | `/api/rentals` | Create a new rental listing | Yes (Seller) |
| PUT | `/api/rentals/{id}` | Update a rental listing | Yes (Seller owner) |
| DELETE | `/api/rentals/{id}` | Delete a rental listing | Yes (Seller owner) |

---

## Orders
Prefix: `/api/orders/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| GET | `/api/orders` | List current user's orders | Yes |
| POST | `/api/orders` | Create a new order (Checkout) | Yes |
| GET | `/api/orders/{id}` | Get specific order details | Yes (Buyer/Seller/Admin) |
| PUT | `/api/orders/{id}/status` | Update order status | Yes (Seller/Admin) |

---

## Payments
Prefix: `/api/payments/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| POST | `/api/payments/contact-access`| Pay to access seller contact info | Yes |
| POST | `/api/payments/subscribe` | Pay for seller monthly subscription | Yes (Seller) |
| GET | `/api/payments/history` | View payment history | Yes |

---

## Subscriptions
Prefix: `/api/subscriptions/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| GET | `/api/subscriptions/plans` | List available subscription plans | No |
| GET | `/api/subscriptions/me` | View current subscription status | Yes (Seller) |

---

## Reviews
Prefix: `/api/reviews/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| GET | `/api/products/{id}/reviews`| Get all reviews for a product | No |
| POST | `/api/products/{id}/reviews`| Leave a review for a product | Yes |

---

## Notifications
Prefix: `/api/notifications/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| GET | `/api/notifications` | List user's notifications | Yes |
| PUT | `/api/notifications/{id}/read`| Mark a notification as read | Yes |
