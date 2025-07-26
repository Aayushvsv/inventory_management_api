from pydantic import BaseModel, ConfigDict # Import ConfigDict

class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)