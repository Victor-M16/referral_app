### Project Structure Overview

The project, `referral_app`, contains two apps: `core` and `api`. Each app serves a specific purpose. The **`core`** app handles the core functionalities like data modeling and serialization, while the **`api`** app is responsible for exposing this functionality via an API.

Here's a breakdown of the structure:

```
referral_app/
│
├── core/            # Contains the main logic for handling data (models and serializers)
│   ├── models.py    # Defines the data structure (database tables)
│   ├── serializers.py  # Converts models to JSON or other formats and vice versa
│   └── ...          # Other files for the core logic of the project
│
├── api/             # Handles the API (URLs and viewsets)
│   ├── urls.py      # Maps URLs to specific viewsets or functionalities
│   ├── views.py     # Contains viewsets that manage how API actions (create, read, update, delete) are handled
│   └── ...          # Other files related to API functionality
│
├── referral_app/    # Main project settings and configuration
│   ├── settings.py  # Settings for the whole Django project (like database, installed apps, etc.)
│   ├── urls.py      # Main URL configuration that links to the 'api' URLs
│   └── ...          # Other project configuration files
│
└── manage.py        # Script to run Django commands (like running the server or migrations)
```

### Core Concepts and How They Work Together

1. **Models (`core/models.py`)**  
   Models are Python classes that represent database tables. For example, if you have a model called `Referral`, it defines the structure for storing referral-related data in the database. Each model is a "blueprint" for the data, and Django uses it to automatically create the necessary database tables.

   **Example**:
   ```python
    # Referral Model
    class Referral(models.Model):
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="referrals")
        referred_from = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="referrals_made")
        referred_to = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="referrals_received")
        referral_reason = models.TextField()  # Why the patient is being referred
        referral_date = models.DateField()
        status = models.CharField(max_length=20, choices=[
            ('Pending', 'Pending'),
            ('Accepted', 'Accepted'),
            ('Rejected', 'Rejected'),
        ], default='Pending')

        def __str__(self):
            return f'Referral of {self.patient.first_name} {self.patient.last_name} from {self.referred_from.name} to {self.referred_to.name}'
   ```

2. **Serializers (`core/serializers.py`)**  
   Serializers are used to convert the data from the models into a format that can be sent over the web, such as JSON. They also validate the incoming data from API requests before saving it to the database.

   **Example**:
   ```python
   from rest_framework import serializers
   from .models import Referral

   class ReferralSerializer(serializers.ModelSerializer):
       class Meta:
           model = Referral
           fields = '__all__'
   ```

   The `ReferralSerializer` converts data from the `Referral` model into JSON and validates data coming from requests before it’s saved.

3. **Viewsets (`api/viewsets.py`)**  
   Viewsets are like "controllers" in Django. They define how the API interacts with the data in the models. Viewsets manage actions like getting data (read), creating new entries, updating existing data, and deleting entries.

   **Example**:
   ```python
   from rest_framework import viewsets
   from core.models import Referral
   from core.serializers import ReferralSerializer

   class ReferralViewSet(viewsets.ModelViewSet):
       queryset = Referral.objects.all()
       serializer_class = ReferralSerializer
   ```

   The `ReferralViewSet` is responsible for handling the HTTP requests. When someone calls the API to get referral data, create a referral, etc., this viewset takes care of that interaction.

4. **URLs (`api/urls.py`)**  
   URLs define the paths for the API endpoints. For instance, `/api/referrals/` would be the URL for accessing the referral data through the API.

   **Example**:
   ```python
   from django.urls import path, include
   from rest_framework.routers import DefaultRouter
   from .viewsets import ReferralViewSet

   router = DefaultRouter()
   router.register(r'referrals', ReferralViewSet)

   urlpatterns = [
       path('', include(router.urls)),
   ]
   ```

   This file maps the `/referrals/` endpoint to the `ReferralViewSet`, so users can interact with the referral data via the API.

### How Everything Fits Together

- **Models (`core/models.py`)**: Define what kind of data you want to store (like referrals).
- **Serializers (`core/serializers.py`)**: Convert the model data into JSON for the API or validate incoming data.
- **Viewsets (`api/viewsets.py`)**: Handle how the API interacts with the models (e.g., listing all referrals, creating a new one, etc.).
- **URLs (`api/urls.py`)**: Define the paths that users or other systems use to interact with the API.

### Conclusion

- The **`core`** app focuses on handling the data: defining it with models and making it usable via serializers.
- The **`api`** app is responsible for the interaction side: exposing URLs, and handling requests through viewsets.


### Important Packages

