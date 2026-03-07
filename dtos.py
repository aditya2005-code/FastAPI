from pydantic import BaseModel

class ProductDTO(BaseModel):
    id:int
    name:str
    price:int
    category:str
    stock:int
    rating:float