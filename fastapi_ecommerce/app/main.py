from fastapi import FastAPI,HTTPException,Query
from service.products import load_product , get_all_products

app=FastAPI()



# @app.get("/products")
# def get_product():
#     return get_all_products()

@app.get("/products")
def list_product(
    name:str=Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Search product by Name(case insensitive)",)
): 

    
    products=get_all_products()
   
    if name :
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name","").lower()]

        if not products:
            raise HTTPException(status_code=404,detail=f"no product found matching name ={name}")

        total = len(products)
    return {
        "total":total,
        "items":products
    }