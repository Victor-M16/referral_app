# Patient Referral System API Documentation

This API allows you to manage patient data, medical histories, diagnostics, equipment, referrals, and user authentication. Below is a detailed guide on how to interact with the API.

## Base URL

```
https://referralapp-production.up.railway.app/api/
```

---

## **Data Entry**

### Django Admin

You can enter some data to test using the django admin site, whose using the word admin for both username and password.

The admin site is available on this link:

```
https://referralapp-production.up.railway.app/admin/
```


## **Authentication**

### JWT Authentication

The API uses **JWT (JSON Web Token)** for authentication. To access any API endpoint that requires authentication, you must include the **JWT token** in the `Authorization` header.

### Getting the JWT Token

1. **Obtain a token** by sending a POST request to the **`/api/token/`** endpoint with your username and password:

    ```http
    POST /api/token/
    Content-Type: application/json

    {
        "username": "your_username",
        "password": "your_password"
    }
    ```

2. You will receive an access token and a refresh token:

    ```json
    {
        "access": "your_access_token",
        "refresh": "your_refresh_token"
    }
    ```

### Using the JWT Token

For each subsequent request, include the access token in the **`Authorization`** header as a Bearer token:

```http
Authorization: Bearer your_access_token
```

---

## **API Endpoints**

### 1. **Patients**

#### List all patients
- **GET** `/patients/`
- Returns a list of all patients.

#### Create a new patient
- **POST** `/patients/`
- Request body:

    ```json
    {
        "first_name": "Grace",
        "last_name": "Chiwaya",
        "dob": "1960-01-01",
        "gender": "Female",
        "contact_info": "+265123456789"
    }
    ```

#### Retrieve a patient by ID
- **GET** `/patients/{id}/`
- Replace `{id}` with the patient's ID to get specific details about that patient.

#### Update a patient's details
- **PUT** `/patients/{id}/`
- Request body:

    ```json
    {
        "first_name": "Grace",
        "last_name": "Chiwaya",
        "dob": "2016-01-01",
        "gender": "Female",
        "contact_info": "+265123456789"
    }
    ```

#### Delete a patient
- **DELETE** `/patients/{id}/`

---

### 2. **Medical History**

#### List all medical histories
- **GET** `/medical-history/`

#### Create a new medical history record
- **POST** `/medical-history/`
- Request body:

    ```json
    {
        "patient": 1,
        "condition": "Hypertension",
        "treatment": "Medication",
        "start_date": "2022-05-01",
        "end_date": null,
        "notes": "Ongoing treatment"
    }
    ```

#### Retrieve medical history by `patient_id`
- **GET** `/medical-history/?patient_id=1`
- Filters medical histories by `patient_id`.

#### Update a medical history record
- **PUT** `/medical-history/{id}/`
- Request body:

    ```json
    {
        "condition": "Diabetes",
        "treatment": "Insulin",
        "start_date": "2022-06-01",
        "end_date": null,
        "notes": "Regular monitoring"
    }
    ```

#### Delete a medical history record
- **DELETE** `/medical-history/{id}/`

---

### 3. **Diagnostics**

#### List all diagnostics
- **GET** `/diagnostics/`

#### Create a new diagnostic record
- **POST** `/diagnostics/`
- Request body:

    ```json
    {
        "patient": 1,
        "diagnostic_type": "Blood Test",
        "result": "Normal",
        "date_taken": "2022-05-01",
        "notes": "No issues"
    }
    ```

#### Retrieve a diagnostic record by ID
- **GET** `/diagnostics/{id}/`

#### Update a diagnostic record
- **PUT** `/diagnostics/{id}/`
- Request body:

    ```json
    {
        "result": "Abnormal",
        "notes": "Further tests required"
    }
    ```

#### Delete a diagnostic record
- **DELETE** `/diagnostics/{id}/`

---

### 4. **Equipment**

#### List all equipment
- **GET** `/equipment/`

#### Add new equipment to a hospital
- **POST** `/equipment/`
- Request body:

    ```json
    {
        "hospital": 1,
        "equipment_name": "MRI Machine",
        "description": "High resolution MRI scanner",
        "available": true
    }
    ```

#### Retrieve equipment by ID
- **GET** `/equipment/{id}/`

#### Update equipment details
- **PUT** `/equipment/{id}/`
- Request body:

    ```json
    {
        "description": "Updated MRI scanner with additional features"
    }
    ```

#### Delete equipment
- **DELETE** `/equipment/{id}/`

---

### 5. **Referrals**

#### List all referrals
- **GET** `/referrals/`

#### Create a new referral
- **POST** `/referrals/`
- Request body:

    ```json
    {
        "patient": 1,
        "referred_from": 1,
        "referred_to": 2,
        "referral_reason": "Specialized surgery required",
        "referral_date": "2022-05-01",
        "status": "Pending"
    }
    ```

#### Retrieve a referral by ID
- **GET** `/referrals/{id}/`

#### Update a referral
- **PUT** `/referrals/{id}/`
- Request body:

    ```json
    {
        "status": "Accepted"
    }
    ```

#### Delete a referral
- **DELETE** `/referrals/{id}/`

---

## **Filtering and Querying**

You can filter data using query parameters. For example, to list all medical histories for a specific patient, use:

```http
GET /medical-history/?patient=3
```

---


## **Error Handling**

The API will return standard HTTP status codes along with a JSON object for errors.

### Example Error Response:

```json
{
    "detail": "Not found."
}
```

---

## **Conclusion**

This API allows you to manage patients, medical histories, diagnostics, referrals, and more. Use JWT authentication to interact with endpoints that require it, and filter results using query parameters to narrow down results based on specific criteria.
