# Inventory Management API 📦

High-performance RESTful API for managing product inventory, built with FastAPI and modern Python practices.

## ✨ Features

- **Fast & Async** - Built with FastAPI for high-performance operations
- **Full CRUD** - Complete product management (Create, Read, Update, Delete)
- **Data Validation** - Pydantic schemas for robust request/response handling
- **Database Ready** - SQLAlchemy with PostgreSQL (prod) / SQLite (dev)
- **Testing Suite** - Comprehensive Pytest coverage
- **Cloud Deploy** - Ready for Render, Docker, and other platforms

## 🛠️ Tech Stack

- **Python 3.12** + **FastAPI**
- **SQLAlchemy** + **PostgreSQL/SQLite**
- **Pydantic** for validation
- **Pytest** for testing
- **Uvicorn** server

## 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/Aayushvsv/inventory_management_api.git
cd inventory_management_api

# Virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn inventory_api.main:app --reload
```

**Access:**
- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/products/` | Create product |
| `GET` | `/products/` | List all products |
| `GET` | `/products/{id}` | Get product by ID |
| `PUT` | `/products/{id}` | Update product |
| `DELETE` | `/products/{id}` | Delete product |

### Example Usage

```bash
# Create a product
curl -X POST "http://localhost:8000/products/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Wireless Mouse",
    "price": 29.99,
    "quantity": 100,
    "category": "Electronics"
  }'
```

## 📁 Project Structure

```
inventory_management_api/
├── inventory_api/
│   ├── main.py          # FastAPI app
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   └── database.py      # DB configuration
├── tests/               # Test suite
├── requirements.txt
└── .env.example
```

## 🧪 Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=inventory_api
```

## 🚀 Deployment

### Environment Variables
```env
# Development
DATABASE_URL=sqlite:///./inventory.db

# Production
DATABASE_URL=postgresql://user:password@host:port/database
```

### Docker
```bash
docker build -t inventory-api .
docker run -p 8000:8000 inventory-api
```

### Render
1. Connect GitHub repo
2. Set `DATABASE_URL` environment variable
3. Build: `pip install -r requirements.txt`
4. Start: `uvicorn inventory_api.main:app --host 0.0.0.0 --port $PORT`

## 🤝 Contributing

1. Fork the repo
2. Create feature branch: `git checkout -b feature-name`
3. Add tests and make changes
4. Submit pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

---

⭐ **Star this repo if you found it helpful!**
