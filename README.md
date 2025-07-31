# Exam-prog2-API

This repository contains **answers** for the HEI FastAPI evaluation held on **July 31, 2025**. It implements a minimal API using FastAPI, covering all the required endpoints.

---

## Prerequisites

* Python 3.10+
* Git
* Postman

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:Mathieu-bot/exam-prog2-API.git
   cd exam-prog2-API
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:

   ```bash
   uvicorn main:app --reload
   ```

4. Access the API at:
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Implemented Endpoints

### Q1: GET /ping

* **URL**: `/ping`
* **Method**: GET
* **Response**: `"pong"` (200)

### Q2: GET /home

* **URL**: `/home`
* **Method**: GET
* **Response**: `<h1>Welcome home!</h1>` (200)

### Q3: GET /{unknown}

* **URL**: Any unmatched route (e.g., `/test`)
* **Method**: GET
* **Response**: `<h1>404 NOT FOUND</h1>` (404)

### Q4: POST /posts

* **URL**: `/posts`
* **Method**: POST
* **Body**:

  ```json
  [
    {
      "author": "John",
      "title": "Post 1",
      "content": "Text",
      "creation_datetime": "2025-07-31T10:00:00"
    }
  ]
  ```
* **Response**:

  ```json
  {
    "posts": []
  }
  ```

  (201)

### Q5: GET /posts

* **URL**: `/posts`
* **Method**: GET
* **Response**:

  ```json
  {
    "posts": []
  }
  ```

  (200)

### Q6: PUT /posts

* **URL**: `/posts`
* **Method**: PUT
* **Body**:

  ```json
  [
    {
      "author": "John",
      "title": "Post 1",
      "content": "Updated",
      "creation_datetime": "2025-07-31T10:00:00"
    }
  ]
  ```
* **Response**:

  ```json
  {
    "posts": []
  }
  ```

  (200)

### Bonus: GET /ping/auth

* **URL**: `/ping/auth`
* **Method**: GET
* **Header**:

  ```
  Authorization: Basic YWRtaW46MTIzNDU2
  ```
* **Response**:

   * `"pong"` (200)
   * Error (401 or 403)

---

## Testing with Postman

1. Create a `postman/` folder in the project root.
2. Test each endpoint and save screenshots as:

   * `Q1.png` → GET /ping
   * `Q2.png` → GET /home
   * `Q3.png` → GET /test (unknown route)
   * `Q4.png` → POST /posts
   * `Q5.png` → GET /posts
   * `Q6.png` → PUT /posts

---

## File Structure

```
exam-prog2-API/
├── api/routes.py
├── models/post.py
├── templates/
│   ├── home.html
│   └── not_found.html
├── main.py
├── README.md
├── requirements.txt
└── postman/
    ├── Q1.png
    ├── Q2.png
    ├── Q3.png
    ├── Q4.png
    ├── Q5.png
    └── Q6.png
```

---

## Templates

* `templates/home.html`:

  ```html
  <h1>Welcome home!</h1>
  ```

* `templates/not_found.html`:

  ```html
  <h1>404 NOT FOUND</h1>
  ```

---

