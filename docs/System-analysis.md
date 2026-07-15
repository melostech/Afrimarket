### Afrimarket Backend system analysis

## created by: Simret A.

## Project purpose
Afrimarket is an online marketplace that connects buyers, sellers, and rental service providers. The platform allows users to buy products, sell products, and offer rental services in one place while helping businesses manage their listings and customers.

### Main Users

#### Buyer
- Browse products
- Search and filter listings
- Purchase products
- Contact sellers

#### Seller
- Create and manage listings
- Sell products
- Offer rental services
- Manage inventory

#### Admin
- Manage users
- Manage categories
- Monitor the platform
- Manage subscriptions and payments

### The problem I think it will solve
Afrimarket solve the problem by providing one centralized marketplace where user can easily discover products and services.

### Business Model

Afrimarket generates revenue through:

- Monthly subscriptions paid by sellers.
- Contact access fees paid by buyers to view seller contact information.
- Future premium business features.

### Backend Modules

- Authentication
- User Management
- Seller Profiles
- Products
- Rental Listings
- Categories
- Orders
- Payments
- Subscriptions
- Reviews
- Notifications
- Admin

## Technologies

Backend Framework:
- Django
- Django REST Framework

Database:
- PostgreSQL

### Entities

*** User ***
- Full Name
- Email
- Password
- Phone Number
- Role
- Date Joined
- Profile Picture
- Is Active

*** Seller Profile ***
- User
- Business Name
- Business Description
- Rating
- Subscription
- Verified

*** Product ***
- Title
- Description
- Price
- Condition
- Category
- Seller
- Status
- Location
- Created At

*** Rental Listing ***
- Title
- Description
- Rental Price
- Seller
- Availability
- Location

*** Category ***
- Name
- Description

*** Order ***
- User
- Product
- Quantity
- Total Price
- Status
- Created At

*** Payment ***
- User
- Amount
- Payment Type
- Status
- Date

*** Subscription ***
- Seller
- Plan
- Start Date
- End Date
- Status

*** Review ***
- Buyer
- Product
- Rating
- Comment
- Created At

*** Notification ***
- User
- Title
- Message
- Is Read


Authentication
Can one user be both a buyer and a seller?
Does every seller have a user account?
Products
Can a product belong to multiple categories?
Can a seller edit a sold product?
Rentals
Can one rental listing have multiple bookings?
What happens if two people request the same rental?
Reviews
Can a buyer review the same product twice?
Can sellers review buyers?