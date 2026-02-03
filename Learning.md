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

---
**Date:** 31 Jan 2026
### 16. Concrete View Classes: ListCreateAPIView
- Used **ListCreateAPIView** instead of separate **ListAPIView** and **CreateAPIView** to support both **GET and POST** on the **same endpoint**, following REST principles. 
- The **serializer** was **modified** as for **post request**, **id** must not be kept. 
- Id is:
  - auto-generated by Django
  - should never be sent by client on POST

**Date:** 1 Feb 2026 
### 17. Method-based Permissions in DRF
- Learned how to handle **different permissions** for the **same endpoint** when it supports **multiple HTTP methods** (GET and POST).
- Used **ListCreateAPIView** and overrode **get_permissions()** to **dynamically assign permissions based on the request method**.
- Applied **AllowAny** for **GET requests** (public access) and restricted **POST requests** to admins using **IsAdminUser**.
- This approach avoids relying on a single global permission, which may not work correctly for mixed-access endpoints.

### 18. Using REST Client Extension in VS Code
- Learned to use the **REST Client** extension in VS Code to test APIs directly from the editor.
- Created request **files** with the **.http** extension to organize and store API requests.
- Can send GET, POST, and other HTTP requests directly from these .http files.
- Eliminates the need for external tools like Postman during development.
- Makes API testing faster and keeps request examples documented alongside the codebase.
- Especially useful during DRF development for quickly validating permissions, serializers, and responses.

### 19. JWT Authentication with SimpleJWT
- Learned to implement **JWT-based authentication** in Django REST Framework using **djangorestframework-simplejwt**.
- Configured JWTAuthentication in REST_FRAMEWORK **settings** alongside SessionAuthentication.
- Included **routes** for Simple JWT’s **TokenObtainPairView** and **TokenRefreshView** to handle token generation and refresh.
- Understood the flow of access and refresh tokens for secure API authentication.
- Used the **/token/** endpoint to obtain JWT tokens by sending username and password.
- Used the **/token/refresh/** endpoint to generate a new access token using a refresh token.
- Practiced testing JWT authentication directly from VS Code using REST Client **token.http** file.

**Date:** 2 Feb 2026 
### 20. Retrieve vs RetrieveUpdateDestroyAPIView
- `RetrieveAPIView` only supports **GET**
- `RetrieveUpdateDestroyAPIView` supports:
  - GET
  - PUT
  - PATCH
  - DELETE
- Useful when the same URL should handle read, update, and delete operations

### 21. ## Documentation Options in DRF
I learned that there are several ways to document APIs in Django REST Framework:

- **Browsable API**: DRF’s built-in feature that allows navigating and interacting with endpoints directly in a web interface. Useful for quick testing and exploration.
- **CoreAPI / Schema Generation**: Automatically generates schemas that describe API endpoints and their inputs/outputs. Forms the basis for automated documentation tools.
- **OpenAPI / Swagger**: Widely used standards for interactive API documentation, allowing developers to test endpoints directly from the docs.
- **Third-Party Tools**: Packages like `drf-yasg`, `django-rest-swagger`, and `drf-spectacular` extend schema generation and provide interactive documentation.

I also integrated **drf-spectacular** in my project, which is currently the most recommended third-party tool for generating OpenAPI 3 schemas(latest standard). It ensures that the API documentation is accurate, interactive,customizable and maintainable. It extracts maximum schema information automatically and is designed for modern API workflows.

**Date:** 3 Feb 2026 
## Filtering in Django REST Framework (DRF)
I learned how filtering works in Django REST Framework using `django-filter` by referring to the DRF documentation and Django Filter documentation.

### Key Concepts Learned

#### 1. django-filter Integration in DRF
- DRF supports filtering using the third-party package `django-filter`.
- Filtering can be enabled either by:
  - adding `DjangoFilterBackend` to a view’s `filter_backends`, or
  - configuring it globally in `REST_FRAMEWORK` settings.
- In this implementation, filtering was enabled using the **default filter backend configuration**, so it was not explicitly added in the view.

#### 2. FilterSet Class
- Custom filters are defined by creating a class that extends `django_filters.FilterSet`.
- The `FilterSet` class is used when more control is needed over **filter fields** and **lookup expressions**.
- A `FilterSet` must define an inner `Meta` class with:
  - `model`: the model to filter
  - `fields`: fields and allowed lookup expressions
  - `FilterSet` was used instead of `filterset_fields` because `filterset_fields` only supports basic filtering (exact match by default), whereas `FilterSet` allows explicit control over advanced lookups such as `icontains`, `lt`, `gt`, and `range`.

## Search Filtering and Per-View Filter Backends in DRF

I learned how DRF handles filtering backends at both global and view levels, and how adding filter backends in a view overrides the default configuration.

### Key Concepts Learned

#### 1. Default vs Per-View Filter Backends
- DRF allows filter backends to be configured globally using `REST_FRAMEWORK` settings.
- When `filter_backends` is defined inside a view, it **overrides** the globally configured default filter backends for that view only.
- Because of this override, any default backend (such as `DjangoFilterBackend`) must be explicitly re-added if it is still required.

#### 2. Combining django-filter with SearchFilter
- `DjangoFilterBackend` is used for structured, field-based filtering using query parameters.
- `SearchFilter` is used for text-based search across one or more fields.
- Both can be combined in a single view by listing them in `filter_backends`.

## Ordering in DRF API Views
#### 1. OrderingFilter
- `OrderingFilter` is a DRF filter backend that enables sorting of query results.
- It works seamlessly when included in the view's `filter_backends`.
- `ordering_fields` defines which model fields clients are allowed to sort by.
- Clients can sort ascending (default) or descending by prefixing the field with `-`.
- The `ordering` attribute sets a `default order` for query results if the client does not specify an ordering parameter.
