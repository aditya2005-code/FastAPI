from fastapi import FastAPI , Request
from mockData import products

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "This is home page"}


# Path Params
@app.get("/products/{product_id}")
def get_product(product_id:int):
    product = None
    for p in products:
        if(p.get("id") == product_id):
            return p
        
    return {"error" : "Product not found in the list"}

#Query Params
@app.get("/greet")
def greet(request:Request):
    query_params = request.query_params

    return {
        "greet":f"Hello {query_params.get("name")}. You are {query_params.get("age")} years old"
    }