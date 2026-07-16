# Database Design

## Overview
This document outlines the database schema for the Afrimarket backend. It is based on the initial system analysis and uses a relational structure (PostgreSQL).

## Entities and Relationships

### 1. User
The core authentication and identity model. We assume users can act as both buyers and sellers using the same base account.

**Fields:**
- `id` (Primary Key)
- `first_name` (String)
- `last_name` (String)
- `email` (String, Unique)
- `password` (Hashed String)
- `phone_number` (String)
- `role` (Enum: Buyer, Seller, Admin)
- `date_joined` (DateTime)
- `profile_picture` (URL/File Path)
- `is_active` (Boolean)

**Relationships:**
- **One-to-One** with `SellerProfile` (A user can have at most one seller profile).
- **One-to-Many** with `Order` (A user can place many orders).
- **One-to-Many** with `Payment` (A user can make many payments).
- **One-to-Many** with `Review` (A user can write many reviews).
- **One-to-Many** with `Notification` (A user can receive many notifications).

### 2. SellerProfile
Contains business-specific information for users who sell products or offer rentals.

**Fields:**
- `id` (Primary Key)
- `user_id` (Foreign Key -> User, Unique)
- `business_name` (String)
- `business_description` (Text)
- `rating` (Float)
- `is_verified` (Boolean)

**Relationships:**
- **One-to-One** with `User`.
- **One-to-Many** with `Product` (A seller can have many products).
- **One-to-Many** with `RentalListing` (A seller can have many rental listings).
- **One-to-Many** with `Subscription` (A seller can have subscription records).

### 3. Category
Used to organize products and rentals.

**Fields:**
- `id` (Primary Key)
- `name` (String, Unique)
- `description` (Text)

**Relationships:**
- **One-to-Many** (or Many-to-Many) with `Product`. Assuming One-to-Many for simplicity initially (A category contains many products, a product belongs to one primary category).

### 4. Product
Items available for purchase.

**Fields:**
- `id` (Primary Key)
- `seller_id` (Foreign Key -> SellerProfile)
- `category_id` (Foreign Key -> Category)
- `title` (String)
- `description` (Text)
- `price` (Decimal)
- `condition` (Enum: New, Used, etc.)
- `status` (Enum: Available, Reserved, Sold, Out of Stock, Expired)
- `location` (String)
- `created_at` (DateTime)
- `updated_at` (DateTime)

**Relationships:**
- **Many-to-One** with `SellerProfile`.
- **Many-to-One** with `Category`.
- **One-to-Many** with `Review` (A product can have many reviews).
- **One-to-Many** with `Order` (A product can be part of many orders - usually handled via an OrderItem junction table in complex systems, but assuming simple 1 product per order for now based on analysis).

### 5. RentalListing
Services or items available for rent.

**Fields:**
- `id` (Primary Key)
- `seller_id` (Foreign Key -> SellerProfile)
- `title` (String)
- `description` (Text)
- `rental_price` (Decimal, per day/hour)
- `availability_status` (Enum: Available, Rented, Unavailable)
- `location` (String)
- `created_at` (DateTime)

**Relationships:**
- **Many-to-One** with `SellerProfile`.

### 6. Order
Records of purchases made by buyers.

**Fields:**
- `id` (Primary Key)
- `buyer_id` (Foreign Key -> User)
- `product_id` (Foreign Key -> Product)
- `quantity` (Integer)
- `total_price` (Decimal)
- `status` (Enum: Pending, Completed, Cancelled)
- `created_at` (DateTime)

**Relationships:**
- **Many-to-One** with `User`.
- **Many-to-One** with `Product`.

### 7. Payment
Financial transactions (contact access fees, subscriptions).

**Fields:**
- `id` (Primary Key)
- `user_id` (Foreign Key -> User)
- `amount` (Decimal)
- `payment_type` (Enum: ContactAccess, Subscription)
- `status` (Enum: Pending, Successful, Failed)
- `date` (DateTime)

**Relationships:**
- **Many-to-One** with `User`.

### 8. Subscription
Records of seller subscription plans.

**Fields:**
- `id` (Primary Key)
- `seller_id` (Foreign Key -> SellerProfile)
- `plan_name` (String)
- `start_date` (DateTime)
- `end_date` (DateTime)
- `status` (Enum: Active, Expired, Cancelled)

**Relationships:**
- **Many-to-One** with `SellerProfile`.

### 9. Review
Feedback left by buyers on products.

**Fields:**
- `id` (Primary Key)
- `buyer_id` (Foreign Key -> User)
- `product_id` (Foreign Key -> Product)
- `rating` (Integer, 1-5)
- `comment` (Text)
- `created_at` (DateTime)

**Relationships:**
- **Many-to-One** with `User`.
- **Many-to-One** with `Product`.

### 10. Notification
System alerts for users.

**Fields:**
- `id` (Primary Key)
- `user_id` (Foreign Key -> User)
- `title` (String)
- `message` (Text)
- `is_read` (Boolean)
- `created_at` (DateTime)

**Relationships:**
- **Many-to-One** with `User`.
