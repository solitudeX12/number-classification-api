# 📊 Number Classification API

## Overview

This project implements a Number Classification API using FastAPI and deploys it to AWS Lambda with API Gateway as the public-facing endpoint. The API takes a number as input and returns its mathematical properties and a fun fact.

---

## 🚀 Features
✅ Accepts integer inputs via `GET /classify/{number}`  
✅ Returns **JSON** with number properties (even/odd, prime, Fibonacci, etc.)  
✅ Provides a **fun fact** about the number  
✅ Handles **CORS** for cross-origin requests  
✅ Returns **HTTP status codes** for proper validation  
✅ Publicly deployable  

---

## 🛠️ Technologies Used
- **FastAPI** - Web framework for API development  
- **Uvicorn** - ASGI server for running FastAPI  
- **Python 3.7+** - Programming language  
- **Httpx** - For making external API requests.

---

## 📥 Installation & Setup
### 🔹 **1. Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/number-classification-api.git
cd number-classification-api
### 🔹 **2. Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
### 🔹 **3. Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
---

## 🚀 Running the API Locally
```
uvicorn main:app --reload
```
API will be accessible at:
Local URL: http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs

---

## 📡 API Endpoints
### Classify Number
**Endpoint:** `GET /api/classify-number?number=<integer>`

#### Example Request:
```sh
curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371"
```

---

### Example Response:
```
{
    "number": 7,
    "error": false,
    "is_even": false,
    "is_prime": true,
    "is_fibonacci": true,
    "fun_fact": "Seven is considered a lucky number in many cultures."
}
```

---

## Error Handling:

If a non-integer input is provided:
```
{
    "number": "abc",
    "error": true
}
```

---

## 🌍 Deployment:

You can deploy the API using AWS EC2, AWS Lambda, or Docker.
I deployed the API using Lambda and API gateway.
Check out this blog post for instructions;

---

## 🛠 Contributing

Fork the repository
Clone your fork
Create a feature branch (git checkout -b feature-name)
Commit your changes (git commit -m "Add new feature")
Push to GitHub (git push origin feature-name)
Create a Pull Request

---

## 📜 License

This project is open-source under the MIT License.
