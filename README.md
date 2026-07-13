

---

# URL Shortener API

A clean and efficient URL shortener REST API built with Django and Django REST Framework. This service creates compact, 6-character hashes for long links, handles fast redirects, and provides full CRUD management for shortened URLs.

## Key Features

* Deterministic Hashing: Uses MD5 hashing to generate predictable, unique 6-character short codes.
* Instant Redirection: Performs clean HTTP redirects for lightning-fast routing.
* Avoid Duplicates: Automatically catches previously shortened URLs to save database storage.

## API Endpoints Reference

### 1. Shorten a URL

* URL: /add/
* Method: POST
* Request Body:

```json
{
  "long_url": "https://www.example.com/some/very/long/path/to/a/page"
}

```

* Response (200 OK):

```json
{
  "id": 1,
  "short_code": "a1b2c3",
  "long_url": "https://www.example.com/some/very/long/path/to/a/page",
  "created_at": "2026-07-13",
  "updated_at": "2026-07-13"
}

```

### 2. View Shortened Link Meta Info

* URL: /long/short_code
* Method: GET

### 3. Update a Target URL

* URL: /up/short_code
* Method: PUT
* Request Body:

```json
{
  "long_url": "https://www.new-destination.com"
}

```

### 4. Delete a Short URL Record

* URL: /del/short_code
* Method: DELETE

### 5. Hit Redirect Route

* URL: /short_code
* Method: GET
* Behavior: Performs a direct HTTP redirect to your stored long_url.

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

```

### 2. Set Up Your Virtual Environment

```bash
python -m venv venv

```

Activate it on Windows:

```bash
venv\Scripts\activate

```

Activate it on macOS/Linux:

```bash
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run Migrations and Start Server

```bash
python manage.py migrate
python manage.py runserver

```

The server will boot locally at [http://127.0.0.1:8000/](https://www.google.com/search?q=http://127.0.0.1:8000/)
