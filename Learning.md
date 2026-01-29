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

### 1. Django Models & Custom User
- **CustomUser** inherits from `AbstractUser` but can be left with `pass`.  
  - Allows adding fields later without breaking migrations.  
  - Declared in `settings.py` with `AUTH_USER_MODEL="account.CustomUser"` so Django uses it throughout the project.
- Using **`settings.AUTH_USER_MODEL`** in relationships (ForeignKey, OneToOneField) is **safer** than importing CustomUser directly.  
  - Prevents **circular import errors**.  

### 2. Organizing Models
- Models can be split into **packages** (`models/` folder) instead of one big `models.py`.  
- **`__init__.py`** must import models explicitly so Django can discover them.  

### 3. Django Admin
- Registering models in `admin.py` allows **viewing and managing models from the Django admin site**.  

### 4. Relationships
- **OneToOneField** → unique 1:1 relationship (e.g., Profile → CustomUser).  
- **ForeignKey** → many-to-one relationship (e.g., Order → User).  
- **ManyToManyField** → many-to-many relationship (e.g., Order → Product).  
  - Can use **`through` table** to add extra fields (e.g., quantity, price).  
- **`related_name`**:  
  - Allows reverse access (e.g., `user.orders.all()`).  
  - If omitted, Django defaults to `<model>_set`.  
  - Highly recommended for ManyToMany relationships for clarity.

### 5. Model Meta Options
- **`unique_together`** → ensures combination of fields is unique in the database.  
- **`verbose_name_plural`** → customize plural display in admin interface.  

### 6. Reusable Code
- **Core app** is used for **common reusable code** like `AbstractBaseModel` with `created_at` / `updated_at`.  

### 7. Model Utilities
- **@property decorator** → makes a method behave like a field/property.  
- **Choices** as a nested class (`TextChoices`) →  
  - Efficient for fields with limited options (e.g., Order status, YearInSchool)  
  - Provides human-readable names and easy-to-use constants.  

### 8. SQLite & Testing
- Learned to inspect data using **SQLite Explorer** in VS Code.  
- Understanding of how migrations create tables for models and relationships.  

---
**Date:** 26 Jan 2026

### 9. Django Rest Framework (DRF) Basics
- **Serializers**: Learned how to convert complex model instances into JSON data.
- **Nested Serializers**: Including one serializer inside another (e.g., ProfileSerializer inside UserSerializer) to -  show related data in a single API response.
- **SerializerMethodField**: Used for logic-based fields that aren't in the database, like calculating a total_price or subtotal on the fly.
- The **source argument**: Used to access nested attributes (e.g., source='product.name') directly in a flat serializer.


### 10. API Views & Folder Structure
- **@api_view** decorator: Used to transform standard Python functions into DRF-ready views that handle GET/POST requests and return Response objects.
- **Modular Folder Structure**: Organizing serializers/, views/, and urls/ into separate folders within each app makes the project scalable and easier to navigate.
- **URL Path Converters**: Using <int:pk> for standard IDs and <uuid:pk> for UUIDs (like in the Cart and Order models) to ensure the API routes correctly identify specific resources.

---
**Date:** 28 Jan 2026

### 11. Composite / Aggregated API Responses
- Learned that an API does not have to represent a **single model**.
- A **Composite API response** combines:
  - **model data** (e.g., list of products)
  - **metadata** (e.g., total count)
  - **computed values** (e.g., max_price, min_price)
- This pattern is **frontend-driven**, not **database-driven**.
- Reduces multiple API calls
- Improves performance and UX
- Implemented using **non-model serializers** (**serializers.Serializer**) to shape custom responses.

### 12. Non-Model Serializers (Custom Response Serializers)
- A Non-Model Serializer (serializers.Serializer) is used when:
  - the API response does not directly map to a single Django model
  - the response contains **computed, aggregated, or custom fields**
- They allow the API to return **information**, not just **raw records**.

### 13. Query Profiling with Silk
- Integrated **Django Silk** to **profile**(the process of analyzing code execution to understand performance characteristics like execution time, query count, memory usage) SQL queries per endpoint.
- Identified redundant queries.
- Used Silk’s breakdown to pinpoint slow queries and excessive joins.

### 14. Optimizing with select_related and prefetch_related
- Applied **select_related** for **single-valued relationships(ForeignKey, OneToOneField)** to reduce joins.
- Used **prefetch_related** for **multi-valued relationships(ManyToManyField, reverse ForeignKey)** to batch-fetch related objects.
- Switched to **Prefetch objects** for fine-grained control:
- Reduced query count from 10+ to 3–4 per endpoint.
- Improved response time and memory usage by avoiding repeated DB hits.

---
**Date:** 29 Jan 2026

### 15. Function-Based Views (FBV) → Class-Based Views (CBV) with DRF Generics
- Learned to refactor simple **function-based views** into **class-based views** using:
  - **generics.ListAPIView**
  - **generics.RetrieveAPIView**
- Understood that **generic CBVs** are best suited for standard **CRUD patterns**:
  - **ListAPIView** → listing collections
  - **RetrieveAPIView** → fetching a single object
- Learned that behavior remains unchanged when refactoring FBV → CBV if:
  - queryset
  - serializer
  - permissions
  are preserved correctly.