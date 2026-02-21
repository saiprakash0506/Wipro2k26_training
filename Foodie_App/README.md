<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Playfair+Display&weight=700&size=26&pause=1000&color=E6AA3C&center=true&vCenter=true&width=640&lines=🍽️+Foodie+App+—+REST+API;Flask+%7C+Pytest+%7C+Robot+Framework;18+Endpoints+%7C+Layered+Architecture" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Pytest](https://img.shields.io/badge/Pytest-7.0+-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![Robot Framework](https://img.shields.io/badge/Robot_Framework-6.0+-E00000?style=for-the-badge)](https://robotframework.org)
[![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://postman.com)

<br/>

> **A complete RESTful backend application** built with Python Flask, featuring comprehensive automation testing using Pytest and Robot Framework. Demonstrates REST API best practices, input validation, layered architecture, and enterprise-grade automated testing.

<br/>

![Endpoints](https://img.shields.io/badge/API_Endpoints-18-E6AA3C?style=flat-square)
![Modules](https://img.shields.io/badge/Modules-5-7AB87A?style=flat-square)
![Frameworks](https://img.shields.io/badge/Test_Frameworks-2-D4521A?style=flat-square)
![Architecture](https://img.shields.io/badge/Architecture-Layered-6DB3F2?style=flat-square)

<br/>

[📦 Modules](#-feature-modules) · [🔌 Endpoints](#-api-endpoints) · [🏗 Architecture](#-architecture) · [💻 Setup](#-installation) · [🧪 Testing](#-testing) · [📊 Reports](#-reports)

---

</div>

## 📋 Table of Contents

- [Overview](#-overview)
- [Technology Stack](#-technology-stack)
- [Feature Modules](#-feature-modules)
- [API Endpoints](#-api-endpoints)
- [REST Principles](#-rest-principles-followed)
- [Input Validation](#-input-validation)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Running the Application](#-running-the-application)
- [Testing](#-testing)
- [API Response Format](#-api-response-format)
- [Reports](#-reports)
- [Project Status](#-project-status)
- [Learning Outcomes](#-learning-outcomes)

---

## 🧩 Overview

**Foodie App** is a production-ready REST API backend that simulates a real-world food delivery and restaurant management platform. It exposes **18 clean RESTful endpoints** across 5 functional modules — Restaurant, Dish, User, Admin, and Order.

The project is built on a **layered architecture** (Routes → Services → Models) ensuring clear separation of concerns, and is validated end-to-end with both **Pytest** (HTTP-level automated testing) and **Robot Framework** (keyword-driven integration tests).

**Project Highlights:**

- 18 fully implemented REST API endpoints
- 5 core business modules with complete CRUD operations
- Full input validation with descriptive error messages
- Consistent JSON request/response contract
- Dual automated test frameworks with HTML reports
- Industry-standard layered architecture

---

## 🚀 Technology Stack

| Layer                    | Technology                           | Purpose                          |
| ------------------------ | ------------------------------------ | -------------------------------- |
| **Backend Framework**    | Python Flask 2.0+                    | REST API server                  |
| **Language**             | Python 3.8+                          | Core language                    |
| **Manual Testing**       | Postman                              | Manual endpoint verification     |
| **Automation 1**         | Pytest 7.0+                          | HTTP-level automated tests       |
| **Automation 2**         | Robot Framework 6.0+                 | Keyword-driven integration tests |
| **HTTP Client (Pytest)** | `requests`                           | HTTP calls in test cases         |
| **HTTP Client (RF)**     | `RequestsLibrary`                    | HTTP calls in Robot tests        |
| **Validation**           | `jsonschema`                         | Response schema validation       |
| **Data Format**          | JSON                                 | Request / response format        |
| **Architecture Pattern** | Layered (Routes → Services → Models) | Separation of concerns           |

---

## 📦 Feature Modules

### 🏪 1. Restaurant Module

| Feature                     | Status      |
| --------------------------- | ----------- |
| Register new restaurant     | ✅ Complete |
| Update restaurant details   | ✅ Complete |
| Disable restaurant          | ✅ Complete |
| View restaurant information | ✅ Complete |

### 🍜 2. Dish Module

| Feature                            | Status      |
| ---------------------------------- | ----------- |
| Add new dish                       | ✅ Complete |
| Update dish details                | ✅ Complete |
| Enable / Disable dish availability | ✅ Complete |
| Delete dish                        | ✅ Complete |

### 🛡️ 3. Admin Module

| Feature                          | Status      |
| -------------------------------- | ----------- |
| Approve restaurant registrations | ✅ Complete |
| Disable restaurant operations    | ✅ Complete |
| View customer feedback           | ✅ Complete |
| View all orders                  | ✅ Complete |

### 👤 4. User Module

| Feature                  | Status      |
| ------------------------ | ----------- |
| User registration        | ✅ Complete |
| Search restaurants       | ✅ Complete |
| Place orders             | ✅ Complete |
| Submit ratings & reviews | ✅ Complete |

### 📦 5. Order Module

| Feature                   | Status      |
| ------------------------- | ----------- |
| View orders by restaurant | ✅ Complete |
| View orders by user       | ✅ Complete |

---

## 🔌 API Endpoints

> **Base URL:** `http://localhost:5000`
> **Total Endpoints: 18**

### 🏪 Restaurant APIs

```
POST    /api/restaurants                         # Register new restaurant
PUT     /api/restaurants/{id}                    # Update restaurant details
DELETE  /api/restaurants/{id}                    # Disable restaurant
GET     /api/restaurants/{id}                    # Get restaurant info
```

### 🍜 Dish APIs

```
POST    /api/dishes                              # Add new dish
PUT     /api/dishes/{id}                         # Update dish
PATCH   /api/dishes/{id}/toggle                  # Enable / Disable availability
DELETE  /api/dishes/{id}                         # Delete dish
```

### 👤 User APIs

```
POST    /api/users/register                      # Register user
GET     /api/restaurants/search?q={query}        # Search restaurants
POST    /api/orders                              # Place order
POST    /api/ratings                             # Submit rating & review
```

### 🛡️ Admin APIs

```
PUT     /api/admin/restaurants/{id}/approve      # Approve restaurant
DELETE  /api/admin/restaurants/{id}              # Disable restaurant
GET     /api/admin/feedback                      # View all feedback
GET     /api/admin/orders                        # View all orders
```

### 📦 Order APIs

```
GET     /api/orders/restaurant/{id}              # Orders by restaurant
GET     /api/orders/user/{id}                    # Orders by user
```

### Health Check

```
GET     /api/health                              # Server health check
```

---

## 🧠 REST Principles Followed

| Principle                        | Implementation                                                                    |
| -------------------------------- | --------------------------------------------------------------------------------- |
| ✅ **Resource-Based URIs**       | Noun-based paths — `/restaurants`, `/dishes`, `/orders`                           |
| ✅ **HTTP Methods**              | GET (read), POST (create), PUT (replace), PATCH (partial update), DELETE (remove) |
| ✅ **Stateless Communication**   | Every request is fully self-contained — no server-side sessions                   |
| ✅ **JSON Format**               | All requests and responses use `Content-Type: application/json`                   |
| ✅ **HTTP Status Codes**         | `200`, `201`, `400`, `404`, `409`, `500` — used correctly and consistently        |
| ✅ **Consistent Error Handling** | Uniform error response structure with `status`, `message`, `error_code`           |

---

## 🛡️ Input Validation

The API enforces strict validation at every endpoint:

| Validation Type        | Behaviour                                            |
| ---------------------- | ---------------------------------------------------- |
| **Required fields**    | Returns `400` with the missing field name            |
| **Data type checks**   | Type mismatches caught and reported                  |
| **Conflict detection** | Duplicate restaurant / user returns `409 Conflict`   |
| **Invalid ID**         | Non-existent resource returns `404 Not Found`        |
| **Bad request body**   | Descriptive messages returned, never a generic `500` |

---

## 🏗 Architecture

The project follows a clean **4-layer architecture**:

```
┌──────────────────────────────────────────────────────────┐
│                      ROUTES LAYER                         │
│          HTTP Request Handling — API Endpoints            │
│  restaurant_routes.py · dish_routes.py · order_routes.py │
└──────────────────────────────┬───────────────────────────┘
                               │  delegates to
                               ▼
┌──────────────────────────────────────────────────────────┐
│                     SERVICE LAYER                         │
│       Business Logic — Validation, Processing, Rules      │
│  restaurant_service.py · dish_service.py · user_service   │
└──────────────────────────────┬───────────────────────────┘
                               │  reads / writes
                               ▼
┌──────────────────────────────────────────────────────────┐
│                      MODELS LAYER                         │
│            Data Management — Storage & Retrieval          │
│         restaurant.py · dish.py · user.py · order.py      │
└──────────────────────────────┬───────────────────────────┘
                               │  verified by
                               ▼
┌──────────────────────────────────────────────────────────┐
│                      TESTS LAYER                          │
│         Quality Assurance — Pytest & Robot Framework      │
│              tests/pytest/ · tests/robot/                 │
└──────────────────────────────────────────────────────────┘
```

**Architecture Benefits:**

| Benefit                    | Why It Matters                                   |
| -------------------------- | ------------------------------------------------ |
| **Separation of Concerns** | Each layer has a single, focused responsibility  |
| **Testability**            | Services and models can be tested independently  |
| **Maintainability**        | Changes in one layer don't cascade unnecessarily |
| **Extensibility**          | New features slot into a single layer            |

---

## 📂 Project Structure

```
Foodie_App/
│
├── 📄 app.py                           # Flask app entry point
├── 📄 config.py                        # App configuration
├── 📄 requirements.txt                 # All Python dependencies
│
├── 📁 routes/                          # HTTP route handlers
│   ├── 📄 restaurant_routes.py         # Restaurant CRUD endpoints
│   ├── 📄 dish_routes.py               # Dish CRUD endpoints
│   ├── 📄 user_routes.py               # User registration & search
│   ├── 📄 admin_routes.py              # Admin management endpoints
│   └── 📄 order_routes.py              # Order retrieval endpoints
│
├── 📁 services/                        # Business logic layer
│   ├── 📄 restaurant_service.py        # Restaurant validation & rules
│   ├── 📄 dish_service.py              # Dish validation & rules
│   ├── 📄 user_service.py              # User validation & rules
│   └── 📄 order_service.py             # Order processing logic
│
├── 📁 models/                          # Data models & storage
│   ├── 📄 restaurant.py                # Restaurant model
│   ├── 📄 dish.py                      # Dish model
│   ├── 📄 user.py                      # User model
│   └── 📄 order.py                     # Order model
│
├── 📁 utils/                           # Utility helpers
│   ├── 📄 validators.py                # Input validation utilities
│   └── 📄 response_helpers.py          # Standardized response builders
│
├── 📁 tests/
│   ├── 📁 pytest/                      # Pytest automation
│   │   ├── 📄 conftest.py              # Flask test client fixtures
│   │   ├── 📄 test_restaurants.py      # Restaurant endpoint tests
│   │   ├── 📄 test_dishes.py           # Dish endpoint tests
│   │   ├── 📄 test_users.py            # User endpoint tests
│   │   ├── 📄 test_admin.py            # Admin endpoint tests
│   │   └── 📄 test_orders.py           # Order endpoint tests
│   │
│   └── 📁 robot/                       # Robot Framework tests
│       ├── 📄 restaurant_tests.robot   # Restaurant test suite
│       ├── 📄 dish_tests.robot         # Dish test suite
│       ├── 📄 user_tests.robot         # User test suite
│       └── 📄 variables.robot          # Base URL and test data
│
└── 📄 README.md
```

---

## 💻 Installation

### Prerequisites

| Tool    | Version | Link                                            |
| ------- | ------- | ----------------------------------------------- |
| Python  | 3.8+    | [python.org](https://python.org)                |
| pip     | Latest  | Bundled with Python                             |
| Git     | Any     | [git-scm.com](https://git-scm.com)              |
| Postman | Any     | [postman.com](https://postman.com) _(optional)_ |

### Step 1 — Clone the Repository

```bash
git clone https://github.com/saiprakash0506/Wipro_Group5_Project.git
cd Wipro_Group5_Project/Foodie_App
```

### Step 2 — Create Virtual Environment

```bash
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — macOS / Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Application

### Start the Flask Server

```bash
python app.py
```

The API is now live at: **`http://localhost:5000`**

### Verify Server is Running

```bash
curl http://localhost:5000/api/health

# Expected response:
# {"status": "success", "message": "Server is healthy"}
```

---

## 🧪 Testing

> **Important:** Ensure the Flask server is running (`python app.py`) before executing automated tests.

---

### Manual Testing — Postman

1. Import the Postman collection (if available in the repo)
2. Set `base_url` variable to `http://localhost:5000`
3. Test each endpoint with both valid and invalid payloads
4. Verify HTTP status codes match the documented contract
5. Check response body structure against the API contract below

---

### Automated Testing — Pytest

**What is validated:**

- HTTP status codes for all 18 endpoints
- Response body fields and values
- JSON schema validation via `jsonschema`
- Positive scenarios (valid inputs → 200 / 201)
- Negative scenarios (invalid input → 400 / 404 / 409)
- Multi-step integration flows (register → order → rate)

```bash
# Ensure Flask is running first
python app.py

# Navigate to pytest folder
cd tests/pytest

# Run all tests
pytest -v

# Run a specific module
pytest test_restaurants.py -v
pytest test_dishes.py -v
pytest test_orders.py -v

# Generate HTML report
pytest --html=../../reports/pytest_report.html --self-contained-html

# Run with coverage
pytest --cov=../../ --cov-report=html
```

**Sample Pytest Test:**

```python
def test_register_restaurant(client):
    response = client.post('/api/restaurants', json={
        'name':     'Test Restaurant',
        'cuisine':  'Italian',
        'location': 'Downtown'
    })
    assert response.status_code == 201
    assert response.json['status'] == 'success'
    assert 'registered successfully' in response.json['message']


def test_duplicate_restaurant_returns_409(client):
    payload = {'name': 'Same Name', 'cuisine': 'Indian', 'location': 'Hyderabad'}
    client.post('/api/restaurants', json=payload)           # First — should succeed
    response = client.post('/api/restaurants', json=payload) # Second — should conflict
    assert response.status_code == 409
```

---

### Automated Testing — Robot Framework

**What is validated:**

- Full keyword-driven E2E integration flows
- Data-driven test cases with centralized variable files
- Step-by-step execution with keyword-readable test names
- Detailed `log.html` for debugging failures

```bash
# Ensure Flask is running first
python app.py

# Navigate to robot folder
cd tests/robot

# Run all suites
robot .

# Run a specific suite
robot restaurant_tests.robot
robot dish_tests.robot

# Custom output directory
robot --outputdir ../../reports .

# Override base URL
robot --variable BASE_URL:http://localhost:5000 .
```

**Sample Robot Test:**

```robot
*** Settings ***
Library     RequestsLibrary
Variables   variables.robot

*** Test Cases ***
Register New Restaurant Successfully
    [Documentation]    POST /api/restaurants should return 201
    ${body}=    Create Dictionary
    ...    name=Test Restaurant    cuisine=Italian    location=Downtown
    ${response}=    POST    ${BASE_URL}/api/restaurants    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
    Should Be Equal    ${response.json()}[status]    success

Duplicate Restaurant Returns 409 Conflict
    [Documentation]    Registering the same restaurant twice returns 409
    ${body}=    Create Dictionary    name=Same Name    cuisine=X    location=Y
    POST    ${BASE_URL}/api/restaurants    json=${body}
    ${response}=    POST    ${BASE_URL}/api/restaurants    json=${body}
    Should Be Equal As Integers    ${response.status_code}    409
```

---

## 📬 API Response Format

All endpoints follow a **consistent JSON response contract**:

### ✅ Success Response (200 / 201)

```json
{
  "status": "success",
  "message": "Restaurant registered successfully",
  "data": {
    "id": 1,
    "name": "Test Restaurant",
    "cuisine": "Italian",
    "location": "Downtown",
    "approved": false
  }
}
```

### ❌ Error Response (400 / 404 / 409 / 500)

```json
{
  "status": "error",
  "message": "Restaurant with this name already exists",
  "error_code": "DUPLICATE_RESTAURANT"
}
```

### HTTP Status Code Reference

| Code               | Meaning                       | When Used            |
| ------------------ | ----------------------------- | -------------------- |
| `200 OK`           | Successful fetch or update    | GET, PUT, PATCH      |
| `201 Created`      | Resource successfully created | POST success         |
| `400 Bad Request`  | Invalid or missing input      | Validation failures  |
| `404 Not Found`    | Resource does not exist       | Invalid ID in URL    |
| `409 Conflict`     | Duplicate resource            | Existing name / user |
| `500 Server Error` | Unexpected server failure     | Unhandled exceptions |

---

## 📊 Reports

### Pytest Reports

> Located in: `reports/pytest_report.html`

| File                 | Description                                           |
| -------------------- | ----------------------------------------------------- |
| `pytest_report.html` | Visual summary — pass/fail, duration, failure details |
| `htmlcov/index.html` | Line-by-line code coverage per module                 |

### Robot Framework Reports

> Located in: `reports/`

| File          | Description                                       |
| ------------- | ------------------------------------------------- |
| `report.html` | High-level test statistics and suite summary      |
| `log.html`    | Full step-by-step keyword execution log           |
| `output.xml`  | Machine-readable — suitable for CI/CD integration |

---

## 🏆 Project Status

| Component                  | Status         | Notes                             |
| -------------------------- | -------------- | --------------------------------- |
| Flask REST API             | ✅ Complete    | 18 endpoints across 5 modules     |
| Input Validation           | ✅ Complete    | All edge cases handled            |
| Error Handling             | ✅ Complete    | Consistent response format        |
| Manual Testing (Postman)   | ✅ Complete    | All endpoints verified            |
| Pytest Automation          | ✅ Complete    | Positive & negative scenarios     |
| Robot Framework Automation | ✅ Complete    | Keyword-driven integration tests  |
| HTML Reports               | ✅ Complete    | Auto-generated by both frameworks |
| Documentation              | ✅ Complete    | —                                 |
| Code Review                | 🟡 In Progress | Ready for mentor review           |

---

## 🎯 Learning Outcomes

| Skill                    | What Was Learned                                       |
| ------------------------ | ------------------------------------------------------ |
| **Flask REST API**       | Routing, request parsing, JSON responses               |
| **RESTful Design**       | Resource naming, HTTP verbs, statelessness             |
| **Input Validation**     | Required fields, type checks, conflict detection       |
| **Layered Architecture** | Routes → Services → Models separation                  |
| **Postman**              | Manual testing, environment variables, collections     |
| **Pytest (API)**         | HTTP calls via `requests`, fixtures, schema validation |
| **Robot Framework**      | RequestsLibrary, keyword-driven API tests              |
| **Integration Testing**  | Multi-step flows — register → order → rate             |
| **Report Generation**    | HTML reports from both frameworks                      |
| **API Documentation**    | Writing clear, consumable API contracts                |

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "feat: describe your change"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

Developed for educational purposes as part of the **Wipro Training Program**.

---

<div align="center">

**Built with ❤️ by Wipro Group 5**

_Happy Coding! 🚀_

[![Repo](https://img.shields.io/badge/GitHub-Foodie__App-181717?style=flat-square&logo=github)](https://github.com/saiprakash0506/Wipro_Group5_Project/tree/main/Foodie_App)

</div>
