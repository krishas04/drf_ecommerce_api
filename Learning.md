# Learnings from this commit

**Date:** 25 Jan 2026

**Changes made:**
- Created necessary models for the project:
  - AbstractBaseModel
  - CustomUser
  - Profile
  - Product
  - Category
  - Cart, CartItem
  - Order, OrderItem

---

## Key Learnings

### 1️⃣ Django Models & Custom User
- **CustomUser** inherits from `AbstractUser` but can be left with `pass`.  
  - Allows adding fields later without breaking migrations.  
  - Declared in `settings.py` with `AUTH_USER_MODEL="account.CustomUser"` so Django uses it throughout the project.
- Using **`settings.AUTH_USER_MODEL`** in relationships (ForeignKey, OneToOneField) is **safer** than importing CustomUser directly.  
  - Prevents **circular import errors**.  

### 2️⃣ Organizing Models
- Models can be split into **packages** (`models/` folder) instead of one big `models.py`.  
- **`__init__.py`** must import models explicitly so Django can discover them.  

### 3️⃣ Django Admin
- Registering models in `admin.py` allows **viewing and managing models from the Django admin site**.  

### 4️⃣ Relationships
- **OneToOneField** → unique 1:1 relationship (e.g., Profile → CustomUser).  
- **ForeignKey** → many-to-one relationship (e.g., Order → User).  
- **ManyToManyField** → many-to-many relationship (e.g., Order → Product).  
  - Can use **`through` table** to add extra fields (e.g., quantity, price).  
- **`related_name`**:  
  - Allows reverse access (e.g., `user.orders.all()`).  
  - If omitted, Django defaults to `<model>_set`.  
  - Highly recommended for ManyToMany relationships for clarity.

### 5️⃣ Model Meta Options
- **`unique_together`** → ensures combination of fields is unique in the database.  
- **`verbose_name_plural`** → customize plural display in admin interface.  

### 6️⃣ Reusable Code
- **Core app** is used for **common reusable code** like `AbstractBaseModel` with `created_at` / `updated_at`.  

### 7️⃣ Model Utilities
- **@property decorator** → makes a method behave like a field/property.  
- **Choices** as a nested class (`TextChoices`) →  
  - Efficient for fields with limited options (e.g., Order status, YearInSchool)  
  - Provides human-readable names and easy-to-use constants.  

### 8️⃣ SQLite & Testing
- Learned to inspect data using **SQLite Explorer** in VS Code.  
- Understanding of how migrations create tables for models and relationships.  

---