1. **`rest_framework`**:
   - **Purpose**: This is the backbone of the API. The **Django REST Framework (DRF)** simplifies building APIs in Django by providing tools to create viewsets, serializers, and request handling out-of-the-box.
   - **Role in the Project**: In the project, **`rest_framework`** is crucial for:
     - Handling API requests and responses (like JSON).
     - Managing authentication, permissions, and routing (URLs).
     - Offering tools like `ModelViewSet` and `DefaultRouter` to make building APIs easier.
     - Serializing the data from the models (e.g., `ReferralSerializer`).
     - Defining reusable views (e.g., `ReferralViewSet`) for the referral app's functionality.
   
   Without DRF, you'd have to write a lot of low-level code to handle HTTP requests, validation, and responses manually.

2. **`rest_framework_jwt`**:
   - **Purpose**: **JWT (JSON Web Token)** authentication is a secure method to verify users trying to access the API. Instead of traditional sessions, JWT uses a token that is passed along with API requests to authenticate the user.
   - **Role in the Project**: This is important for protecting the API endpoints from unauthorized access. For example, only authenticated users can create, view, update, or delete referral records. 
     - When a user logs in, the API generates a token for them. This token is included in the headers of future API requests as proof that the user is authenticated.
     - `rest_framework_jwt` provides endpoints for token authentication, like `/api/token-auth/`, which returns the token when users log in.

   **Example of Token Authentication Flow**:
   1. User sends a login request with username/password to `/api/token-auth/`.
   2. Server verifies the credentials and returns a JWT token.
   3. User sends this token in the `Authorization` header (e.g., `Authorization: Bearer <token>`) with future API requests.
   4. The server checks this token to verify the user's identity for every request.

   This ensures that the referral system is secure and only authorized users can access it.

3. **`corsheaders`**:
   - **Purpose**: **CORS (Cross-Origin Resource Sharing)** is a mechanism that allows the API to be accessed from different domains or frontend applications. By default, web browsers block requests to the API from other domains for security reasons.
   - **Role in the Project**: In the project, **`corsheaders`** is important because:
     - the API may be consumed by web clients or mobile apps running on different domains.
     - For example, if the React Native mobile app wants to access the Django API, **CORS** must be enabled to allow cross-domain requests.
     - The `corsheaders` package ensures that the API is accessible from external domains while controlling which domains can access it (for security).
   
   In the settings, you’ll configure **allowed origins**, which specify which domains or IP addresses can send requests to the API.

   **Example Configuration**:
   ```python
   # settings.py
   CORS_ALLOWED_ORIGINS = [
       "http://localhost:3000",   # Allow frontend running on localhost
       "https://example-frontend.com"  # Allow production frontend
   ]

   # We used the one below because we are expecting requests from all kinds of clients 
   # since we are in development (IP addresses of the machines that the other teams are using)
   CORS_ALLOWED_ORIGINS = True
   ```

### How They All Work Together

- **`rest_framework`**:
  - Enables you to build and expose the API endpoints easily using viewsets and serializers.
  - Helps in defining how data (like referrals) should be returned in JSON format and how incoming data should be validated.
  
- **`rest_framework_jwt`**:
  - Adds an extra layer of security by ensuring that only authorized users can access the API.
  - Allows users to log in and authenticate via tokens instead of sessions, which is crucial for modern API-based architectures.
  
- **`corsheaders`**:
  - Ensures that clients like mobile apps or web frontends, which may be hosted on different domains, can securely access the API.
  - Prevents security issues caused by unauthorized domains making requests to the API.

### Final Project Structure Including These Packages

To give the team a more complete picture, here's how these packages fit into the project:

```
referral_app/
│
├── core/
│   ├── models.py          # Defines the data structure (e.g., Referral)
│   ├── serializers.py     # Converts models into JSON and validates incoming data
│   └── ...                # Other core logic
│
├── api/
│   ├── urls.py            # Maps URLs to specific views
│   ├── viewsets.py        # Handles API actions like create, read, update, delete
│   └── ...                # Other API-related logic
│
├── referral_app/
│   ├── settings.py        # Configures Django, including rest_framework, JWT, and corsheaders
│   ├── urls.py            # Main URL configuration that links to API URLs
│   └── ...                # Other project settings
│
├── manage.py              # Django command-line utility
└── requirements.txt       # Specifies all dependencies including rest_framework, rest_framework_jwt, and corsheaders
```

### Example Configuration in `settings.py`

```python
INSTALLED_APPS = [
    'rest_framework',      # Adds Django REST framework
    'rest_framework_jwt',  # Adds JWT authentication based on Django REST framework
    'corsheaders',         # Enables cross-origin requests
    'core',                # the core app
    'api',                 # the API app
]

# CORS settings
CORS_ALLOWED_ORIGINS = True

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # Might be needed for frontend
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    
    # uncomment if clients want pagination
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 1  # Number of items per page
}
```

### Conclusion

- **`rest_framework`** helps you easily build and manage the API.
- **`rest_framework_jwt`** ensures secure access to the API by using token-based authentication.
- **`corsheaders`** allows the API to be accessed by different domains, like mobile apps and web clients.

These tools work together to make the project secure, flexible, and accessible across platforms, which is essential for modern APIs.

