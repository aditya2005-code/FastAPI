from fastapi import FastAPI
from pydantic import BaseModel
from dtos import ProductDTO
from mockData import products

app = FastAPI()

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)

    return {"status" : "Successfully product is added in the library" , "data":products}

@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO,product_id:int):
    product_data =product_data.model_dump()

    for index,p in enumerate(products):
        if(p.get("id") == product_id):
            products[index] = product_data
            return {"message" : "The data is updated" , "data":products}
        
    return {"error" : "Id not found"}


@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index,p in enumerate(products):
        if p.get("id") == product_id :
            products.pop(index)
            return {"message" : "The data is successfully deleted" , "data":products}
    
    return {"error" : "The id is not found"}
        
    
