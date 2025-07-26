Inventory Management API 📦
A robust and high-performance RESTful API for managing product inventory, built with Python and FastAPI. This project demonstrates best practices in modern backend development, including asynchronous programming, database integration, data validation, and automated testing.

Key Features
Full CRUD Functionality: Create, Read, Update, and Delete operations for products.

Asynchronous: Built on FastAPI for high-performance, non-blocking I/O.

Data Validation: Uses Pydantic for robust request and response data validation.

Database Integration: Uses SQLAlchemy ORM for seamless interaction with a relational database (PostgreSQL in production, SQLite for local development).

Automated Testing: Includes a suite of unit tests written with Pytest to ensure reliability.

Dependency Injection: Leverages FastAPI's dependency injection system for managing database sessions.

Deployment Ready: Configured to be deployed on cloud platforms like Render using environment variables.

Tech Stack
Language: Python 3.12

Framework: FastAPI

Database: SQLAlchemy | PostgreSQL | SQLite

Testing: Pytest

Data Validation: Pydantic

Server: Uvicorn

Local Setup
Clone the repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Create and activate a virtual environment:

Bash

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies:

Bash

pip install -r requirements.txt
Run the application:

Bash

uvicorn inventory_api.main:app --reload
Access the interactive API documentation at http:your_ip:8000/docs.

API Endpoints

Method	Endpoint	Description
POST	/products/	Create a new product.
GET	/products/	Retrieve a list of all products.
GET	/products/{product_id}	Retrieve a single product by its ID.
PUT	/products/{product_id}	Update an existing product.
DELETE	/products/{product_id}	Delete a product.

Export to Sheets
Running Tests
To run the automated tests, execute the following command from the root directory:

Bash

pytest